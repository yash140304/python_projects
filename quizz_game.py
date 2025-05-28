print("Welcome to Quiz Game!!")
playing = input("Do You Want To Play The Game ? ")
if playing.lower() != "yes":
    quit()
else: 
    print("Okay! Let's start the game!!")

score = 0    

Answer1 = input("Question no.1 - What does Ram stands for? ")
if Answer1.lower() == "random access memory":
    print("Correct Answer!")
    score += 1
else:
    print("Incorrect Answer")  


Answer2 = input("Question no.2 - Which is the largest ocean? ")
if Answer2.lower() == "pacific":
    print("Correct Answer!")
    score += 1
else:
    print("Incorrect Answer")    


Answer3 = input("Question no.3 - What does ROM stands for? ")
if Answer3.lower() == "read only memory":
    print("Correct Answer!")
    score += 1
else:
    print("Incorrect Answer")   


Answer4 = input("Question no.4 -  What is the capital of Japan? ")
if Answer4.lower() == "tokyo":
    print("Correct Answer!")
    score += 1   
else:
    print("Incorrect Answer") 


Answer5 = input("Question no.5 - what does SMPS stands for? ")
if Answer5.lower() == "swith mode power supply":
    print("Correct Answer!")
    score += 1 
else:
    print("Incorrect Answer")  


Answer6 = input("Question no.6 - Which is the largest planet in our solar system ? ")
if Answer6.lower() == "jupiter":
    print("Correct Answer!")
    score += 1 
else:
    print("Incorrect Answer") 


Answer7 = input("Question no.7 - Which gas do plants breathe in? ")
if Answer7.lower() == "carbon dioxide":
    print("Correct Answer!")
    score += 1 
else:
    print("Incorrect Answer") 


Answer8 = input("Question no.8 - How many sides does hexagone has? ")
if Answer8 == "6":
    print("Correct Answer!")
    score += 1
else:
    print("Incorrect Answer")    


Answer9 = input("Question no.9 - What is the chemical symbol for silver? ")
if Answer9 == "Ag":
    print("Correct Answer!")
    score += 1 
else:
    print("Incorrect Answer")    


Answer10 = input("Question no.10 - Which subatomic particle of the atom has a positive charge? ")
if Answer10.lower() == "proton":
    print("Correct Answer!")
    score += 1 
else:
    print("Incorrect Answer")                               



print("Your Quiz is completed!")
print("Your final score is",score)