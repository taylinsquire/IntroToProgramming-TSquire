def intro():
    print("Oh Mama, I'm in fear for my life from the long arm of the law")
    print("Lawman has put an end to my running, and I'm so far from my home")
    print("Oh Mama, I can hear you a-cryin', you're so scared and all alone")
    print("Hangman is comin' down from the gallows, and I don't have very long")
    print("(Yeah!)")


def chorus(iteration):
    print("The jig is up, the news is out")
    print("They finally found me")
    print("The renegade who had it made")
    print("Retrieved for a bounty")
    print("Nevermore to go astray")
    if iteration == 1 or iteration == 3:
        print("This'll be the end today")
        print("Of the wanted man")
    else:
        print("The judge will have revenge today")
        print("On the wanted man")
    if iteration == 3:
        print("And I don't wanna go, no, no")
        print("Mama, don't let 'em take me!")
        print("Hey, hey")
        print("No, no, no I can't go")


def verse():
    print("Oh Mama, I've been years on the lam and had a high price on my head")
    print("Lawman said, \"Get hime dead or alive.\" I was for sure he'll see me dead")
    print("Dear Mama, I can hear you a-cryin', you're so scared and all alone")
    print("Hangman is comin' down from the gallows, and I don't have very long")


def bridge():
    print("Oh Mama, I'm in fear for my life from the long arm of the law")
    print("Hangman is comin' down from the gallows, and I don't have very long")


def main():
    intro()
    print()
    chorus(1)
    print()
    verse()
    print()
    chorus(2)
    print()
    bridge()
    print()
    chorus(3)


main()
