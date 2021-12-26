import pyautogui
import time

numberOfOffersToRefresh = 10
switchToGumTreeTab = True

def switchWindow():
    if switchToGumTreeTab:
        pyautogui.hotkey("alt", "tab")

def openCloseDevTools():
    pyautogui.hotkey("ctrl", "shift", "j")

def clearDevToolsConsole():
    pyautogui.hotkey("ctrl", "l")

def openElementsTab():
    openCloseDevTools()
    time.sleep(2)
    clearDevToolsConsole()
    time.sleep(1)
    pyautogui.keyDown("shift")
    pressTabNTimes(13)
    pyautogui.keyUp("shift")
    pyautogui.press("enter")
    pyautogui.press("down")
    pyautogui.press("enter")
    time.sleep(1)

def findFirstInstance():
    pyautogui.hotkey("ctrl", "f")
    pyautogui.write("row clearfix")

def openAllOffersToRefresh():
    for i in range(numberOfOffersToRefresh):
        pyautogui.keyDown("shift")
        pressTabNTimes(3)
        pyautogui.keyUp("shift")
        pyautogui.press("enter")
        goToPreviousTab()
        pressTabNTimes(3)
        pyautogui.press("enter")
    time.sleep(2)

def refreshAllOpenedOffers():
    openCloseDevTools()
    for i in range(numberOfOffersToRefresh):
        goToNextTab()
        pyautogui.keyDown("shift")
        pressTabNTimes(10)
        pyautogui.keyUp("shift")
        pyautogui.press("enter")
    time.sleep(4)

def closeAllRefreshedOffersTabs():
    pyautogui.keyDown("ctrl")
    pyautogui.press("w", presses=numberOfOffersToRefresh)
    pyautogui.keyUp("ctrl")

def goToNextTab():
    pyautogui.hotkey("ctrl", "tab")

def goToPreviousTab():
    pyautogui.hotkey("ctrl", "shift", "tab")

def pressTabNTimes(N):
    pyautogui.press("tab", presses=N)

def closeTab():
    pyautogui.hotkey('ctrl', 'w')

def refreshTab():
    pyautogui.press("f5")

if __name__ == '__main__':
    for i in range(3, 0, -1):
        print(i)
        time.sleep(0.5)
    print("Start!")
    time.sleep(1)
    switchWindow()
    openElementsTab()
    findFirstInstance()
    openAllOffersToRefresh()
    refreshAllOpenedOffers()
    closeAllRefreshedOffersTabs()
    pyautogui.press("home")
    refreshTab()