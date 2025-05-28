name=input("enter your name: ")
print("Hello",name,"Welcome to the 'HAUNTED MANSION' Adventure Game!")


answer=input("you're  standing in front of an old creaky Mansion.It's midnight\nDO knock on the door or look through the window? \n enter KNOCK or LOOK : ").lower()

if answer == "look":
    print("You stared too long.. ghost pulls you into the shadows\nYou Lodt the game!")
    print("---GAME OVER---")



elif answer=="knock":
    print("The door creaks open by itself...")  
    print("You walk into a dusty hall\n Do you go upstairs or library ")
    choice2=input("enter 'UPSTAIRS' or 'LIBRARY' : ").lower()
    if choice2=="upstairs":
        print("you find a sleeping ghost. It wakes up and gives you the treasure map for your braveness!\nYou won the game!")
        print("---GAME OVER---")

    elif choice2=="library":
        print("Books starts flying around you!You run out screaming.\n You lost the game!")
        print("---GAME OVER---") 

    else:
        print("Not a valid Option.\nYou Lost the Game!!")
        print("---GAME OVER---") 



else:
    print("Not a valid Option.\nYou Lost the Game!!")
    print("---GAME OVER---") 



















