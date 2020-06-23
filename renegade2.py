def intro():
    lyrics = ("Oh Mama, I'm in fear for my life from the long arm of the law\n" +
              "Lawman has put an end to my running, and I'm so far from my home\n" +
              "Oh Mama, I can hear you a-cryin', you're so scared and all alone\n" +
              "Hangman is comin' down from the gallows, and I don't have very long\n" +
              "(Yeah!)\n\n")
    return lyrics


def chorus(iteration):
    lyrics = ("The jig is up, the news is out\n" +
              "They finally found me\n" +
              "The renegade who had it made\n" +
              "Retrieved for a bounty\n" +
              "Nevermore to go astray\n")
    if iteration == 1 or iteration == 3:
        end = ("This'll be the end today\n" +
               "Of the wanted man\n")
    else:
        end = ("The judge will have revenge today\n" +
               "On the wanted man\n")
    if iteration == 3:
        end = (end + "And I don't wanna go, no, no\n" +
               "Mama, don't let 'em take me!\n" +
               "Hey, hey\n" +
               "No, no, no I can't go\n")
    return lyrics + end + "\n"


def verse():
    lyrics = ("Oh Mama, I've been years on the lam and had a high price on my head\n" +
              "Lawman said, \"Get hime dead or alive.\" I was for sure he'll see me dead\n"+
              "Dear Mama, I can hear you a-cryin', you're so scared and all alone\n"+
              "Hangman is comin' down from the gallows, and I don't have very long\n\n")
    return lyrics


def bridge():
    lyrics = ("Oh Mama, I'm in fear for my life from the long arm of the law\n" +
              "Hangman is comin' down from the gallows, and I don't have very long\n\n")
    return lyrics


def main():
    print(intro() + chorus(1) + verse() + chorus(2) + bridge() + chorus(3))


main()
