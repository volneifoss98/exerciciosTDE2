nome = input('digite seu nome: ')
horaTrabalhada = int(input(nome + ' quantas horas você trabalha por dia? '))
horasMes = horaTrabalhada*30
salarioHora = int(input(nome + ' quanto você ganha por hora? '))
salario = salarioHora * horasMes
print(f"{nome}, seu salario deste mês será: {salario}")
