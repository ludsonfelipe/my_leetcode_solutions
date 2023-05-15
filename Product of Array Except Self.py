# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

nums = [1, 2, 3, 4]
# [1, 1, 2, 6]
# Output: [24,12,8,6]
lista = []
value = 1
for i in nums:
    lista.append(value)
    value*=i
value = 1
for i in range(len(nums)-1,-1,-1):
    lista[i]=lista[i]*value
    value*=nums[i]
print(lista)