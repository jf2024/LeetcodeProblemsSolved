def simplify_path(path: str) -> str:
    """
    Transforms an absolute Unix-style path into its simplified canonical path.
    
    Rules:
    - '.' represents current directory (ignore).
    - '..' represents parent directory (go up one level).
    - '//' is treated as a single '/'.
    - Canonical path starts with '/', no trailing '/', no '.' or '..'.

    TIME: O(N)
        - traverse the entire string once to find delimiters (O(N))
        - our loop to iterate the elements (O(N))
        - joining with "/" (also O(N))
        - so O(3(N)) which is just O(N)

    SPACE: O(N)
        - stack at the worst case will store most characters from the path O(N) so final string is O(N)
    """
    path_split = path.split("/")
    stack = []

    for char in path_split:
        if char != '' and char != '..' and char != '.':
            stack.append(char)

        elif stack and char == '..' :
            stack.pop()

    ans = "/" + "/".join(stack)
    return ans


def run_tests():
    test_cases = [
        ("/home/", "/home"),
        ("/home//foo/", "/home/foo"),
        ("/home/user/Documents/../Pictures", "/home/user/Pictures"),
        ("/../", "/"),
        ("/.../a/../b/c/../d/./", "/.../b/d"),
        # ("/a/./b/../../c/", "/c"),
        # ("/a//b////c/d//././/..", "/a/b/c"),
    ]

    for i, (path, expected) in enumerate(test_cases, 1):
        result = simplify_path(path)
        passed = result == expected
        print(f"Test case {i}: Input='{path}', Expected='{expected}', Got='{result}', Passed={passed}")


if __name__ == "__main__":
    run_tests()
