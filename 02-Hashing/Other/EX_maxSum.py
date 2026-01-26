from collections import defaultdict
from unicodedata import digit

def maximumSum(nums: list[int]) -> int:
    """
    Given an array of integers nums, find the maximum value of nums[i] + nums[j],
    where nums[i] and nums[j] have the same digit sum (sum of their individual digits).
    Return -1 if there is no pair of numbers with the same digit sum.


    Time Complexity: O(N * (logM + logN))
        - N = number of elements in nums
        - M = value of the largest integer array
        - Calculating DigitSums = O(N * log(M))
        - Sorting Groups = O(N * logN)

    Space Complexity: O(N)
    """

    def get_digit_sum(num):
        """
        % 10 part gives us the last digit 
        // 10 chops off the last digit 

        so we extract the last digit, add to sum 
        remove the last digit
        stop when our num hits 0

        ex: if we had 123 

        first loop:
            digit_sum = 3   (123 % 10 = 3 (remainder is 3 left))
            num = 12    (123 // 10 = 12 (12.3 goes down to 12, our new num))

        second loop:
            digit_sum = 5   (12 % 10 = 2 (remainder is 2 left))
            num = 1         (12 // 10 = 1 (1.2 goes down to 1, our new num))
        
        third loop:
            digit_sum = 6   (1 % 10 = 1)
            num = 0         (1 // 10 = 0 (0.1 goes down to 0, our new num))

        stop loop and return 6

        """
        digit_sum = 0
        while num:  #if num is 0, loop will stop
            digit_sum += num % 10
            num //= 10

        return digit_sum 


    dic = defaultdict(list)
    for num in nums:
        digit_sum = get_digit_sum(num)
        dic[digit_sum].append(num)  #key is sum, value is original number from list

    ans = -1
    for key in dic:
        curr = dic[key]
        if len(curr) > 1:
            curr.sort(reverse=True) #regardless if we have more then 2 in the list, sort them so the top 2 are first and second
            ans = max(ans, curr[0] + curr[1])   #get the max 
    
    return ans


def maximumSum(nums: list[int]) -> int: 
    """
    Time Complexity: O(N * logM)
        - N = number of elements in Nums
        - M = number of digits in largest number
    Space Complexity: O(N) 

    This version, instead of storing every number in a list and sorting them like the implementation above, 
    just keep track of the largest number we have seen so far for each digit sum and update if needed
    """

    def get_digit_sum(num):
        total = 0 
        while num:  #if num is 0, loop will stop 
            total += num % 10   #gives us the last digit 
            num //= 10  #will remove the last digit 

        return total
    
    #key: digit_sum, value: largest number seen so far for that sum
    dic = defaultdict(int)
    ans = -1

    for num in nums:
        digit_sum = get_digit_sum(num)

        #check for partner
        #if we have the digit sum before, found a potential match, so add the current number with the largest stored inside
            # of the dictionary so far
        if digit_sum in dic:
            ans = max(ans, num + dic[digit_sum])    

        # regardless if we found a pair, update the dictionary
        # only keep the largest number for this digit_sum to make sure future pairs result in the highest possible sum
        dic[digit_sum] = max(dic[digit_sum], num)

    return ans


if __name__ == "__main__":
    # Test 1: Example from the prompt
    c1 = [18, 43, 36, 13, 7]
    print(f"Test 1: {maximumSum(c1)}")
    # Expected: 54  (18 + 36, both have digit sum 9)

    # Test 2: No two numbers share the same digit sum
    c2 = [10, 21, 32]
    print(f"Test 2: {maximumSum(c2)}")
    # Expected: -1

    # Test 3: Multiple numbers with the same digit sum
    c3 = [51, 42, 60, 15]  # digit sums: 6, 6, 6, 6
    print(f"Test 3: {maximumSum(c3)}")
    # Expected: 111  (60 + 51 is the max pair)

    # Test 4: Mixed case
    c4 = [7, 25, 34, 16, 61]
    print(f"Test 4: {maximumSum(c4)}")
    # Example: 34 (3+4=7) and 61 (6+1=7) -> sum 95
    # Expected: 95
