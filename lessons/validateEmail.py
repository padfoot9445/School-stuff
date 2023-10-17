def validate(__input):
    parts = __input.split("@")
    SPECIALCHARS = {"_", ".", "-"}
    if len(parts) != 1 or parts[1][0] == "." or len(parts[1]) < 4 or len([i for i in parts[0] if i.isalnum() or i in SPECIALCHARS]) != len(parts[0]):
        return False
    current = 0
    first_part_len = len(parts[0])
    while current < first_part_len:
        if parts[0][current] in SPECIALCHARS and parts[0][current + 1] in SPECIALCHARS:
            #no need to check for other invalid characters because the guard clause(specifically the list comprehension) handles that
            return False
        current += 1
    return True

if validate(input()):
    print("Email address is valid.")
else:
    print("Email address is invalid.")
