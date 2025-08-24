# Crie um código onde é solicitado para o usuário inserir dois valores: a idade, e o ano atual. O sistema deve calcular quantos anos ele tem de acordo com essas informações e exibir no console.
anoNascimento = int((input("Digite seu ano de nascimento")))
anoAtual = int(input("Digite o ano atual: Ex 2025 "))
idade = anoAtual - anoNascimento
print(f"Sua idade é: {idade}")