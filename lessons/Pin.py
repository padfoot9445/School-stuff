HASH = hash(7528) #should probably just store hash lol
def get_pin() -> bool:
    i = None
    times = 0
    while hash(i) != HASH and times < 3:
        i = int(input())
        times += 1
    return hash(i) == HASH

def main():
    output_messages = ("Locked out", "Security check passed")
    print(output_messages[get_pin()])

if __name__ == "__main__":
    main()