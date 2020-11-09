from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con
import PySimpleGUI as sg


# Cookie position
class cookie:
    x = 319 
    y = 488


# Perform the click on the cookie
def clickT(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(0.0001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)


# Loop for click on the cookie
def loopClicking(clicksQnt):
    for i in range(clicksQnt):

        if(keyboard.is_pressed('q')):
            break

        clickT(cookie.x, cookie.y)




sg.theme('DarkAmber')

layout = [ [sg.Text("Welcome to the Cookie Clicker Bot!! To stop the bot just press Q")],
            [sg.Text("How much clicks do you want?"), sg.InputText()],
            [sg.Button('START'), sg.Button('CANCEL')] ]


window = sg.Window("Cookie Clicker Bot", layout)
window.KeepOnTop = True


while True:
    event, values = window.read()

    if event == 'START':
        if values[0].isnumeric():
            loopClicking(int(values[0]))
            # break

        else:
            sg.popup("Hey, you are crazy?? Please type a number", keep_on_top=True)

        

    if event == sg.WIN_CLOSED or event == 'CANCEL':
        break

    print('You entered', values[0])