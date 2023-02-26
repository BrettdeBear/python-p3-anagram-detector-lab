# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
        # self.words = []

    def match(self, list_of_words):
        matched_words = []
        for item in list_of_words:

            if sorted(self.word) == sorted(item):
                matched_words.append(item)
                
        return matched_words
# Anagram('enlist').match(['silent'])
            # sorted_word = sorted(i)
            # if [letter for letter in self.word] == [letter for letter in sorted_word]:
            #     self.words.append(i)
            # else:
            #     return []
        

        
        # for i in list_of_words:
        #     sorted_word = sorted(i)

            # if sorted(i) == sorted(self.word):
            #     self.words.append(i)

    
# Anagram('enlist').match('listen')
#         sorted_word = sorted(self.word)
#         if sorted_word == sorted([word for word in list_of_words]):
#             print("holy moly")
# Anagram("enlist").match(["listen"])
