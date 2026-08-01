import random
def Rock_Paper_Scissor():
    print('''   
Let's Play Rock, Paper & Scissor
Enter :
r for choosing Rock
p for choosing Paper
s for choosing Scissor
    ''')
    compscore = 0
    yourscore = 0
    for i in range(1,4):
        computer = random.choice([1,2,3])
        youstr = input("Enter your choice: ")
        youstr1 = youstr.lower()
        if (((youstr1 != "r" )== True) and ((youstr1 != "p") == True) and ((youstr1 != "s") == True)):
            print("Enter a valid input\n")
            return
        youDict = {"r":1, "p":2, "s":3}
        you = youDict[youstr1]
        reverseDict = {1:"Rock", 2:"Paper", 3:"Scissor"}
        print(f"Your choice is {reverseDict.get(you)}")
        print(f"Computer choice is {reverseDict.get(computer)}")
        if(you == computer):
            print("Draw\n")
        else:
            if(you == 1 and computer == 2): 
                print("You Lose,Try Again! \n")
            elif(you == 1 and computer == 3):   
                print("You WON \n")
            elif(you == 2 and computer == 1):   
                print("You WON \n")
            elif(you == 2 and computer == 3):   
                print("You Lose,Try Again! \n")
            elif(you == 3 and computer == 1):
                print("You Lose,Try Again! \n")
            elif(you == 3 and computer == 2):
                print("You WON \n")
            else:
                print("Enter valid Input")

        if((you -  computer) == 1 or (you - computer) == -2):
            yourscore = yourscore + 1
        elif((you - computer) == 0):
            yourscore = yourscore + 0
            compscore = compscore + 0
        else:
            compscore = compscore + 1
           
    print(f"Your Score is {yourscore}")
    print(f"Computer's Score is {compscore}")
    if(yourscore == compscore):
        print("It's a draw, Try another Round")
    elif(yourscore > compscore):
        print("You are the Winner")
    elif(yourscore < compscore):
        print("Computer is the Winner")


Rock_Paper_Scissor()


    


    
