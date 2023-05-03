import pyautogui

# def moveToImage(img, addLeft=0, addTop=0):
#     res = pyautogui.locateOnScreen(img, confidence=0.7)
#     if res:
#         resX = int(res.left)
#         resY = int(res.top)
#         if addLeft != 0 or addTop != 0:
#             pyautogui.moveTo([resX + addLeft, resY + addTop])
#         else: 
#             pyautogui.moveTo(res)
#     else:
#         print("Imagem Nao Econtrada")

# # pyautogui.sleep(3)
# moveToImage("cabecalhoExcel2.png", 0, 0)


def imgOnScreen(img, sair = True):
    res = pyautogui.locateOnScreen(img, confidence= 0.7)
    if res:
        return True
    else:
        if sair:
            print(f"Imagem '{img}' Nao Econtrada")
            quit()
        return False

def imgCaptcha():
    disponivel = True
    while disponivel:
        res = pyautogui.locateOnScreen("Pular.png")
        if res:
            pyautogui.click(res, clicks=2)
            # print("imgCaptcha Econtrado")
        else:
            disponivel = False
            return False


def passCaptcha():
    imgCaptcha()
    pyautogui.sleep(2)
    if imgOnScreen("checkBoxCaptcha.png", False):
        print("erro, espere 2min")
        return False
    else:
        return True
    

print(passCaptcha())