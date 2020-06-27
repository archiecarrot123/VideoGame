def attackOrCrouch(creature, enemyHealth):
    curEnemyHealth = enemyHealth
    while curEnemyHealth > 0:
        print("A " + creature + " attacks!")
        print(creature + "'s Health " + str(curEnemyHealth) + " / " + str(enemyHealth))
        print(name + "'s Health " + "placeholder")
        print("Attack, or Crouch?")
        action = input("(a/c)? ")
        if action.lower() == "a":
            curEnemyHealth = curEnemyHealth - 3
        elif action.lower() == "c":
            print("error: not implemented yet")
        else:
            print("What?")
    if enemyHealth <= 0:
        print("You beat the " + creature)
        return(True)
    else:
        print("ERROR IN HEALTH CALCULATION" + str(curEnemyHealth))
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
if attackOrCrouch("goblin", 10) == True:
    print("You win. This is the end of this <40 line game")
else:
    print("You lose. How?")