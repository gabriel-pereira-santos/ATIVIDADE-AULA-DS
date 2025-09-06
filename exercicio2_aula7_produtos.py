import Aula7_modulos

# crie um arquivo separado com as funções para resolver para uma das solicitações:
# 1. Calcule a média.
# 2. Calcule a mediana.
# 3. Calcule a moda.
# 4. Calcule a variância.
# 5. Calcule o desvio padrão.
# 6. Calcule a amplitude.

produtos = {
    "Arroz 5kg": 22.90,
    "Feijão 1kg": 7.50,
    "Macarrão 500g": 4.20,
    "Açúcar 1kg": 3.80,
    "Sal 1kg": 2.50,
    "Café 500g": 12.90,
    "Leite 1L": 4.70,
    "Óleo de soja 900ml": 6.30,
    "Farinha de trigo 1kg": 5.10,
    "Margarina 500g": 6.80,
    "Detergente 500ml": 2.40,
    "Sabão em pó 1kg": 9.90,
    "Papel higiênico (4un)": 7.20,
    "Shampoo 350ml": 12.50,
    "Condicionador 350ml": 13.00,
    "Desodorante aerosol": 9.40,
    "Escova de dentes": 3.80,
    "Creme dental 90g": 4.60,
    "Frango congelado 1kg": 11.90,
    "Carne bovina 1kg": 34.50,
    "Linguiça 1kg": 17.90,
    "Ovos (dúzia)": 9.20,
    "Manteiga 200g": 8.50,
    "Refrigerante 2L": 7.30,
    "Água mineral 1,5L": 2.90,
    "Biscoito recheado 130g": 2.50,
    "Pão de forma 500g": 7.60,
    "Molho de tomate 340g": 3.20,
    "Queijo mussarela 1kg": 29.90,
    "Iogurte 170g": 2.80
}

preços = []

for preco in produtos.values():
    preços.append(preco)

Aula7_modulos.dados(preços)

