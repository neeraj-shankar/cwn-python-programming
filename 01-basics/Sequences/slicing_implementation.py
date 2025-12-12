class SlicingImplementation:

    def __init__(self):
        pass 

    def nslice(self, iterable, start, end):
        pass

    def reverse_string_slicing():
    
        my_list = [10, 20, 30, 40]

        # Equivalent to:
        reversed_list = []
        for i in range(len(my_list)-1, -1, -1):  # from last index to 0
            reversed_list.append(my_list[i])

        print(reversed_list)  # [40, 30, 20, 10]


        