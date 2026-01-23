"""
The Challenge: "The Flattener"

The Task:
-----------------------------------------------------------
Take a nested dictionary and turn it into a single-level dictionary where the keys are a combination
of the parent and child keys (separated by a .).

Input
-----------------------------------------------------------
nested = {
    "user": {
        "name": "KB",
        "address": {
            "city": "Indore",
            "zip": 452001
        }
    },
    "status": "Active"
}

Output
-----------------------------------------------------------
{
    "user.name": "KB",
    "user.address.city": "Indore",
    "user.address.zip": 452001,
    "status": "Active"
}

"""


class Flatten:

    @staticmethod
    def solution_brueforce(nested: dict) -> dict:
        """
        1. Iterate through the dictionary.
        2. If the value is not a dictionary, just add it to our result.
        3. If the value is a dictionary, call the function again on that sub-dictionary and prepend the current key to whatever it returns.
        """

        return Flatten.flatten(nested, "", ".")

    @staticmethod
    def flatten(d, parent_key="", sep="."):
        ans = {}

        for k, v in d.items():
            # Create the new key name
            new_key = f"{parent_key}{sep}{k}" if parent_key else k

            if isinstance(v, dict):
                ans.update(Flatten.flatten(v, new_key, sep))
            else:
                ans[new_key] = v

        return ans


if __name__ == "__main__":

    nested = {
        "user": {"name": "KB", "address": {"city": "Indore", "zip": 452001}},
        "status": "Active",
    }

    result = Flatten.solution_brueforce(nested)
    print(result)
