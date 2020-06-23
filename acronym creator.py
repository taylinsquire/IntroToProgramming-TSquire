phrase = input("Enter a phrase: ")

splitPhrase = phrase.split()
acronym = ""

for i in range(len(splitPhrase)):
    newLetter = splitPhrase[i]
    acronym = acronym + newLetter[0]


print(acronym.upper())
