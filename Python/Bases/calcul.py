print("Donne moi une operation")
operation = input()
print("Donne moi deux nombres")
a = int(input())
b = int(input())
if operation == "addition":
    reponse = a + b
elif operation == "Addition":
    reponse = a + b
elif operation == "+":
    reponse = a + b
elif operation == "soustraction":
    reponse = a - b
elif operation == "Soustraction":
    reponse = a - b
elif operation == "-":
    reponse = a - b

print(reponse)
