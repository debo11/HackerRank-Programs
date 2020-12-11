def PowerfulDigitSum(input1):
    if input1 in range (5, 201):
        input1 = input1 - 1
        square_value = str (pow (input1, input1))
        total = 0
        for i in square_value:
            total = total + int (i)
        return total
    else:
        return ""


input1 = int (input ())
output =  PowerfulDigitSum(input1)
print(output)



