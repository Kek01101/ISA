#14/9/2020, Blue, Nicolas Keck, Solutions to all of the array challenges
names = input("Please enter a list of names (Seperated with commas): ")
names = names.split(", ")

# Pink challenge
print("Challenge 1")
for a in range(0, len(names)):
    print(a, names[a])

# Red challenge
print("\nChallenge 2")
for name in names:
    if len(name) > 3:
        print(name)

# Blue challenge
print("\nChallenge 3")
for name in names:
    name.lower()
    vowels = 0
    consonants = 0
    for letter in name:
        if letter in "aeiou":
            vowels += 1
        else:
            consonants += 1
    print(f"{name}:\nVowels: {vowels}\nConsonants: {consonants}")