# Write the inputs in the next three lines. Labels must be in plural form.
#Accepted labels atm: Weight: grams,kilograms,tonnes
from_quantity = 1050
from_label = "grams"
to_label = "tonnes"

fq = from_quantity
fl = from_label
tl = to_label
rv = 0

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
