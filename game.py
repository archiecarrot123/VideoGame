import battleSystem as battle

# Main code


print("THIS GAME HAS FEATURES NOT IMPLEMENTED CORRECTLY")
name = input("What is your name? ")
print("Hello " + name)
print("Random mode, or predictable mode? (WIP)")
mode = input("(R/p)? ")
if mode.lower() == "p":
    print("Predictable")
    p = True
else:
    print("Random")
    p = False
print("Tutorial")
maxPlayerHealthMain = 20
playerHealthMain = maxPlayerHealthMain
playerHealthMain = battle.attackOrCrouch("goblin", 10, 1, 1, playerHealthMain, maxPlayerHealthMain)
if playerHealthMain > 0:
    print("You win. This is the end of this <75 line game")
    print("Your health was: " + str(playerHealthMain) + " / " + str(maxPlayerHealthMain))
else:
    print("You lose. How?")