import win32gui
import win32api
import win32con
import cv2
from PIL import ImageGrab
import pyautogui
import time
import numpy as np
from os import path

rect = None

def find_windows_with_title(title):
    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd) and title in win32gui.GetWindowText(hwnd):
            windows.append(hwnd)
        return True

    windows = []
    win32gui.EnumWindows(callback, windows)
    return windows

def start_game():
    windows = find_windows_with_title("崩坏：星穹铁道")
    if len(windows) == 0:
        win32gui.MessageBox(None, "没有找到游戏窗口")
    gamewindow = windows[0]
    # 获取窗口位置，并将窗口设置为最顶层
    win32gui.SetForegroundWindow(gamewindow)
    global rect
    rect = win32gui.GetWindowRect(gamewindow)
    time.sleep(2)
    return rect[0], rect[1]

def capture_image():
    image = ImageGrab.grab(rect)
    # 将PIL图像转换为numpy数组
    numpy_image = np.array(image)
    # 将RGB格式转换为BGR格式
    gray = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2GRAY)
    time.sleep(0.5)
    return gray

def click_at(x, y):
    pyautogui.moveTo(x, y, duration=0.2)
    mouse_click()

def mouse_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

def game_chat(x, y):
    pyautogui.keyDown('F')
    time.sleep(0.02)
    pyautogui.keyUp('F')

def preset_image_loader():
    chat_continue = cv2.imread( path.join('images', 'chat-continue.png'), cv2.IMREAD_GRAYSCALE)
    chat_select = cv2.imread(path.join('pc_images','chat-select.png'), cv2.IMREAD_GRAYSCALE)
    chat_begin = cv2.imread(path.join('pc_images','chat-begin.png'), cv2.IMREAD_GRAYSCALE)
    chat_begintask = cv2.imread(path.join('pc_images', 'chat-begintask.png'), cv2.IMREAD_GRAYSCALE)
    phone_select = cv2.imread(path.join('pc_images','phone-select.png'), cv2.IMREAD_GRAYSCALE)
    phone_close = cv2.imread(path.join('pc_images', 'phone-close.png'), cv2.IMREAD_GRAYSCALE)
    return chat_continue, chat_select, chat_begin, chat_begintask, phone_select, phone_close
