# PESQUISA SATISFAÇÃO - TUDOWEB #
excelente = 0
ruim = 0
for i in range (1, 51):
    print(f"\n--- entrevistado {i} ---")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    print("\nOpções de atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    opiniao = int(input("Digite sua opinião (1, 2 ou 3): "))
if opiniao == 1:
        excelente += 1
        resposta = "EXCELENTE"
elif opiniao == 2:
        resposta = "BOM"
elif opiniao == 3:
        ruim += 1
        resposta = "RUIM"
else:
        resposta = "OPÇÃO INVÁLIDA"
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Opinião: {resposta}")
print("\n==============================")
print("RESULTADO FINAL DA PESQUISA")
print("==============================")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")
