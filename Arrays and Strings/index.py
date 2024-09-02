# https://leetcode.com/problems/find-all-duplicates-in-an-array/

def find_duplicates(nums):
    
    i = 0
    while i < len(nums):
        correct_index = nums[i] - 1
        if nums[i] != nums[correct_index]:
            swap(nums, i, correct_index)
        else:
            i += 1

    ans = []
    for index in range(len(nums)):
        if nums[index] != index + 1:
            ans.append(nums[index])
    return ans

def swap(arr, first, second):
   
    arr[first], arr[second] = arr[second], arr[first]

if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    duplicates = find_duplicates(nums)
    print(duplicates)
