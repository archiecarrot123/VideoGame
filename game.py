import time
import creatureAI as AI

# Functions

def attackOrCrouch(creature, maxEnemyHealth, enemyAttack, enemyRegen, playerHealth, maxPlayerHealth):
    enemyHealth = maxEnemyHealth
    playerAttack = 3
    while enemyHealth > 0:
        print("A " + creature + " attacks!")
        print(creature + "'s Health " + str(enemyHealth) + " / " + str(maxEnemyHealth))
        print(name + "'s Health " + str(playerHealth) + " / " + str(maxPlayerHealth))
        print("Attack, or Crouch?")
        action = input("(a/c)? ")
        if action.lower() == "a":
            enemyHealth = enemyHealth - playerAttack
            print(name + "'s attack deals " + str(playerAttack) + " damage")
        elif action.lower() == "c":
            print("error: not implemented yet")
        else:
            print("What? You do nothing as you pressed " + action.lower())
        if AI.creatureAI(creature, enemyHealth) == "a":
            playerHealth = playerHealth - enemyAttack
            print(creature + "'s attack deals " + str(enemyAttack) + " damage")
        else:
            enemyHealth = enemyHealth + 1
            print(creature + " crouches and regenerates " + str(1) + " health")
        time.sleep(1)
    if enemyHealth <= 0:
        print("You beat the " + creature)
        return(playerHealth)
    else:
        print("ERROR IN HEALTH CALCULATION" + str(enemyHealth))
        return("You lose")


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
playerHealthMain = attackOrCrouch("goblin", 10, 1, 1, playerHealthMain, maxPlayerHealthMain)
if playerHealthMain > 0:
    print("You win. This is the end of this <75 line game")
    print("Your health was: " + str(playerHealthMain) + " / " + str(maxPlayerHealthMain))
else:
    print("You lose. How?")