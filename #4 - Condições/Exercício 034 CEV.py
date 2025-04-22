salary = float(input("Digite o salário do funcionário: "))
if salary <= 1250:
    new_salary = salary * 1.15
else:
    new_salary = salary * 1.10
print(f"O novo salário do funcionário é: R$ {new_salary:.2f}")