# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/tabela
    #pip install pyautogui
import pyautogui
import time

    #pyautogui.write -> escrever um texto
	#pyautogui.click -> clicar com o mouse
	#pyautogui.press -> pressiona uma tecla
    #pyautogui.hotkey -> aperta um atalho de teclado (ctrl + c)

pyautogui.PAUSE = 0.5 #da uma pausa de meio segundo para não executar tudo muito rápido

    #abrir navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

    #entrar no link

# Passo 2: Fazer login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3) #quero dar uma pausa de 3 segundos

pyautogui.click(x=498, y=413)
pyautogui.write("python1@gmail.com")
    #passar para o próximo campo
pyautogui.press("tab")
pyautogui.write("minha senha 1")
    #clicar no botão de login
pyautogui.click(x=695, y=570) #procurar a posição do mouse para clicar em login
time.sleep(3)

#Passo 3: Importar a base de dados
 #pip install pandas
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)

#Passo 4: Cadastrar um produto
#para cada linha da  minha tabela
for linha in tabela.index:
        #é necessário dar um "tab" para que tudo fique dentro do for e funcione

        #codigo
        pyautogui.click(x=557, y=302)
        codigo = tabela.loc[linha,"codigo"]
        pyautogui.write(str(codigo))
        pyautogui.press("tab")

        #marca
        marca = tabela.loc[linha,"marca"]
        pyautogui.write(str(marca))
        pyautogui.press("tab")

        #tipo
        tipo = tabela.loc[linha,"tipo"]
        pyautogui.write(str(tipo))
        pyautogui.press("tab")

        #categoria
        categoria = tabela.loc[linha,"categoria"]
        pyautogui.write(str(categoria))
        pyautogui.press("tab")

        #preço unitario
        preco_unitario = tabela.loc[linha,"preco_unitario"]
        pyautogui.write(str(preco_unitario))
        pyautogui.press("tab")

        #custo
        custo = tabela.loc[linha,"custo"]
        pyautogui.write(str(custo))
        pyautogui.press("tab")

        #obs
        obs = tabela.loc[linha,"obs"]
        if not pd.isna(obs):
            pyautogui.write(str(obs))
        pyautogui.press("tab")
        pyautogui.press("enter")
        pyautogui.scroll(5000)

    #Passo 5: Repetir o processo de cadastro até acabar os produtos

