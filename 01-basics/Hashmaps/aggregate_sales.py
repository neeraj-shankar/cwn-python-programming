"""
Summarize data that is already grouped.

The Task:
You have a dictionary of sales per month per city. Calculate the total sales for each city across all months.

sales_data = {
    "January": {"New York": 200, "Mumbai": 500},
    "February": {"New York": 300, "Mumbai": 400},
    "March": {"New York": 100, "London": 800}
}

Expected Output: {"New York": 600, "Mumbai": 900, "London": 800}
"""


class AggregateSalesData:

    @staticmethod
    def solution_bruteforce(sales_data: dict) -> dict:
        """
        1. Create a dictionary to store answer
        2. Vist sales data for each month, Check the if the key city exists in result
        3. If not --> sum the sales value to existing key else create new key and store value
        """

        result = {}

        for data in sales_data.values():

            for city, amount in data.items():

                result[city] = result.get(city, 0) + amount
        return result


if __name__ == "__main__":
    sales_data = {
        "January": {"New York": 200, "Mumbai": 500},
        "February": {"New York": 300, "Mumbai": 400},
        "March": {"New York": 100, "London": 800},
    }

    ans = AggregateSalesData.solution_bruteforce(sales_data)
    print("Aggregated Sales Data: ", ans)
