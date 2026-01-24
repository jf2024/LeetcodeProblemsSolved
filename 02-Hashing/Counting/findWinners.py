from collections import defaultdict

def findWinners(matches: list[list[int]]) -> list[list[int]]:
    """
    Find players who have not lost any matches and players 
    who have lost exactly one match.

    Time Complexity: O(N * log(N)) - iterating matches, winners set and losers dict is O(N)
    the sorting takes O(N * log(N))

    Space Complexity: O(N)
    """
    winners_set = set()
    losers_dict = defaultdict(int)

    winner_ans = []
    loser_ans = []

    #adding to our winner set and loser dict while keeping count of the losers
    # for arr in matches:
    #     for num in range(len(arr)):
    #         if num == 0: 
    #             winners_set.add(arr[num])
    #         else:
    #             losers_dict[arr[num]] += 1

    for winner, loser in matches:
        winners_set.add(winner)
        losers_dict[loser] += 1

    losers_set = set(losers_dict.keys())

    # if the number in winners but not in losers, add to our winner list answer
    for num in winners_set:
        if num not in losers_set:
            winner_ans.append(num)

    # add the losers with only 1 lost to our loser list answer
    for key in losers_dict:
        if losers_dict[key] == 1:
            loser_ans.append(key)

    return [sorted(winner_ans), sorted(loser_ans)] #make sure its sorted here


"""
Alternative way below, much cleaner imo 

Time Complexity: O(n * log(N))
Space Complexity: O(n)
"""
def findWinners(matches: list[list[int]]) ->list[list[int]]: 
    #losses_count = {}
    losses_count = defaultdict(int)
    
    for winner, loser in matches:
        # losses_count[winner] = losses_count.get(winner, 0)
        # losses_count[loser] = losses_count.get(loser, 0) + 1
        losses_count[winner]
        losses_count[loser] += 1
    
    zero_lose, one_lose = [], []

    for player, count in losses_count.items():
        if count == 0:
            zero_lose.append(player)
        if count == 1:
            one_lose.append(player)
    
    return [sorted(zero_lose), sorted(one_lose)]
            

if __name__ == "__main__":
    m1 = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    print(f"Test 1: {findWinners(m1)}") 
    # Expected: [[1, 2, 10], [4, 5, 7, 8]]

    m2 = [[2,3],[1,3],[5,4],[6,4]]
    print(f"Test 2: {findWinners(m2)}") 
    # Expected: [[1, 2, 5, 6], []]