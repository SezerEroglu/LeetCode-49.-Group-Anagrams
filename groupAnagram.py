from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for strng in strs:
            count = [0] * 26  # Lowercase letters in English alphabet
            for c in strng:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(strng)
            # we can not res[count] because a List is mutable and thus can not
            # be used as an index (or key), so we use tuple(count) to create an
            # immutable variable to use as a key
        return res.values()
