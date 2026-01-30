# Desafio – Calculadora Simples:
# Crie uma calculadora simples no terminal que permita ao usuário escolher uma operação (soma, subtração, multiplicação ou divisão) e, em seguida, insira dois números para realizar a operação escolhida. Depois de calcular o resultado, verifique e exiba:
#   - Se o resultado é positivo ou negativo.
#   - Se o resultado é ímpar ou par.

number1 = None
while number1 is None:
    try:
        number1 = int(input("Enter a number: "))
    except ValueError:
        print("Not a number")

number2 = None
while number2 is None:
    try:
        number2 = int(input("Enter a second number: "))
    except ValueError:
        print("Not a number")

opperator = input("Enter a operator: ")
valid_operators = ["+", "-", "*", "/"]
while opperator not in valid_operators:
    print("Not a valid operator")
    opperator = input("Enter a operator: ")

result = None
match opperator:
    case '+':
        result = number1 + number2
    case '-':
        result = number1 - number2
    case '*':
        result = number1 * number2
    case '/':
        if number2 == 0:
            print("Cannot divide by zero")
            result = 0
        else:
            result = number1 / number2
    case _:
        print("Not a valid operator")

print(f"Result: {result}")


