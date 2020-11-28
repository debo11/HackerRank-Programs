import re

def ValidPostal(xs):
    txt = str (xs)
    count = sum ([xs[i] == xs[i + 2] for i in range (0, len (xs) - 2)])
    regex = "^[0-9]{6}$"
    matched = re.findall (regex, txt)
    if count <= 1 and matched:
        return True
    else:
        return False


input1 = [int (x) for x in input ("Enter Postal Code:")]
output = ValidPostal (input1)
print (output)
