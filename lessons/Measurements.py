def feet_to_inches(feet: float):
    return feet * 12
def inches_to_feet(inches):
    return inches / 12
def converter():
    try:
        while True:
            dispatch(input())
    except StopIteration:
        pass
def dispatch(i):
    match i:
        case "1":
            k = float(input())
            print(f"{k} feet is {feet_to_inches(k)} inches")
            return
        case "2":
            k = float(input())
            print(f"{k} inches is {inches_to_feet(k)} feet")
            return
        case "3":
            print("Goodbye")
            raise StopIteration()
    raise ValueError("Invalid Input")

if __name__ == "__main__":
    converter()