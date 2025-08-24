# Verificador de Nota Mínima: Crie um código que pergunte ao usuário qual foi sua nota em um teste. Defina uma nota mínima para aprovação (por exemplo, 6). Use uma estrutura if para verificar se a nota do usuário é maior ou igual à nota mínima. Se for, exiba a mensagem "Você atingiu a nota mínima!".

nota_minima = 6

nota_aluno = int((input("Digite sua nota: ")))

if nota_aluno == nota_minima:
    print("Você atingiu a nota mínima!")
elif nota_aluno >= nota_minima:
    print(f"Parabéns você atingiui {nota_aluno}")
else:
    print(f"Infelizmente você não atingiu a nota mínima, sua nota é: {nota_aluno}")