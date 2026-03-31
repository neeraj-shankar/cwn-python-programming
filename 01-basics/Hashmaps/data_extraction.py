"""
Extract data from a deeply nested structure without using if/else for every level

The Task:
-----------------------------------------------------------
You have a dictionary representing a company's structure.
Write a function that takes a Department Name and a Role, and returns the name of the person in that role.

company = {
    "Engineering": {
        "Manager": "Alice",
        "Lead": "Bob"
    },
    "HR": {
        "Manager": "Charlie"
    }
}

Test Case: Get the "Lead" from "HR" (should return "Not Found").
"""


class DataExtraction:

    @staticmethod
    def get_lead_hr(company: dict) -> str:
        """
        1. Navigate to the HR department check for the key lead
        2. Return if found else not found
        """

        return company["HR"].get("Lead", "Not Found")


if __name__ == "__main__":

    company = {
        "Engineering": {"Manager": "Alice", "Lead": "Bob"},
        "HR": {"Manager": "Charlie"},
    }

    ans = DataExtraction.get_lead_hr(company)
    print(ans)
