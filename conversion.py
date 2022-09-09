avail_lbls = ["g", "kg", "mg", "lb"]
print(f"Only accepts {avail_lbls} atm.")

fq = float(input("Type the number: "))
fl = input("Type the label of this: ")
tl = input("What label to convert this to?: ")

def result():
    print(f"Formula: {fq} {fl} {op} {tl}")
    print(f"Answer: {rv} {tl}")
def error():
    print(f"Labels are either misspelled, or currently not in the program. The only accepted labels are: {avail_lbls}")

if fl in avail_lbls and tl in avail_lbls:
    if fl == "g":
        if tl == "kg":
            rv = fq / 1000
            op = "/ 1000 kilograms"
        elif tl == "mg":
            rv = fq * 1000
            op = "* 1000"
        elif tl == "lb":
            rv = fq / 453.592
            op = "/ 453.592"
    elif fl == "kg":
        if tl == "g":
            rv = fq * 1000
            op = "* 1000 grams"
        elif tl == "mg":
            rv = fq * 1000000
            op = "* 1000000"
        elif tl == "lb":
            rv = fq / 0.454
            op = "/ 0.454"
    elif fl == "mg":
        if tl == "g":
            rv = fq / 1000
            op = "/ 1000"
        elif tl == "kg":
            rv = fq / 1000000
            op = "/ 1000000"
        elif tl == "lb":
            rv = fq / 453592.37
            op = "/ 453592.37"
    elif fl == "lb":
        if tl == "g":
            rv = fq * 453.592
            op = "* 453.592"
        elif tl == "kg":
            rv = fq * 0.454
            op = "* 0.454"
        elif tl == "mg":
            rv = fq * 453592.37
            op = "* 453592.37"
    result()
else:
    error()
