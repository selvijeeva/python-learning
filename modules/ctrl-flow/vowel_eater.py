"""Design a vowel eater! Write a program that uses:
        a for loop;
        the concept of conditional execution (if-elif-else)
        the continue statement."""

user_word = input("Enter a word into the vowel eater : ")
word_without_vowels = ''

for letter in user_word:
       if letter in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
        continue
     word_without_vowels += letter
print("Word out of the vowel eater is : ", word_without_vowels)
