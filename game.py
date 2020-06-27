def attackOrCrouch(creature, maxEnemyHealth):
    enemyHealth = maxEnemyHealth
    while enemyHealth > 0:
        print("A " + creature + " attacks!")
        print(creature + "'s Health " + str(enemyHealth) + " / " + str(maxEnemyHealth))
        print(name + "'s Health " + str(playerHealth) + " / " + str(maxPlayerHealth))
        print("Attack, or Crouch?")
        action = input("(a/c)? ")
        if action.lower() == "a":
            enemyHealth = enemyHealth - 3
        elif action.lower() == "c":
            print("error: not implemented yet")
        else:
            print("What?")
    if enemyHealth <= 0:
        print("You beat the " + creature)
        return(True)
    else:
        print("ERROR IN HEALTH CALCULATION" + str(enemyHealth))
        return(False)

name = input("What is your name? ")
print("Hello " + name)
print("Random mode, or predictable mode?")
mode = input("(R/p)? ")
if mode.lower() == "p":
    print("Predictable")
    p = True
else:
    print("Random")
    p = False
print('Tutorial')
maxPlayerHealth = 20
playerHealth = maxPlayerHealth
if attackOrCrouch("goblin", 10) == True:
    print("You win. This is the end of this <40 line game")
else:
    print("You lose. How?")