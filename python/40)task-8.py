import random

# Step 1: Accept a word from the user
word = input("Enter a word to scramble: ")

# Step 2: Convert it into a list of characters
char_list = list(word)

# Step 3: Shuffle the characters
random.shuffle(char_list)

# Step 4: Join the shuffled characters back into a word
scrambled_word = ''.join(char_list)

# Step 5: Display the scrambled version
print("Scrambled Password:", scrambled_word)
