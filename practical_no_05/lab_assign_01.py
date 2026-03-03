nums = tuple(map(int, input("Enter integers separated by space: ").split()))
print("Total items:", len(nums))
print("Last item:", nums[-1])
print("Reverse order:", nums[::-1])
print("Count of 5:", nums.count(5))
print("Count of 0:", nums.count(0))
if len(nums) > 2:
    print("After removing first and last:", nums[1:-1])
else:
    print("Not enough elements to remove first and last.")