import pyautogui    
import time  
import pandas as pd
 
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
#pyautogui.PAUSE = 0.3 

tabela = pd.read_excel("Chamados.xlsx")

print(tabela)


time.sleep(5)
# Loop para percorrer os códigos
for linha in tabela.index:
# abrir o navegador (chrome)   
    pyautogui.PAUSE = 0.3   

    time.sleep(2)   
    pyautogui.press("tab")
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.write(str(tabela.loc[linha, "Chamados"])) 
    time.sleep(2)  
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("down")  
    pyautogui.press("tab") 
    time.sleep(1)
    pyautogui.press("space")
    time.sleep(1)
    pyautogui.press("tab") 
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1) 
    pyautogui.press("down") 
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("down") 
    time.sleep(1)
    pyautogui.press("tab") 
    time.sleep(1)
    pyautogui.press("enter") 
    time.sleep(1)
    pyautogui.click(x=449, y=423)

#pyautogui.click()
#time.sleep(2)
#pyautogui.write("youtube")
#time.sleep(2)
#pyautogui.press("enter")
#time.sleep(5)
#pyautogui.click(x=644, y=108)
#time.sleep(2)
#pyautogui.write("como tornar o código python executavel")#"https://forms.office.com/Pages/ResponsePage.aspx?id=QWJvW1ea5EuOUB36cueaVysGd9RlOD5BpEqjI8yC_0JUN0dWNURMVlBCTElZMk0yVTM1MlVVRk1IWi4u"
#pyautogui.press("enter")
#time.sleep(2)
#pyautogui.click(x=671, y=725)


   