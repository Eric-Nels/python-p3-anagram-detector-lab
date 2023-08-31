class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, anagrams):
        matching_anagrams = []
        sorted_word = sorted(self.word.lower())

        for anagram in anagrams:
            if sorted(anagram.lower()) == sorted_word and anagram.lower() != self.word.lower():
                matching_anagrams.append(anagram)
        
        return matching_anagrams
           