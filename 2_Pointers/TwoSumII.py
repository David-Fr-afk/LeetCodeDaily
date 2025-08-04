class Solution(object):
    def twoSum(self, numbers, target):
        num_set = set(numbers)
        min_val = numbers[0]  
        closest_number = target

        if not numbers:
            return [] 
        #check to find whats the closest number to the target, this is simply to make the code more efficent.
        while closest_number not in num_set and closest_number >= min_val:
            closest_number -= 1

        pointer_foward = 0                
        closest_index = numbers.index(closest_number)    
        
        for i in range (closest_index, -1, -1):
            num = numbers[i]
            num_needed = target - num
            if num_needed in num_set:
                j = numbers.index(num_needed)
        #this is the solution i worked on, where you would look for the closest number to the target, find that index, then iterate from that index down using 2 pointers,
         #then  finding directly in the list if the number needed is in the list, for ex index 4, holds a integer 6, and the target is 9, so i would have a check that would find if 3 is in the list and return that index, unfortunatly its extremley slow and hard to implement without imports.
         # i ended up just learning the fastest way to do it with 2 pointers.
         class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]  
            elif total < target:
                left += 1
            else:
                right -= 1

        return []
#this was the original way of doing it, but i assumed it would be faster to narrow the search
"i understand the logic in the better way, because its ordered, you can actually find the target faster, "
"the real ingenuity comes from the elif and else statement, where if the total is less than the target, "
"than were shooting too high so we reduce the right to get a lower number, "
"and if the total is greater than the target, "
"we need a bigger number and since its sorted we move left to the right to get a bigger number"