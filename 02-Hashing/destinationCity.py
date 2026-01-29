# from collections import defaultdict

# def destCity(paths: list[list[str]]) -> str:
#     """
#     Given an array of paths [cityA, cityB], return the destination city.
#     The destination city is defined as the city without any path 
#     outgoing to another city.

#     My original implementation
#     """
#     city_dict = defaultdict(list)

#     for row in paths:
#         city_dict[row[0]].append(row[1])

#     city_values = city_dict.values()
#     city_keys = city_dict.keys()

#     for destinations in city_values:
#         if destinations[0] not in city_keys:
#             return destinations[0]
        
#     return None


def destCity(paths: list[list[str]]) -> str:
    """
    Given an array of paths [cityA, cityB], return the destination city.
    The destination city is defined as the city without any path 
    outgoing to another city.

    Time Complexity: O(N)
        - loop through the paths once
        - iterate the desintations set, worst case this is has many as paths 
            - so its O(N) + O(N) which is O(2n) but its just O(N)

    Space Complexity: O(N)
        - storing every city in at least one set 
        - O(2N) will reduce to O(N)
    """
    outgoings = set()
    destinations = set()

    for row in paths:
        outgoings.add(row[0])
        destinations.add(row[1])

    for stop in destinations:
        if stop not in outgoings:
            return stop
    
    return None

#Can even reduce this code further with just one set but ask chat/gemini for that or try it on my own time

    




if __name__ == "__main__":
    p1 = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    print(f"Test 1: {destCity(p1)}") # Expected: "Sao Paulo"

    p2 = [["B","C"],["D","B"],["C","A"]]
    print(f"Test 2: {destCity(p2)}") # Expected: "A"

    p3 = [["A","Z"]]
    print(f"Test 3: {destCity(p3)}") # Expected: "Z"