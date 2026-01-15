# 2090. K Radius Subarray Averages
# link to problem: https://leetcode.com/problems/k-radius-subarray-averages/description/

def getAverages(nums: list[int], k: int) -> list[int]:
    """
    Builds and returns an array of k-radius averages.
    The window for index i is [i - k, i + k].
    
    Complexity Analysis (Target):
    - Time: O(n) where n is the length of nums.
    """
    ans = []
    nums_length = len(nums)
    denominator = k + k + 1

    if k >= nums_length:
        return [-1] * nums_length
    
    prefix = [nums[0]]
    for i in range(1, nums_length):
        prefix.append(nums[i] + prefix[-1])

    for _ in range(k):
        ans.append(-1)

    for l in range(k, nums_length):
        if l + k >= nums_length:
            ans.append(-1)
        # elif l == k:
        #     ans.append(prefix[l+k] // denominator)
        else:
            window_sum = prefix[l + k] - prefix[l - k] + nums[l - k]
            ans.append(window_sum // denominator)
            #ans.append((prefix[l+k] - prefix[l-k]) // denominator)
    
    return ans

def getAveragesPrefixSum(nums: list[int], k: int) -> list[int]:
    """
    Builds and returns an array of k-radius averages.
    The window for index i is [i - k, i + k].
    
    Complexity Analysis (Target):
    - Time: O(n) where n is the length of nums.
    """
    n = len(nums)
    averages = [-1] * n #creating our block
    window_size = k + k + 1 #max window size

    if window_size > n: #if the window size is bigger then n, have to return all -1 as its impossible to build a subarray
        return averages
    
    if k == 0: #if k is 0, just return the original list
        return nums
    
    # Start our prefix sum approach here
    prefix = [nums[0]]
    for i in range(1, n):
        prefix.append(nums[i] + prefix[-1])

    #start from k and only go up to n-k
        #ensures at least k elements on their left and right
    for i in range(k, n-k):
        subArraySum = prefix[i + k] - prefix[i - k] + nums[i - k]
        average = subArraySum // window_size
        averages[i] = average
    
    return averages

def getAveragesSlidingWindow(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    averages = [-1] * n #creating our block
    window_size = k + k + 1 #max window size

    if window_size > n: #if the window size is bigger then n, have to return all -1 as its impossible to build a subarray
        return averages
    
    if k == 0: #if k is 0, just return the original list
        return nums
    
    #Sliding Window approach here

    curr_window_sum = sum(nums[:window_size]) #doing our first window here 
    averages[k] = curr_window_sum // window_size

    for i in range(window_size, n):
        curr_window_sum += nums[i] - nums[i - window_size] #then we update our window 
        averages[i - k] = curr_window_sum // window_size

    return averages

if __name__ == "__main__":
    # Test 1: Standard case
    n1, k1 = [7, 4, 3, 9, 1, 8, 5, 2, 6], 3
    print(f"Test 1: {getAverages(n1, k1)}") 
    # Expected Output: [-1, -1, -1, 5, 4, 4, -1, -1, -1]

    # Test 2: Radius 0
    n2, k2 = [100000], 0
    print(f"Test 2: {getAverages(n2, k2)}") 
    # Expected Output: [100000]

    # Test 3: Radius larger than array
    n3, k3 = [8], 100000
    print(f"Test 3: {getAverages(n3, k3)}") 
    # Expected Output: [-1]