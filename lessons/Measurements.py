# -------------------------
# Subprograms
# -------------------------
def feet_to_inches(feet: float):
    return feet * 12
def inches_to_feet(inches):
    return inches / 12
def converter():
    try:
        while True:
            menu()
    except StopIteration:
        pass
def menu():
  dispatch()
def dispatch():
    while True:
      match input():
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
      


