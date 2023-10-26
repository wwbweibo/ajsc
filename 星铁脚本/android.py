import os
import cv2
import time
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
    item_submit = cv2.imread(path.join('pc_images', 'item-submit.png', cv2.IMREAD_GRAYSCALE))
    return [('chat_continue', chat_continue, chat_continue_action), 
            ('chat_select', chat_select, chat_select_action), 
            ('chat_begintask', chat_begintask, chat_begintask_action),
            ('chat_begin', chat_begin, chat_begin_action), 
            ('phone_select', phone_select, phone_select_action), 
            ('phone_close', phone_close, phone_close_action),
            ('item_submit', item_submit, item_submit_action)]
    # return chat_continue, chat_select, chat_begin, chat_be
    # return chat_continue, chat_select, chat_begin, chat_begintask, phone_select, phone_close, item_submit

def start_game():
    os.system(adb_path + ' shell monkey -p com.miHoYo.hkrpg -c android.intent.category.LAUNCHER 1')
    # wait for 30 seconds
    time.sleep(30)
    # do tap on any position
    os.system(adb_path + ' shell input tap 500 500')
    # make sure game stated
    time.sleep(30)
    return 0, 0

def game_chat(x, y):
    click_at(x, y)

def chat_continue_action(x, y):
    click_at(x, y )

def chat_select_action(x, y):
    click_at(x, y)

def chat_begin_action(x, y): 
    click_at(x, y)

def chat_begintask_action(x, y):
    click_at(x, y)

def phone_select_action(x,y):
    click_at(x, y)

def phone_close_action(x, y):
    click_at(x, y)

def item_submit_action(x, y):
    click_at(x, y)