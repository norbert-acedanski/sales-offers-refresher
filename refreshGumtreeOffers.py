import pyautogui
import time

numberOfOffersToRefresh = 10
switchToGumTreeTab = False


def switch_window():
    if switchToGumTreeTab:
        pyautogui.hotkey("alt", "tab")


def open_close_dev_tools():
    pyautogui.hotkey("ctrl", "shift", "j")


def clear_dev_tools_console():
    pyautogui.hotkey("ctrl", "l")


def open_elements_tab():
    open_close_dev_tools()
    time.sleep(2)
    clear_dev_tools_console()
    time.sleep(1)
    pyautogui.keyDown("shift")
    press_tab_n_times(13)
    pyautogui.keyUp("shift")
    pyautogui.press("enter")
    pyautogui.press("down")
    pyautogui.press("enter")
    time.sleep(1)


def find_first_instance():
    pyautogui.hotkey("ctrl", "f")
    pyautogui.write("row clearfix")


def open_all_offers_to_refresh():
    for _ in range(numberOfOffersToRefresh):
        pyautogui.keyDown("shift")
        press_tab_n_times(3)
        pyautogui.keyUp("shift")
        pyautogui.press("enter")
        time.sleep(0.1)
        go_to_previous_tab()
        press_tab_n_times(3)
        pyautogui.press("enter")
    time.sleep(2)


def refresh_all_opened_offers():
    open_close_dev_tools()
    for _ in range(numberOfOffersToRefresh):
        go_to_next_tab()
        pyautogui.keyDown("shift")
        press_tab_n_times(10)
        pyautogui.keyUp("shift")
        pyautogui.press("enter")
    time.sleep(4)


def close_all_refreshed_offers_tabs():
    pyautogui.keyDown("ctrl")
    for _ in range(numberOfOffersToRefresh):
        pyautogui.press("w")
    pyautogui.keyUp("ctrl")


def go_to_next_tab():
    pyautogui.hotkey("ctrl", "tab")


def go_to_previous_tab():
    pyautogui.hotkey("ctrl", "shift", "tab")


def press_tab_n_times(n: int):
    for _ in range(n):
        pyautogui.press("tab")


def close_tab():
    pyautogui.hotkey('ctrl', 'w')


def refresh_tab():
    pyautogui.press("f5")


if __name__ == '__main__':
    for i in range(3, 0, -1):
        print(i)
        time.sleep(0.5)
    print("Start!")
    time.sleep(1)
    switch_window()
    open_elements_tab()
    find_first_instance()
    open_all_offers_to_refresh()
    refresh_all_opened_offers()
    close_all_refreshed_offers_tabs()
    pyautogui.press("home")
    refresh_tab()
