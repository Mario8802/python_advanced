def insertion_sort(nums):
    for i in range(1, len(nums)):  # start from 1, because index 0 is the sorted part
        key = nums[i]  # we take the key because it will be lost when shifting
        j = i - 1  # take the last value of the sorted part

        # while we haven't reached the beginning
        # and while we haven't found the correct position to insert the key
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]  # shift the element to the right
            j -= 1  # move left

        nums[j + 1] = key  # place the key at the valid position


nums = [int(x) for x in input().split()]
insertion_sort(nums)
print(*nums)

# thanks to
# DiyanKalaydzhiev23
