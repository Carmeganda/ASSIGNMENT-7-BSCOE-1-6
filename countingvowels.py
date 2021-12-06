#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#ex.
#input: Bahala kayo dyan
#output:
#words: 3
#vowels: 6
#consonants: 8

#STEPS:
#1. Ask for the sentence:
print("Hello, I am Mela and I will help you to count the vowels, consonants and words in your sentence")
sntnce = input("Please put your sentence here: ")

#2. Let's count the number of words, consonants and vowels:
wordsNum = len(sntnce.split())
vowelsNum = 0
consonantsNum = 0
spaceNum = 0

for count in sntnce:
    if count == "A" or count == "E" or count == "I" or count == "O" or count == "U" or \
        count == "a" or count == "e" or count == "i" or count == "o" or count == "u":
        vowelsNum = vowelsNum + 1
    elif count == " ":
        spaceNum = spaceNum + 1
    else:
        consonantsNum = consonantsNum + 1

#3. Display
print(f"The number of words: {wordsNum}")
print(f"The number of vowels: {vowelsNum}")
print(f"The number of consonants: {consonantsNum}")
print(f"\33[92mThe number of words\33[0m: \33[35m{wordsNum}\33[0m")
print(f"\33[92mThe number of vowels\33[0m: \33[35m{vowelsNum}\33[0m")
print(f"\33[92mThe number of consonants\33[0m: \33[35m{consonantsNum}\33[0m")