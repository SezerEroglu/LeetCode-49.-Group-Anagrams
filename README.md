# LeetCode-49.-Group-Anagrams

For every string, there can be only 26 different characters (given from the question)
For every string in input list, we count how many characters it has.
Then by the count (tuple(count) so it is immutable and can be used as a key) we add the string to the res {list} by the same key, the anagrams.
