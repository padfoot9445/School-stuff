with open("players.txt", "r") as file:
    PLAYERS_CACHE = {i for i in file.readlines()}
def get_gamertag():
    while True:
        __input = input()
        if __input in PLAYERS_CACHE:
            print("Sorry, that gamertag is already taken. Try again.")
            continue
        write_gamertag(__input)
        return
def write_gamertag(name: str):
    with open("players.txt", "a") as file:
        file.write(name)
    print(f"Welcome {name}")

get_gamertag()