"""
A simple python to demonstrate the conversion of dictionary to json format and vice versa
"""
import json
from format_output import use_case_separator


def dictionary_with_numerical_value_to_json():

    student_detail = {
        "name": "Mohan Kumar",
        "roll_no": 2037,
        "total_marks": 534.29,
        "is_graduated": False
    }

    json_student_data = json.dumps(student_detail, indent=2)
    print(f"The converted data into json format:")
    print(json_student_data)


use_case_separator()
dictionary_with_numerical_value_to_json()


def convert_json_data_to_dictionary():
    json_data = '{"name": "John", "age": 30, "city": "New York"}'

    data_in_dict_format = json.loads(json_data)
    print(f"The dictionary data converted from json: ")
    print(data_in_dict_format)


use_case_separator()
convert_json_data_to_dictionary()


