class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            word_arr = []
            for letter in word:
                word_arr.append(letter)
            word_arr.sort()
            word_sorted = ""
            for letter in word_arr:
                word_sorted += letter
            if word_sorted not in anagrams:
                anagrams[word_sorted] = [word]
            else:
                anagrams[word_sorted].append(word)
        
        return list(anagrams.values())
        

            



