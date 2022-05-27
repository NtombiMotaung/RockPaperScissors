print("WELCOME TO ROCK,PAPER,SCISSORS GAME")

def info():
    print("""
    rock beats scissors
    paper beats rock
    scissors beats paper
    """)

def game():
    print("Please enter either r for rock, p for paper or s for scissors")
    hand = input("> ")
    options = ["r", "p", "s"]