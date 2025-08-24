# Verificação de Diferença: Crie um código que peça para o usuário inserir dois nomes. Depois verifique se os dois nomes são diferentes. Se forem, exiba "Os nomes digitados são diferentes.".

name1 = input("Digite um nome: ")
name2 = input("Digite novamente um nome: ")

if name1 != name2:
    print(f"Os nomes digitados são diferentes.")
else:
    print(f"Os nomes digitados são iguais.")
