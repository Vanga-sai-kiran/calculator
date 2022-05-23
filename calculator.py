import art
from replit import clear
print(art.logo)
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def module(num1,num2):
    return num1%num2
operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
    "%":module
}
def calculation():
    num1=float(input("what's your first number : "))
    should_continue=True
    while should_continue==True:
        for operator in operations:
            print(f"{operator} \n")
        choice=input("Pick one operator from above : ")
        num2=float(input("What is your next number : "))
        calculation_function=operations[choice]
        answer=calculation_function(num1,num2)
        print(f"{num1} {choice} {num2} ={answer}")
        next_step=input(f"Type 'yes' to continue calculating with {answer} or type 'no ' to start a new calculation :") 
        if next_step=="yes":
            num1=answer
        else:
            should_continue=False
            clear()
            calculation()
            
calculation()