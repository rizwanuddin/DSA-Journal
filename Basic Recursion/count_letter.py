##Not recursion question
def count_letter(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count
letter = input("Enter a letter: ")
word = input("Enter a word: ")
result = count_letter(word, letter)
print(f"The letter '{letter}' appears {result} times in the word '{word}'.")