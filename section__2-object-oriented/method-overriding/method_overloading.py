class Calculator:

    def find_sum(self, *args):

        print(args)
        print(type(args))
        for name in args:
            print (f"Hello Good Morning, {name}.")


    def keyword_arguments(self, **dictionary):
        print(dictionary)
        for k, v in dictionary.items():
            print(f"Key: {k} and value: {v}")

    def both_arguments(self, *items, **dictionary):
        print(items)
        print(dictionary)

    def upacking_args_kwargs(self, name, ID):

        print(name, ID)

if __name__ == "__main__":

    calc = Calculator()

    calc.find_sum("Ram", "Shyaam", "Mohan")

    student_data = {"name" : "Shyam", "ID": 2}
    calc.keyword_arguments(name="Shyam", ID=20)
    calc.both_arguments(1, 2, 3, 4, name="Neeraj", is_working=True)

    calc.upacking_args_kwargs(**student_data)