import os
import cv2
from os import path

adb_path = '/Users/gongsi/Library/Android/sdk/platform-tools/adb'

def capture_image():
    os.system(adb_path + ' shell screencap -p /sdcard/screen.png')
    os.system(adb_path + ' pull /sdcard/screen.png')
    # using cv2 read this image and convert to gray image
    img = cv2.imread('screen.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # do edge detection on image
    # edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    return gray

def click_at(x, y):
    os.system(adb_path + ' shell input tap ' + str(x) + ' ' + str(y))

def preset_image_loader():
    chat_continue = cv2.imread( path.join('images', 'chat-continue.png'), cv2.IMREAD_GRAYSCALE)
    chat_select = cv2.imread(path.join('images','chat-select.png'), cv2.IMREAD_GRAYSCALE)
    chat_begin = cv2.imread(path.join('images','chat-begin.png'), cv2.IMREAD_GRAYSCALE)
    chat_begintask = cv2.imread(path.join('images', 'chat-begintask.png'), cv2.IMREAD_GRAYSCALE)
    phone_select = cv2.imread(path.join('images','phone-select.png'), cv2.IMREAD_GRAYSCALE)
    phone_close = cv2.imread(path.join('images', 'phone-close.png'), cv2.IMREAD_GRAYSCALE)
    return chat_continue, chat_select, chat_begin, chat_begintask, phone_select, phone_close
