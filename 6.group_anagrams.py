from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):      
        temp_dictionary = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            temp_dictionary[key].append(word)
            
        return temp_dictionary.values()