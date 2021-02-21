# # In a town, there are N people labelled from 1 to N. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# 1 The town judge trusts nobody.
# 2 Everybody(except for the town judge) trusts the town judge.
# 3 There is exactly one person that satisfies properties 1 and 2.

# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

# If the town judge exists and can be identified, return the label of the town judge. Otherwise, return -1.

# example
# Example 1:

# Input: N = 2, trust = [[1, 2]]
# Output: 2

# Example 2:

# Input: N = 3, trust = [[1, 3], [2, 3]]
# Output: 3

#--------------------SOLUTION-------------------

#for each person who do they trust?
#who trusts a given person?
#graph problem = has dependencies of things, i.e. one trusts another
#build adjacency list to answer the above two questions

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        number_who_trust = {} #{number: how many people trust that person}
        people_who_trust = set()
        if N == 1 and not trust:
            return 1
        for truster, trustee in trust:
            if trustee not in number_who_trust:
                number_who_trust[truster] = 0
            number_who_trust[truster] += 1
            people_who_trust.add(truster)
        for person, number_who_trusts_them in number_who_trust.items():
            if person not in people who trust and number_who_trusts_them == N-1:
                return person
        return -1
