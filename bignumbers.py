input1=int(input("Type in your first number"))
input2=int(input("Type in the second number"))

if input1+input2>100:
    print("This is a big number!")
elif input1 + input2 <100 and input1 + input2 >10:
    print("This is a mediocre number.")
elif input1 + input2 <10 and input1 + input2 >5:
    print("This is a small number...")
else:
    print("This is a very small number")

'''
in one statement print("This is a big number!") else print("This is a mediocre number.") 
if input1+input2>100 nd input1 + input2 >10 else print("This is a small number...") if nput1 + input2 <10 and input1 + input2 >5
else print("This is a very small number"
'''