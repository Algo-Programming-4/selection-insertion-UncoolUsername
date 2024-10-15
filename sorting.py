#bubble(list) - > sorted ist

#selection(list) -> sorted list
def bubble(input_list):
    """Sort via bubble sort"""
    # Note: Two nested loops that loop the same thing feels wrong. 
    for e in range(0, len(input_list)):

        for i in range(0, len(input_list) - e): # e-1 ignores the previous searches
            if e != 0 and input_list[i + 1] < input_list[i]:
                # Store i+1 so we could switch it with i without any problems
                storage_var = input_list[i + 1]
                input_list[i+1] = input_list[i]
                input_list[i] = storage_var

    # Return the sorted list for future use later
    return input_list    


def selection(unsorted_list):
    for i in range(len(unsorted_list)):
        # smallest_number[0] = value
        # smallest_number[1] = index
        smallest_number = [unsorted_list[i], i] #FORMAT: (Item, IndexOfItem)

        # Find the smallest number
        for e in range(i, len(unsorted_list)):
            # Finds and sets the smallest number across the entire list to be used later

            if unsorted_list[e] < smallest_number[0]:
                smallest_number[0] = unsorted_list[e]
                smallest_number[1] = e

        # Swap the two elements
        temp_var = unsorted_list[i]

        unsorted_list[i] = smallest_number[0]
        unsorted_list[smallest_number[1]] = temp_var


    return unsorted_list


def insertion(unsorted_list):
    """
    This is my attempt at an insertion sort algorithm. 
    
    INPUTS:
        unsorted_list - list: The list that needs sorted
    """
    # The logic to swap the values does not need to be in the insertion loop. Keeping it here
    # keeps the runtime section of the insertion() function easier to read. 

    # TODO: I would prefer this to not be nested: This solution is not perminant. 
    def swap_values_from_indexes(input_list, index1, index2=0):
        """
        This function takes two indexes in a list and swaps them. 
        
        INPUTS: 

            input_list - list: Expects a list in which to swap
            index1 - int: Represents the index of the first item we need to swap.
            index2 - int: Represents the index of the second item we need to swap. 
        """
        
        # Note: There has to be a better way to do this without all this code duplication. 
        if type(input_list) != list or type(index1) != int or type(index2) != int:
            print(f"swap_values({type(input_list), {type(index1), type(index2)}}) - unexpected paramaters receved")
            return input_list

        temp_var = input_list[index1-1] # Due to what I assume is just 0 base indexing, [index-1] is required to get the correct item. 

        input_list[index2] = input_list[index1]    # Swaps input_list[index2] with input_list[index1].
        input_list[index1] = temp_var # Swaps input_list[index1] with temp_var.

        return input_list
    
    # Runtime section of the program

    for i in range(0, len(unsorted_list)): # Outer Loop
        for e in range(0, len(unsorted_list)): # Inner loop
            while e != 0 and unsorted_list[e] < unsorted_list[e-1]: 
                # Continuously swaps the item with the index before it until it is larger at index[e] - 1. 
                # index e must be greater than 0 for this to work. without the check this program completely breaks. 

                unsorted_list = swap_values_from_indexes(unsorted_list, e, e-1)


    return unsorted_list
#insertion(list) > sorted list
