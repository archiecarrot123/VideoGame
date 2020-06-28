def creatureAI(creature, creatureHealth):
    if creature == "goblin":
        if creatureHealth >= 5:
            return("a") # Attack when health normal
        elif creatureHealth > 1:
            return("c") # Crouch when health low
        else:
            return("a") # Attack when health is 1