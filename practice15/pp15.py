# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order.

phrase = "My name is simon and I like to play chess"

def ReverseSentence(sentence):
    def Reverse(reverse):
        reverse.reverse()
        return reverse
    sentence = sentence.split()
    sentence = Reverse(sentence)
    out_string = ""
    for i in sentence:
        out_string += i
        out_string += " "
    return out_string

print(ReverseSentence(phrase))