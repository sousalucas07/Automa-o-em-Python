import pyautogui    
import time  
 
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
#pyautogui.PAUSE = 0.3 

# abrir o navegador (chrome)  
pyautogui.PAUSE = 0.3
 
pyautogui.click(x=1228, y=3)
time.sleep(2)
pyautogui.click()
time.sleep(2)
pyautogui.write("youtube")
time.sleep(1)
pyautogui.press("enter")

   