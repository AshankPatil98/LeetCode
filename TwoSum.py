class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return[prevMap[diff], i] #returns indices
            prevMap[n] = i  #if difference not found save value to hashmap
        return
    
'''
Used hashmap. Iterate through the array. Subtract value in array from target. Check whether the difference is found in the hashmap. 
If not found continue iterating throught the array. Save previous value and index in the hashmap. Once found return the indices of
values that add up to the target number.

Time Complexity:
We are only iterating through the array once = constant time operation
Adding value to hashmap  = constant time operation
Checking whether value is in hashmap = constant time operation

O(n) 

Memory Complexity:
Hashmap occupies constant space because the space grows linearly with the number of elements

O(n)

'''