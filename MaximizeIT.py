input1 = int(input("Enter no. of Elements: "))
input2 = int(input("Enter your Modulus Value: "))

no_of_elements = range(0,input1)
list1 =[]
for x in no_of_elements:
    arr = list (map (int, input ().split (' ')))
    maximum_values = max(arr) ** 2
    list1.append(maximum_values)
    addi_res = sum(list1)
    print(addi_res)
    result = addi_res % input2
    print(result)













