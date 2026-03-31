import basics
from chained_tasks import fetch_user_data, process_user_data
from celery import chain, group
import idempotent_tasks
# Run the task using delay()
# remove_duplicates.delay()

# Running Tasks with custom queue

# for _ in range(20):

#     fetch_data.apply_async(args=('Netflix', 5), queue='high_priority')

# for _ in range(20):
#     fetch_data_slow.apply_async(args=('Amazon Prime', 10), queue='low_priority')

class RunTasks:

    @staticmethod
    def run_chained_tasks():
        """
        Start Worker:
        1. celery -A chained_tasks worker --loglevel=info
        2. Chain the tasks as workflow
        3. Run the workflow in celery
        """

        # Using the pipe operator (the standard way)
        workflow = fetch_user_data.s('user_1') | process_user_data.s()
        result = workflow.delay()
        print(result.get())

    
    @staticmethod
    def run_grouped_tasks():

        jobs = group(basics.add_nums(i, i) for i in range(10))
        result = jobs.apply_async()
        print(result.get())

    
    @staticmethod
    def run_idempotent():

        idempotent_tasks.process_payement.apply_async(args=('am-2026011820349', 20))


if __name__ == "__main__":

    # RunTasks.run_chained_tasks()
    # RunTasks.run_grouped_tasks()
    RunTasks.run_idempotent()


# TODO Concepts: Visibility Timeout, Dead Letter Queues, Prefetch Multiplier, Worker Pools (Solo vs Prefork vs Eventlet), Task Atomicity, and Result Expiration.
