from components import vars

def total(value):
    # do some logic to see which character you selected

    if value <= 10:
        vars.character = vars.characters[0]
    elif value <= 50:
        vars.character = vars.characters[1]
    if value <= 0:
        vars.character = vars.characters[2]
    elif value >= 60:
        vars.character = vars.characters[3]
    print("You are " + vars.character)
    print("••••••••••••••••••••••••••••••••••••\n")
        # add some emoji icons, or show the character image using the Pillow package
