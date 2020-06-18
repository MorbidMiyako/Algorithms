'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # return [max(nums[i:i+k]) for i in range(0, len(nums)-k + 1)]
    # max_array = [0] * (len(nums) - k + 1)
    # for i in range(0, len(nums)-k + 1):
    #     max_array[i] = (max(nums[i:i+k]))
    # return max_array
    max_array = []
    highest_num = 0
    highest_index = 0
    for i in range(0, k):
        if nums[i] >= highest_num:
            highest_num = nums[i]
            highest_index = i
    max_array.append(highest_num)
    # while i < len(nums) -k +1:
    for i in range(k, len(nums)):
        if nums[i] >= highest_num:
            highest_num = nums[i]
            highest_index = i
        elif highest_index + k <= i:
            highest_num = nums[i]
            for j in range(highest_index + 1, highest_index + 1 + k):
                if nums[j] >= highest_num:
                    highest_num = nums[j]
                    highest_index = j
        max_array.append(highest_num)
    return max_array


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 2, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
