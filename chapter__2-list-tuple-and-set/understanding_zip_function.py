""" 
A simple python program to demonstrate th use of zip function 

Defination --> It used to combine multiple iterables like lists, tuples or strings into a single iterable of tuple

"""


def undertsanding_zip():
    kpi_names = [
        "cpu_utilization",
        "memory_utilizarion",
        "avg_latency",
        "min_latency",
        "max_latency",
    ]
    kpi_values = [30, 28, 7, 27, 68]

    kpi_data = zip(
        kpi_names, kpi_values
    )  # --> returns zip object by combining kpi names and kpi values data
    print(f"Zipped KPI data --> {dict(kpi_data)}")


if __name__ == "__main__":
    undertsanding_zip()
