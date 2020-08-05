import random
from time import sleep
enemy=100
player=100
code="off"
def print_slow(str):
    for l in str:
        print(l,end='',flush=True)
        sleep(0.01)
def right():
  global enemy
  global player
  global code
  print_slow("You can hear the sound of a monster approaching in the darkness!\n\n")
  print_slow("To survive you need to fight with him !\n\n")
  while True:
    checkPlayerHealth()
    if enemy<1:
        print_slow("               You defeated the monster\n\n")
        print_slow("Press <<ENTER>> to continue \n\n")
        input()
        print_slow("There is something written on the wall\n\n ")
        print_slow("              45970\n\n")
        print_slow("You can try this code to open the front door of the house \n\n")
        code="on"
        print_slow("What would you like to do \n\n")
        print_slow("1: Try to open the front door of the house \n\n")
        print_slow("2: Just sit here for a while\n\n")
        while True:
          option=input()
          if option=="2" or option=="sit":
             print_slow("You are bleeding and lossing health !\n\n")
             player =player-5
             checkPlayerHealth()
             print("Health Remaining =",player,"HP\n\n")
             print_slow("What would you like to do \n\n")
            
          elif option=="1" or option=="front":
             front()
          else:
             print_slow("Wrong Input !!\n\n")

    print_slow("Choose 1 for Hard Attack ,2 for Low Attack !\n\n")
    print_slow("Hard attacks will reduce your health also !\n\n")
    choice=input()
    if choice=="1" or choice=="hard" or choice=="Hard":
        hardAttack()
    elif choice=="2" or choice=="conservative" or choice=="Conservative":
        conservAttack()
    else:
        print_slow("That's not an option\n\n")
    print()
    if enemy>=1:
        enemyAttack()
    print()
    
def front():
    if code=="off":
        print_slow("There is a lock on the door, you need to find the code\n\n")
        print_slow("To find the code you can take\n\n")
        print_slow("1: right\n\n")
        print_slow("2: left\n\n")
        while True:
            print_slow("Enter your choice\n\n")
            choice=input()
            if choice in ("right", "1","Right"):
                          right()
            elif choice in ("left","2","Left"):
                          left()
            else :
                          print_slow("Wrong Input!!!\n\n")

    elif code=="on":
         print_slow("Enter the code to open the door, you have only three chances.\n\n")
         a=1
         while True:
             if a<4:
                 c=input()
                 if c=="45970":
                     print_slow("WELL DONE!!!\n\n")
                     print_slow("The code is corect\n\n")
                     print_slow("You are free now ,you can go out of the house\n\n")
                     print_slow("\n**********YOU SURVIVED :) :) ******\n")
                     exit()
                 elif a<3 :
                     print_slow("To go out of this house ,write the correct code.\n\n")
                     print("You are left with only",(3-a),"chances.\n\n")
                     
             else :
                 print_slow("Your all three chances are over, you are permanently trapped in this house !!\n\n")
                 print_slow("                       YOU FAILED TO SURVIVE :(\n\n")
                 exit()
             a=a+1
             
def left():
        print_slow("The room is completely dark\n\n")
        print_slow("There is a light switch on the right wall\n\n")
        while True:
            print_slow("Enter <<on>> to switch on the lights\n\n")
            l=input()
            if l in ("on","On","ON"):
                print_slow("You found three keys you can try them to open the "
                      "door next to you and move out of the house\n\n")
                x=random.randint(1,3)
                while True:
                 print_slow("Enter <<key>> to pick up the keys \n\n")
                 pick=input()   
                 if pick in ("key","Key","KEY"):
                   while True:
                     print_slow("You got only one chance \n\n")
                     print_slow("So choose any one key\n\n")
                     k=int(input())
                     if k in (1,2,3):
                         if k ==x:
                          print_slow("WELL DONE!!!!\n\n")
                          print_slow("You can go out of the house\n\n")
                          print_slow("\n*******YOU SURVIVED :) ********\n")
                          exit()
                         else :
                          print_slow("This was a wrong key you got permantely trapped in this house\n\n")
                          print_slow("                    YOU FAILED TO SURVIVE :(\n\n")
                          exit()
                          
                     else :
                       print_slow("Enter the correct choice \n\n")
                       print_slow("Or you will be trapped in this house\n\n")
                   else:
                      print_slow("Please!! pick up the keys\n\n")
            else :
                print_slow("You need to switch on the lights, you cannot do anything in this dark room\n\n")
                       

def checkPlayerHealth():
    if player<1:
         print_slow("                YOU DIED :(\n\n")
         print_slow("                GAME OVER !!!")
         exit()
        
        
def enemyAttack():
    global player
    enemyAttack=random.randint(10,40)
    print_slow("ENEMY ATTACKS !!!\n\n")
    print("Attack =",enemyAttack,"HP\n\n")
    player =player-enemyAttack
    if player>0:
        print("PLAYER HEALTH REMAINING:",player,"HP\n\n")
    else:
        print_slow("PLAYER HEALTH REMAINING: 0 HP \n\n")
def conservAttack():
    global enemy
    attack=random.randint(1,15)
    print_slow("PLAYER ATTACKS !!!\n\n")
    print("Attack =",attack,"HP\n\n")
    enemy =enemy-attack
    if enemy>0:
        print("ENEMY HEALTH REMAINING:",enemy,"HP\n\n")
    else:
        print_slow("ENEMY HEALTH REMAINING: 0 HP \n\n")
def hardAttack():
    global enemy
    global player
    attack=random.randint(20,50)
    print_slow("PLAYER ATTACKS !!!\n\n")
    print("Attack =",attack,"HP\n\n")
    enemy =enemy-attack
    player=player-5
    if enemy>0:
        print("ENEMY HEALTH REMAINING:",enemy,"HP\n\n")
    else:
        print_slow("ENEMY HEALTH REMAINING: 0 HP\n\n")

print_slow("                            Enter <<START>> to start the game !!!\n\n")
start=input()
if start in ("Start","start","START"):
    
 print("\n==============================================================================================================================\n\n")
 print_slow("You will be exploring places and interacting with items in the game.\n\n")

 print_slow("Please use words like 'front', 'left', and 'right' for movement .\n\n")

 print_slow("When you are ready to continue, press the <<ENTER>> key.\n\n")
 input()

 print("\n==============================================================================================================================\n\n")
 print("\n==============================================================================================================================\n\n")
 while True:
    print_slow("You wake up in a dark room of a haunted house, You don't know where you are and how you get there \n\n")
    print_slow("There is no furniture in this room.\n\nInfront of you there is a short hallway leading to the main door of the house.\n\nThere is an open door to your left leading to a small room which is completely dark.\n\nTo your right is the living room from where some haunted sounds are coming.\n\n")
    print_slow("Where do you want to go.\n\n")
    while True:
        print_slow("Enter your choice.\n\n")
        ch=input()
        if ch =="front":
            front()
        elif ch=="right":
            right()
        elif ch== "left":
            left()
        else :
            print_slow("Wrong input!!\n\n")

else:
    print ("                         GAME OVER !!!\n\n")
    exit()
    



