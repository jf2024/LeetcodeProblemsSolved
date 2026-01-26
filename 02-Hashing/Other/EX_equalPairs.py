from collections import defaultdict

def equalPairs(grid: list[list[int]]) -> int:
    """
    Given an n x n integer matrix grid, return the number of pairs (ri, cj) 
    such that row ri and column cj are equal.

    Time Complexity: O(N^2)
        - since the grid size is N * N, its O(N^2) as there are n^2 elements and each element is iterated over twice
        initially (once for the row and once for the column)

    Space Complexity: O(N^2)
        - if all rows and columns are unique, then the two hash maps will grow to size n, (n * n elements)
    """
    def convert_to_key(arr):
        return tuple(arr)
    
    #getting row counts
    rows_dic = defaultdict(int)
    for row in grid:
        rows_dic[convert_to_key(row)] += 1
    
    #getting column counts
    cols_dic = defaultdict(int)
    for col in range(len(grid[0])): #fixing our column index to start at the 0th position
        current_col = []

        # This inner loop moves vertically:
        # grid[0][0], then grid[1][0], then grid[2][0]... (col is fixed at 0 at first)
        # then in the next outer loop: grid[0][1], grid[1][1], grid[2][1]... (col now at 1 )
        for row in range(len(grid)):    
            current_col.append(grid[row][col]) 

        cols_dic[convert_to_key(current_col)] += 1
    

    ans = 0
    # calculate total pairs
    # if pattern appears 3 tiems as a row and 2 times as a column, 6 possible combinations (3 * 2)
    for arr in rows_dic:
        ans += rows_dic[arr] * cols_dic[arr] #if row patter arr also exists in column dict

    return ans


def equalPairs(grid: list[list[int]]) -> int:
    """
    Time Complexity: O(N^2) - same as before
    Space Complexity: O(N^2) - same as before but uses half the memory with just one hashmap 

    But a more clean design and implementation
    """

    # counting rows 
    row_counts = defaultdict(int)
    for row in grid:
        row_counts[tuple(row)] += 1

    ans = 0
    n = len(grid)

    for col in range(n):
        column = tuple(grid[row][col] for row in range(n)) #same as above with getting the column, just in one line

        # if that column arr exists and in our row dict, then just add the number of times that row appeared to total
        # if the column arr isnt in row dict, it will just return 0 and nothing gets added to ans 
        ans += row_counts[column]

    return ans 


if __name__ == "__main__":
    # Test Case 1
    g1 = [[3, 2, 1], 
          [1, 7, 6], 
          [2, 7, 7]]
    print(f"Test 1: {equalPairs(g1)}") 
    # Expected: 1 (Row 2 and Column 1 are both [2,7,7])

    # Test Case 2
    g2 = [[3, 1, 2, 2], 
          [1, 4, 4, 5], 
          [2, 4, 2, 2], 
          [2, 4, 2, 2]]
    print(f"Test 2: {equalPairs(g2)}") 
    # Expected: 3 
    # (Row 0 == Col 0)
    # (Row 2 == Col 2)
    # (Row 3 == Col 2)