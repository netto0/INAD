import pyautogui
import time


def clicar(itemPos):
    pyautogui.click(x=itemPos[0], y=itemPos[1])


def getCursorPos():
    pos = pyautogui.position()
    print(f"Posicao atual do cursor: x={pos.x}, y={pos.y}")


pauseTimeCaptcha = 4
pauseTime = 2
pyautogui.PAUSE = 1.5


captchaBoxPos = [-1316, 443]
consultaNotaPos = [-727, 333]
chaveCampoPos = [-622, 288]
imprimirPos = [-871, 404]
botaoSalvarPos = [-176, 122]
fecharGuiaPos = [-1087, 13]
pintarPos = [291, 115]

def macroCompleto():
    pyautogui.hotkey("alt", "tab")
    pyautogui.hotkey("ctrl", "c")
    clicar(chaveCampoPos)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "v")
    clicar(consultaNotaPos)
    pyautogui.sleep(pauseTimeCaptcha)
    clicar(captchaBoxPos)
    pyautogui.sleep(pauseTime)
    clicar(imprimirPos)
    pyautogui.sleep(pauseTime)
    clicar(botaoSalvarPos)
    pyautogui.press('enter')
    clicar(fecharGuiaPos)
    pyautogui.hotkey("alt", "tab")
    clicar(pintarPos)


macroCompleto()
# getCursorPos()
# time.sleep(15)

# pyautogui.click(x=consultaNotaPos[0], y=consultaNotaPos[1])
# pyautogui.click(x=captchaBoxPos[0], y=captchaBoxPos[1])