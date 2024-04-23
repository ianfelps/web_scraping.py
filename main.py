from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

os.system('cls')
print("\n\033[33m##### Steam Wishlist Checker #####\033[m")
print("\nO perfil Steam deve estar \033[34m'Público'\033[m, juntamente com a \033[34m'Privacidade de jogos'\033[m.")
print("Developed by: \033[36m@ianfelps\033[m")
id_steam = input("\nInsira seu Steam ID: ")

driver = webdriver.Chrome()
driver.get(f"https://store.steampowered.com/wishlist/id/{id_steam}#sort=discount")
sleep(5)

jogos = driver.find_elements(By.CLASS_NAME, "wishlist_row")
titulos = []
precos = []
descontos = []

for jogo in jogos:
    em_promocao = jogo.find_elements(By.CLASS_NAME, "discount_pct")
    if em_promocao:
        titulos.append(jogo.find_element(By.CLASS_NAME, "title").text)
        precos.append(jogo.find_element(By.CLASS_NAME, "discount_final_price").text)
        descontos.append(jogo.find_element(By.CLASS_NAME, "discount_pct").text)

jogos_info = list(zip(titulos, precos, descontos))

driver.close()

os.system('cls')

if jogos_info:
    jogos_info.sort(key=lambda x: float(x[1].replace('R$', '').replace(',', '.')))
    print("\n\033[33mJogos em promoção na sua lista de desejos:\033[m\n")
    for jogo in jogos_info:
        titulo, preco, desconto = jogo
        print(f"{titulo} - \033[32m{preco}\033[m \033[31m{desconto}\033[m\n")
else:
    print("\n\033[31mNenhum jogo em promocão na sua lista de desejos. :(\033[m\n")