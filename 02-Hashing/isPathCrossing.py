def isPathCrossing(path: str) -> bool:
    """
    Given a string path of 'N', 'S', 'E', 'W', return True if the path 
    crosses itself at any point (visits a coordinate more than once).

    Time Complexity: O(N)
        - iterate each character of path once

    Space Complexity: O(N)
        - if no crossings, paths_set will grow to length n
    """
    paths_set = set()
    point = [0, 0]

    paths_set.add(tuple(point))

    for direction in path:
        if direction == 'N':
            point[0] += 1
        elif direction == "S":
            point[0] -= 1
        elif direction == "E":
            point[1] += 1
        else:
            point[1] -= 1

        if tuple(point) in paths_set:
            return True

        paths_set.add(tuple(point))
        
    return False

# you can make the N, S, E, W, as a dictionary with coordinates (as described by the leetcode solution here)
# https://leetcode.com/problems/path-crossing/editorial/?envType=problem-list-v2&envId=ajcqwr0m



if __name__ == "__main__":
    p1 = "NES"
    print(f"Test 1: {isPathCrossing(p1)}") # Expected: False

    p2 = "NESWW"
    print(f"Test 2: {isPathCrossing(p2)}") # Expected: True