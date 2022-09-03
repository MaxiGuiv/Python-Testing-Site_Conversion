print("Only accepts grams, kilograms, and tonnes atm.")
fq = input("Type the number")
fl = input("Type the label of this")
tl = input("What label to convert this to?")

def result():
    print(f"{fq}{op}")
    print(f"{rv} {tl}")
def error():
    print("Labels are either misspelled, not in plural form, or currently not in the program.")

if fl == "grams":
    if tl == "kilograms":
        rv = fq / 1000
        op = "/1,000"
        result()
    elif tl == "tonnes":
        rv = fq / 1000000
        op = "/1,000,000"
        result()
    else:
        error()

elif fl == "kilograms":
    if tl == "grams":
        rv = fq * 1000
        op = "*1,000"
        result()
    elif tl == "tonnes":
        rv = fq / 1000
        op = "/1,000"
        result()
    else:
        error()

elif fl == "tonnes":
    if tl == "grams":
        rv = fq * 1000000
        op = "*1,000,000"
        result()
    elif tl == "kilograms":
        rv = fq * 1000
        op = "*1,000"
        result()
    else:
        error()
