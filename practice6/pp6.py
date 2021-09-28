# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

word = str(input("Enter a word to check if it is a palindrome: ")).lower()
rev_word = word[::-1]

if word == rev_word:
    print(word + " is a palindrome")
else:
   print(word + " is not a palindrome")

# first_letter = word[0]
# word_len = len(word) - 1
# last_letter = word[word_len]
# if first_letter == last_letter:
#     fl_pos = 0
#     while fl_pos <= word_len:
#         fl_pos += 1
#         word_len -= 1
#         print(fl_pos)
#         print(word_len)
#         if word[fl_pos] != word[word_len]:
#             print(word + " is not a palindrome")
#             break
            
# else:
#     print(word + " is not a palindrome")


