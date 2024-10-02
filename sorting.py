#bubble(list) - > sorted ist

#selection(list) -> sorted list

tests = {
    "unsorted_list1" : [22,46,18,9,40,16,24,32,5,36,33,41,1,5,13],
    "unsorted_list2" : [9,50,7,0,30,50,9,12,22,45,9,42,17,13,29],
    "unsorted_list3" : [31,49,1,48,19,41,30,27,0,47,0,31,48,10,28],
    "unsorted_list4" : [8,14,43,30,6,23,33,40,19,48,7,33,45,23,35],
    "unsorted_list5" : [15,33,45,21,8,45,1,37,14,48,20,24,16,37,26],
}

def select(unsorted_list):
    for i in range(0, len(unsorted_list)):
        # smallest_number[0] = value
        # smallest_number[1] = index
        smallest_number = [unsorted_list[0], 0] 
        

        # Find the smallest number
        for e in range(0, len(unsorted_list)):
            # Check if list item at index e is smaller than smallest_number.
            new_number = [unsorted_list[i], i - 1] #  i - 1 gets the current index

            if unsorted_list[i] < new_number[0]:
                new_number = [unsorted_list[e], e]


        # Swaps each item at index 0 & smallest_number[1]
        if unsorted_list[i] < smallest_number[0]:
            temp_storage_var = unsorted_list[i]

            unsorted_list[i] = smallest_number[0]
            smallest_number[0] = temp_storage_var
            

    return unsorted_list


def main():
    for i in tests:
        print("\n") # This adds a space after each element. It also puts a space in front of the first item in 
                    # the output, which I find easier to read. 

        selected_list = tests[i]
        sorted_list = select(tests[i])

        print(f"Unsorted list: {selected_list}")
        print(f"Sorted list: {sorted_list}")
        print(f"Sort success: {selected_list == sorted}")


main()

#insertion(list) > sorted list
