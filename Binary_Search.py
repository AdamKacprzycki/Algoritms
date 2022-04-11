import math


def binary_search(num_list_sorted, num_to_find):
    step = 1
    min_index = 0
    max_index = len(num_list_sorted) - 1

    while min_index <= max_index:

        mid_index = (min_index + max_index) // 2  #
        guess = num_list_sorted[mid_index]

        # Steps in loop, to check results.
        # print("Step #{0}, min_index:{1}, max_index: {2}, mid_index: {3}, guess: {4}".
        #       format(step, min_index, max_index, mid_index, guess))

        # If number to find is equal to guessed number than return no of loop steps and position index (tuple)
        if num_to_find == guess:
            return step, mid_index

        # If number to find is smaller than guessed number than ignore right part of list.
        elif num_to_find < guess:
            max_index = mid_index - 1

        # Opposite: If number to find is grater than guessed number than ignore left part of list.
        else:
            min_index = mid_index + 1

        step += 1

    return None


list_b = range(1, 100)
find_number = 20

# In general there is way to define max number of steps to find number using binary search as log(number, log base=2).
print("Maximum steps in binary search: {0}, steps of algorithm: {1}, number was found under no of index: {2}.".
      format(math.ceil(math.log(len(list_b), 2)), binary_search(list_b, find_number)[0],
             binary_search(list_b, find_number)[1]))
