#!/usr/bin/python3

#Vai imprimir a saudação.
print("Welcome to the tip calculator")
#Variável para guardar a conta.
bill = float(input("What the total bill? $"))
#Variável da Gorjeta.
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
#Variável para saber o número de pessoas.
people = int(input("How many people to split the bill? "))
#Cálculo da Gorjeta.
tip_as_percent = tip / 100
#Total da Gorjeta...
total_tip_amount = bill * tip_as_percent
#Total da Conta.
total_bill = bill + total_tip_amount
#Conta por pessoa.
bill_per_person = total_bill / people
#Quantidade final
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print (f"Each person should pay: ${final_amount}")
