def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    BRUTE FORCE SOLUTION

    HLPED FROM PERPLEXITY

    TIME: O(M * N)
        - m is nums1
        - n is nums2
        - outer loop going through every element in nums1 (m times)
        - searching: for each element in nums1, we search through nums2 to find matching value - worst case its O(N)
            - then we look through the remaining elements to find something larger, also O(N)
        - total: O(m * (N + N)) = O(M * 2N) = O(M * N)

    SPACE: O(1)
    """
    ans = []

    for i in range(len(nums1)):
        found = False

        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                find_great = j + 1

                while find_great < len(nums2):
                    if nums2[find_great] > nums1[i]:
                        ans.append(nums2[find_great])
                        found = True
                        break
                    find_great += 1

                if not found:
                    ans.append(-1)
                break

    return ans

def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Slighlty better but still brute force
    With hashing

    Time: O(M * N)
        - on the average case, will be faster then the first version above 

    Space: O(N)
    """
    val_to_index = {num: i for i, num in enumerate(nums2)}
    results = []

    for target_val in nums1:
        start_index = val_to_index[target_val]
        found_greater = False
        for j in range(start_index + 1, len(nums2)):
            if nums2[j] > target_val:
                results.append(nums2[j])
                found_greater = True
                break

        if not found_greater:
            results.append(-1)

    return results 


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    VERSION 3 
    STACK + HASHING SOLUTION

    
    TIME: O(N + M)
        - traverse nums2 to build the map (O(N))
        - traverse nums1 to get results (O(M))

    Space: O(N)
        - store the map of nums2 results
    """

    stack = []
    next_greater_map = {}

    for num in nums2:
        while stack and num > stack[-1]:
            smaller_num = stack.pop()

            next_greater_map[smaller_num] = num
    
        stack.append(num)

    ans = []
    for target in nums1:
        if target in next_greater_map:
            ans.append(next_greater_map[target])
        else:
            ans.append(-1)

    return ans


# --- Test Cases ---
def run_tests():
    test_cases = [
        {
            "nums1": [4, 1, 2],
            "nums2": [1, 3, 4, 2],
            "expected": [-1, 3, -1]
        },
        {
            "nums1": [2, 4],
            "nums2": [1, 2, 3, 4],
            "expected": [3, -1]
        },
        {
            "nums1": [1, 3, 5, 2, 4],
            "nums2": [6, 5, 4, 3, 2, 1, 7],
            "expected": [7, 7, 7, 7, 7]
        }
    ]

    print("--- Running Next Greater Element I Tests ---")
    for i, test in enumerate(test_cases, 1):
        result = next_greater_element(test["nums1"], test["nums2"])
        passed = result == test["expected"]
        status = "PASSED" if passed else "FAILED"
        print(f"Test {i}: nums1={test['nums1']}, nums2={test['nums2']}")
        print(f"Result:   {result}")
        print(f"Expected: {test['expected']}")
        print(f"Status:   {status}\n")

if __name__ == "__main__":
    run_tests()