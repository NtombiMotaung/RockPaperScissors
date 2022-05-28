import random
print("WELCOME TO ROCK,PAPER,SCISSORS GAME")

def info():
    print("""
    rock beats scissors
    paper beats rock
    scissors beats paper
    """)

def game():
    hand = input("Please enter either r for rock, p for paper or s for scissors: ")
    options = ["r", "p", "s"]
    while hand != "s" and hand != "r" and hand != "p":
        hand = input("Please enter either r for rock, p for paper or s for scissors: ")
    else:
        machine_move = random.randint(0,2)
        machine_move = options[machine_move]
        if (hand == "r" ):
            if (machine_move == "p"):
                print("Machine wins!!!")
                print(machine_move)
            elif (machine_move == "s"):
                print("You win")
                print(machine_move)
            elif(machine_move == "r"):
                print("It's a tie")
                print(machine_move)

        elif (hand == "p" ):
            if (machine_move == "s"):
                print("Machine wins!!!")
                print(machine_move)
            elif (machine_move == "r"):
                print("You win")
                print(machine_move)
            elif(machine_move == "p"):
                print("It's a tie")
                print(machine_move)

        elif (hand == "s" ):
            if (machine_move == "r"):
                print("Machine wins!!!")
                print(machine_move)
            elif (machine_move == "p"):
                print("You win")
                print(machine_move)
            elif(machine_move == "s"):
                print("It's a tie")
                print(machine_move)
        
        

   

game()