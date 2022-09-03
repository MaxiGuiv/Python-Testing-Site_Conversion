avail_lbls = ["grams", "kilograms", "tonnes"]
print(f"Only accepts {avail_lbls} atm.")

fq = int(input("Type the number: "))
fl = input("Type the label of this: ")
tl = input("What label to convert this to?: ")

def result():
    print(f"Formula: {fq} {fl}{op}")
    print(f"Answer: {rv} {tl}")
def error():
    print("Labels are either misspelled, not in plural form, or currently not in the program.")

if fl in avail_lbls and tl in avail_lbls:
    if fl == "grams":
        if tl == "kilograms":
            rv = fq / 1000
            op = "/1000 kilograms"
        elif tl == "tonnes":
            rv = fq / 1000000
            op = "/1000000 tonnes"
    elif fl == "kilograms":
        if tl == "grams":
            rv = fq * 1000
            op = "*1000 grams"
        elif tl == "tonnes":
            rv = fq / 1000
            op = "/1000 tonnes"
    elif fl == "tonnes":
        if tl == "grams":
            rv = fq * 1000000
            op = "*1000000 grams"
        elif tl == "kilograms":
            rv = fq * 1000
            op = "*1000 kilograms"
    result()
else:
    error()
