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
            # print("imgCaptcha Econtrado")
        else:
            disponivel = False
            return False

def passCaptcha():
    imgCaptcha()
    pyautogui.sleep(4)
    if imgOnScreen("checkBoxCaptcha.png", False):
        print("erro, espere 2min")
        return False
    else:
        return True


def imgOnScreen(img, sair = True):
    res = pyautogui.locateOnScreen(img, confidence= 0.7)
    if res:
        return True
    else:
        if sair:
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
captchaError = "captchaError.png"
imageCaptchaFound = 0

def macroCompleto():
    esperar = False
    if imgOnScreen(cabecalhoExcel):
        moveToImage(cabecalhoExcel)
        pyautogui.hotkey("ctrl", "c")

    if imgOnScreen(chaveCampoPos):
        moveToImage(chaveCampoPos, 30, 30)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "v")
    
    if imgOnScreen(consultaNotaPos):
        moveToImage(consultaNotaPos)
        pyautogui.sleep(pauseTime)

    if imgOnScreen(captchaBoxPos):
        moveToImage(captchaBoxPos, -40)
        pyautogui.sleep(pauseTime)
    
    if passCaptcha():
        esperar = False
    else:
        esperar = True
    pyautogui.sleep(pauseTime)

    if imgOnScreen(captchaError,sair=False):
        print(f"Erro no Captcha")
        moveToImage(captchaError)
        pyautogui.hotkey("ctrl", "w")
        return

    if imgOnScreen(imprimirPos):
        moveToImage(imprimirPos)
        pyautogui.sleep(pauseTime)

    
    if imgOnScreen("ErrorMsg.png", sair=False):
        pyautogui.hotkey("ctrl", "w")
        moveToImage(cabecalhoExcel)
    else:
        if imgOnScreen(botaoSalvarPos):
            moveToImage(botaoSalvarPos)
            pyautogui.sleep(1)
            pyautogui.press('enter')
            pyautogui.sleep(pauseTime)
            pyautogui.hotkey("ctrl", "w")

        if imgOnScreen(cabecalhoExcel):
            moveToImage(cabecalhoExcel)
            moveToImage(pintarPos)
            pyautogui.press('down')

    if esperar:
        print("Esperando 2 Minutos")
        pyautogui.sleep(120)

def executarEmLoop(quantidade):
    for d in range(quantidade):
        print(f"Execucao: {d+1}")
        macroCompleto()

executarEmLoop(50)