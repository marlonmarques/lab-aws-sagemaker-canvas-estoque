import random
import csv
from sys import flags
from datetime import datetime

"""
Script para faciliar na criação de dataset para treinar ML, para executar no windows python gera_dataset.py no linux python3 gera_dataset.py
"""


# Solicitar informações do usuário
num_records = int(input("Digite a quantidade de registros a serem gerados: "))  # Número de registros a serem gerados
mes = int(input("Digite o número do mês desejado: "))  # Mês dos registros
ano = int(input("Digite o ano desejado: "))  # Ano dos registros
num_prod = int(input("Digite a quantidade de variação de produtos: "))  # Quantidade de clientes
mes_ano = f"{mes:02d}-{ano:04d}"  # Data no formato MM-AAAA


# Dados para o dataset
dic_precos = {
  # Dicionário contendo produtos e seus preços
  1: 21.70,
  2: 15.50,
  3: 25.50,
  4: 50.00,
  5: 80.21,
  6: 90.50,
  7: 41.00,
  8: 89.30,
  9: 12.50,
  10: 50.90,
  11: 31.50,
  12: 28.50,
  13: 150.90,
  14: 140.20,
  15: 130.25
  # ... (Adicione outros produtos aqui)
}


dataset = []
for _ in range(num_records):
  id_produto = random.randint(1, num_prod)
  dia = random.randint(1, 30)  # Dia da venda
  data = datetime(year=ano, month=mes, day=dia).strftime("%Y/%m/%d")  # Data da venda formatada
  produto = random.choice(list(dic_precos.keys()))  # Escolhe um produto aleatoriamente
  preco = dic_precos[produto]  # Preço do produto escolhido
  quantidade = random.randint(1, 1000)  # Quantidade do produto vendida
  flags = random.randint(0, 1) #rando flags
  dataset.append([id_produto, data, preco, flags, quantidade])


# criar arquivo csv
filename = f"estoque_{mes_ano}.csv"
with open(filename, "w", newline="") as csvfile:
  csvwriter = csv.writer(csvfile)
  csvwriter.writerow(["ID_PRODUTO", "DATA_EVENTO", "PRECO", "FLAG_PROMOCAO", "QUANTIDADE_ESTOQUE"])
  csvwriter.writerows(dataset)


print(f"Arquivo ficticiosos gerado {filename}")

