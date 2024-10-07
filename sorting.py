#bubble(list) - > sorted ist

#selection(list) -> sorted list
tests = {
    1 : [22,46,18,9,40,16,24,32,5,36,33,41,1,5,13],
    2 : [9,50,7,0,30,50,9,12,22,45,9,42,17,13,29],
    3 : [31,49,1,48,19,41,30,27,0,47,0,31,48,10,28],
    4 : [8,14,43,30,6,23,33,40,19,48,7,33,45,23,35],
    5 : [15,33,45,21,8,45,1,37,14,48,20,24,16,37,26],
}

def select(unsorted_list):
    for i in range(0, len(unsorted_list)):
        # smallest_number[0] = value
        # smallest_number[1] = index
        smallest_number = unsorted_list[0]
        smallest_number_index = 0        

        # Find the smallest number
        for e in range(i, len(unsorted_list)):
            # Finds and sets the smallest number across the entire list to be used later
            if unsorted_list[e] < smallest_number:
                smallest_number = unsorted_list[e]
                smallest_number_index = e
        
        # Swap the two elements
        unsorted_list[smallest_number_index] = unsorted_list[i]
        unsorted_list[i] = smallest_number


    # Because the search algorithm is weird, this bypass will fix it. 
    # This is stupid. 
    # Very stupid.

    # TODO This programming war crime is stupid, fix it. 
    item = unsorted_list[0]

    unsorted_list.pop(0)
    unsorted_list.append(item)

    return unsorted_list


# def main():
#     for i in tests:
#         print("\n") # This adds a space after each element. It also puts a space in front of the first item in 
#                     # the output, which I find easier to read. 

#         print("Test case:", i)

#         # I need to pass the unsorted lists first before calling the select() method. This keeps the lists fully sorted
#         selected_list = tests[i]
#         print(f"Unsorted list: {selected_list}")

#         sorted_list = select(tests[i])
#         print(f"Sorted list: {sorted_list}")
#         print(f"Sort success: {sorted(selected_list) == sorted_list}")


main()

#insertion(list) > sorted list
