import creatureAI as AI
import time

def attackOrCrouch(creature, maxEnemyHealth, enemyAttack, enemyRegen, playerHealth, maxPlayerHealth):
    enemyHealth = maxEnemyHealth
    playerAttack = 3
    print("A " + creature + " attacks!")
    while enemyHealth > 0:
        print()
        print(creature + "'s Health " + str(enemyHealth) + " / " + str(maxEnemyHealth))
        print("Player's Health " + str(playerHealth) + " / " + str(maxPlayerHealth))
        print("Attack, or Crouch?")
        action = input("(a/c)? ")
        if action.lower() == "a":
            enemyHealth = enemyHealth - playerAttack
            print("Player's attack deals " + str(playerAttack) + " damage")
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