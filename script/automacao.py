import pyautogui

def clicar(itemPos):
    pyautogui.click(x=itemPos[0], y=itemPos[1])

def getCursorPos():
    pos = pyautogui.position()
    print(f"Posicao atual do cursor: x={pos.x}, y={pos.y}")

def imgCaptcha():
    disponivel = True

    while disponivel:
        res = pyautogui.locateOnScreen("Pular.png")
        if res:
            pyautogui.click(res, clicks=2)
            print("imgCaptcha Econtrado")
        else:
            # print("imgCaptcha Nao Econtrado")
            disponivel = False
            return False
        
def imgOnScreen(img):
    res = pyautogui.locateOnScreen(img, confidence= 0.7)
    if res:
        # print(f"Imagem '{img}' Econtrada")
        return True
    else:
        print(f"Imagem '{img}' Nao Econtrada")
        quit()
        return False
    
def moveToImage(img, addLeft=0, addTop=0):
    res = pyautogui.locateOnScreen(img, confidence = 0.7) 
    resX = int(res.left)
    resY = int(res.top)
    if addLeft != 0 or addTop != 0:
        pyautogui.moveTo([resX + addLeft, resY + addTop])
    else: 
        pyautogui.moveTo(res)
    pyautogui.click()

contadorCaptcha = 0
contadorExecucoes = 0
pauseTime = 3
pyautogui.PAUSE = .5
continuar = True

cabecalhoExcel = "cabecalhoExcel.png" 
chaveCampoPos = "digiteAChave.png" 
consultaNotaPos = "consultaNota.png" 
captchaBoxPos = "checkBoxCaptcha.png" 
imprimirPos = "imprimir.png" 
botaoSalvarPos = "botaoSalvar.png" 
pintarPos = "pintar.png" 

def macroCompleto():
    
    if imgOnScreen(cabecalhoExcel):
        moveToImage(cabecalhoExcel)
        pyautogui.hotkey("ctrl", "c")
    else:
        continuar = False
        return

    if imgOnScreen(chaveCampoPos):
        moveToImage(chaveCampoPos, 30, 30)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "v")
    else:
        continuar = False
        return
    
    if imgOnScreen(consultaNotaPos):
        moveToImage(consultaNotaPos)
        pyautogui.sleep(pauseTime)
    else:
        continuar = False
        return

    if imgOnScreen(captchaBoxPos):
        moveToImage(captchaBoxPos, -40)
        pyautogui.sleep(pauseTime)
    else:
        continuar = False
        return
    
    imgCaptcha()
    pyautogui.sleep(pauseTime)

    if imgOnScreen(imprimirPos):
        moveToImage(imprimirPos)
        pyautogui.sleep(pauseTime)
    else:
        continuar = False
        return

    if imgOnScreen(botaoSalvarPos):
        moveToImage(botaoSalvarPos)
        pyautogui.press('enter')
        pyautogui.sleep(pauseTime)
        pyautogui.hotkey("ctrl", "w")
    else:
        continuar = False
        return

    if imgOnScreen(cabecalhoExcel):
        moveToImage(cabecalhoExcel)
        moveToImage(pintarPos)
        pyautogui.press('down')
    else:
        continuar = False
        return


def executarEmLoop(quantidade):
    for d in range(quantidade):
        print(f"Execucao: {d+1}")
        macroCompleto()
    print(f"Finalizado! {contadorCaptcha} captchas de imagem enfrentados.")

executarEmLoop(100)