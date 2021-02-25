def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2


operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}
from replit import clear
from art import logo

def calculation():
  print(logo)
  num_1 = float(input("What is your first number? : "))
  for key in operations:
    print(key)

  new_calc = True
  while new_calc:
    operator = input("Choose an operation : ")
    num_2 = float(input("What is your next number? : "))

    result = operations[operator](num_1,num_2)
    print(f"{num_1} {operator} {num_2} = {result}")

    choice = input(f"Type 'yes' if you want to keep calculating with {result}, type 'no' if you want to start new calculation\n")
    if choice == "yes":
      num_1 = result
    else:
      new_calc = False
      clear()
      calculation()
    
calculation()
