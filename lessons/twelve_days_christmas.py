DAYS: list[str] = "first second third fourth fifth sixth seventh eigth ninth tenth eleventh twelfth".split(" ")
GIFTS: list[str] = "a partridge in a pear tree/two turtle doves/three french hens/four calling birds/five gold rings".split("/")
def output_song() -> str:
   list(print(get_day(day)) for day in range(5))
def get_gift_body(day: int = 0) -> str:
    up = lambda x: "".join(v if i else v.upper() for i,v in enumerate(x))
    if day == 0:
        return up(GIFTS[0])
    elif day == 1:
        return f"{up(GIFTS[1])}\nAnd {GIFTS[0]}"
    else:
        return up(GIFTS[day]) + "\n" + get_gift_body(day - 1)
def get_day(day):
    return f"On the {DAYS[day]} of Christmas\nMy true love gave to me\n{get_gift_body(day)}."

if __name__ == "__main__":
    output_song()