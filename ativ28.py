# Crie um programa que receba uma lista com o nome de 5 produtos e outra lista com as quantidades em estoque de cada um desses produtos. O programa deve exibir os produtos que estão com o estoque zerado.
 
l_produtos = []
l_estoque = []

for prod in range(5):
    produto = input("Digite o nome do produto: ")
    estoque = int(input("Digite o estoque correspondente: "))
    l_produtos.append(produto)
    l_estoque.append(estoque)

estoques_zerados = []
for est in range(5):
    if l_estoque[est] == 0:
        estoques_zerados.append(l_produtos[est])

if estoques_zerados:
    print(f"Produtos com estoque zerado: {', '.join(estoques_zerados)}")
else:
    print("Não tem nenhum produto com estoque zearado")   