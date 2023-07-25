word = input("Enter a word: ")
vowels = "aeiouy"

if word[0].lower() in vowels:
    word = word + "way"
    print(word.title())
else:
    # word = word[1:] + word[0] + "ay"
    word = f"{word[1:]}{word[0]}ay"
    print(word.lower().title())