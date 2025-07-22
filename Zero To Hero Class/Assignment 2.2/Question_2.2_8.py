#8. Write a Python program that accepts a word from the user and reverses it.
#Solution:
#Thought Process:
#Create a function to reverse the word
def reverse_word(word):
    return word[::-1]
# Main program
user_word = input("Enter a word to reverse: ")
reversed_word = reverse_word(user_word)
print(f"The reversed word is: {reversed_word}")