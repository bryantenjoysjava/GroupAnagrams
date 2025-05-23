from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            anagrams[key].append(string)

        return list(anagrams.values())





