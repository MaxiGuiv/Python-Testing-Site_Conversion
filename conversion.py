# Write the inputs in the next three lines. Labels must be in plural form.
# Currently supports kilograms and grams
from_quantity =
from_label =
to_label =

fq = from_quantity
fl = from_label
tl = to_label
rv = 0

if fl == "grams" and tl == "kilograms":
    rv = fq / 1000
    print(f"{rv} {tl}")
elif fl == "kilograms" and tl == "grams":
    rv = fq * 1000
    print(f"{rv} {tl}")
else:
    print("Label is either misspelled, not in plural form, or currently not supported by the program.")
