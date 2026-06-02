class Count_vowels:
    def count_vowels(self, text, index, total):
        vowels = ["a", "e", "i", "o", "u"]

        if index == len(text):
            print(total)
            return

        if text[index] in vowels:
            total += 1

        self.count_vowels(text, index + 1, total)


if __name__ == "__main__":
    sol = Count_vowels()
    text = "hello"
    sol.count_vowels(text, 0, 0)