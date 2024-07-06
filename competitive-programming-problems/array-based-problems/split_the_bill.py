"""
---------------------------------------------------------------------------------------------------

Problem Statement:
-------------------------------------------------
Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for
the items they consume. Brian gets the check and calculates Anna's portion. You must determine if 
calculation is correct.

Conditions
-------------------------------------------------
the bill has the following prices: bill[2, 4, 6]. Anna declines to eat item k= bill[2] which costs 6. 
1. If Brian calculates the bill correctly, Anna will pay (2 + 4)/2. 
2. If he includes the cost of bill[2] , he will calculate (2 +4 + 6)/2. In the second case, he should refund 3 to Anna.


"""


def check_bill(bill, k, b_charged):
    """
    Check if Brian's calculation of Anna's portion is correct.

    Parameters:
    - bill (list): The list of prices for items.
    - k (int): The index of the item Anna declines to eat.
    - b_charged (int): The amount Brian charged Anna.

    Returns:
    - str: 'Bon Appetit' if Brian's calculation is correct, or the refund amount.
    """
    anna_portion = (sum(bill) - bill[k]) // 2

    if anna_portion == b_charged:
        return "Bon Appetit"
    else:
        refund = b_charged - anna_portion
        return refund


# Example usage:
bill_items = [2, 4, 6]
declined_item_index = 2
brian_charged = 5  # Assuming Brian charged Anna $5

result = check_bill(bill_items, declined_item_index, brian_charged)
print(result)
