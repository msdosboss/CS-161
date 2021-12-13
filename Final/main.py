import classes
import functions
room1 = classes.room(classes.enemy(10,"G","potion","placeholdername",5),"firerod")
room2 = classes.room(classes.enemy(15,"G","potion","Orc",5),"waterrod")
room3 = classes.room(classes.enemy(15,"G","grassrod","troll",5),"grassrod")
room4 = classes.room(classes.enemy(15,"G","potion","Goblin",5),"victorytoken")
flag = 0
def main():
    playerroom = 1
    print("Welcome to my text adventure!\n What is your name")
    chosenname = functions.GAVW()
    print("Which magic type would you like to be? G for Grass, F for fire, W for water") #type has no use yet
    chosentype = functions.GAVT()
    player = classes.player(50,chosentype,"placeholder",chosenname,10,["potion","potion"])
    print("Good luck,",player.name)
    while(player.health > 0):
        if (playerroom == 1):
            print("welcome to room 1")
            player.health = functions.encounter(playerroom,room1.enemy.health,player.health,room1.enemy.attack,player.attack,room1.enemy.armor,player.armor,room1.enemy.name,player.inv,room1.enemy.item)
            player.inv.append(room1.loot)
            if (player.health > 0):
                playerroom = playerroom + 1
        if (playerroom == 2):
            print("welcome to room 2")
            player.health = functions.encounter(playerroom,room2.enemy.health,player.health,room2.enemy.attack,player.attack,room2.enemy.armor,player.armor,room2.enemy.name,player.inv,room2.enemy.item)
            player.inv.append(room2.loot)
            if (player.health > 0):
                playerroom = playerroom + 1
        if (playerroom == 3):
            print("welcome to room 3")
            player.health = functions.encounter(playerroom,room3.enemy.health,player.health,room3.enemy.attack,player.attack,room3.enemy.armor,player.armor,room3.enemy.name,player.inv,room3.enemy.item)
            player.inv.append(room3.loot)
            if (player.health > 0):
                playerroom = playerroom + 1
        if (playerroom == 4):
            print("welcome to room 4")
            player.health = functions.encounter(playerroom,room4.enemy.health,player.health,room4.enemy.attack,player.attack,room4.enemy.armor,player.armor,room4.enemy.name,player.inv,room4.enemy.item)
            player.inv.append(room4.loot)
            if (player.health > 0):
                playerroom = playerroom + 1
        if (player.health > 0):
            flag = 1
            player.health = 0
            print("you have won")
    if (flag == 0):
        print("you have died :(")


main()