avail_lbls = ["g", "kg", "mg"]
print(f"Only accepts {avail_lbls} atm.")

fq = int(input("Type the number: "))
fl = input("Type the label of this: ")
tl = input("What label to convert this to?: ")

def result():
    print(f"Formula: {fq} {fl} {op} {tl}")
    print(f"Answer: {rv} {tl}")
def error():
    print("Labels are either misspelled, not in plural form, or currently not in the program.")

if fl in avail_lbls and tl in avail_lbls:
    if fl == "g":
        if tl == "kg":
            rv = fq / 1000
            op = "/1000 kilograms"
        elif tl == "mg":
            rv = fq * 1000
            op = "*1000"
    elif fl == "kg":
        if tl == "g":
            rv = fq * 1000
            op = "*1000 grams"
        elif tl == "mg":
            rv = fq * 1000000
            op = "*1000000"
    elif fl == "mg":
        if tl == "g":
            rv = fq / 1000
            op = "/1000"
        elif tl == "kg":
            rv = fq / 1000000
            op = "/1000000"
    result()
else:
    error()
