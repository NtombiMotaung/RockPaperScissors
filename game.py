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
    
    if hand in options:
        print("yaay")
    else:
        print("nah")

game()