import os 
import cv2
import time

adb_path = '/Users/gongsi/Library/Android/sdk/platform-tools/adb'

def check_game_status(image, chat_continue, chat_select, chat_begin, chat_begintask, phone_select, phone_close):
    # 一次查找图像是否在图像中匹配
    res = cv2.matchTemplate(image, chat_continue, cv2.TM_CCOEFF_NORMED)
    min_val, max_val , min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val > 0.8:
        x, y = max_loc
        return 'chat_continue', x, y
    res = cv2.matchTemplate(image, chat_select, cv2.TM_CCOEFF_NORMED)
    min_val, max_val , min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val > 0.8:
        x, y = max_loc
        return 'chat_select', x, y
    res = cv2.matchTemplate(image, chat_begintask, cv2.TM_CCOEFF_NORMED)
    min_val, max_val , min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val > 0.8:
        x, y = max_loc
        return 'chat_begintask', x, y
    res = cv2.matchTemplate(image, chat_begin, cv2.TM_CCOEFF_NORMED)
    min_val, max_val , min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val > 0.8:
        x, y = max_loc
        return 'chat_begin', x, y
    res = cv2.matchTemplate(image, phone_select, cv2.TM_CCOEFF_NORMED)
    min_val, max_val , min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val > 0.9:
        x, y = max_loc
        return 'phone_select', x, y
    res = cv2.matchTemplate(image, phone_close, cv2.TM_CCOEFF_NORMED)
    min_val, max_val , min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val > 0.9:
        x, y = max_loc
        return 'phone_close', x, y

def device_image_capture_and_convert():
    os.system(adb_path + ' shell screencap -p /sdcard/screen.png')
    os.system(adb_path + ' pull /sdcard/screen.png')
    # using cv2 read this image and convert to gray image
    img = cv2.imread('screen.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # do edge detection on image
    # edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    return gray
    return edges

def preset_image_loader():
    chat_continue = cv2.imread("images/chat-continue.png", cv2.IMREAD_GRAYSCALE)
    # chat_continue = cv2.Canny(chat_continue, 50, 150, apertureSize=3)
    auto_battle = cv2.imread("images/auto-battle.png", cv2.IMREAD_GRAYSCALE)
    # auto_battle = cv2.Canny(auto_battle, 50, 150, apertureSize=3)
    chat_select = cv2.imread("images/chat-select.png", cv2.IMREAD_GRAYSCALE)
    # chat_select = cv2.Canny(chat_select, 50, 150, apertureSize=3)
    chat_begin = cv2.imread("images/chat-begin.png", cv2.IMREAD_GRAYSCALE)
    chat_begintask = cv2.imread("images/chat-begintask.png", cv2.IMREAD_GRAYSCALE)
    phone_select = cv2.imread("images/phone-select.png", cv2.IMREAD_GRAYSCALE)
    phone_close = cv2.imread("images/phone-close.png", cv2.IMREAD_GRAYSCALE)
    return chat_continue, auto_battle, chat_select, chat_begin, chat_begintask, phone_select, phone_close

def start_game():
    os.system(adb_path + ' shell monkey -p com.miHoYo.hkrpg -c android.intent.category.LAUNCHER 1')
    # wait for 30 seconds
    time.sleep(30)
    # do tap on any position
    os.system(adb_path + ' shell input tap 500 500')
    # make sure game stated
    time.sleep(30)

if __name__ == "__main__":
    # start_game()
    print('game started')
    chat_continue, auto_battle, chat_select, chat_begin, chat_begintask, phone_select, phone_close = preset_image_loader()
    while True:
        edge = device_image_capture_and_convert()
        status = check_game_status(edge, chat_continue, chat_select, chat_begin, chat_begintask, phone_select, phone_close)
        if status is not None:
            t, x, y = status
            if t == 'chat_continue':
                print('chat continue')
                os.system(adb_path + ' shell input tap ' + str(x) + ' ' + str(y))
            if t == 'chat_select':
                print('chat select')
                os.system(adb_path + ' shell input tap ' + str(x) + ' ' + str(y))
            if t == 'chat_begin':
                print('chat begin')
                os.system(adb_path + ' shell input tap ' + str(x) + ' ' + str(y))
            if t == 'chat_begintask':
                print('chat begintask')
                os.system(adb_path + ' shell input tap ' + str(x) + ' ' + str(y))
            if t == 'phone_select':
                print('phone select')
                os.system(adb_path + ' shell input tap ' + str(x + 10) + ' ' + str(y + 10))
            if t == 'phone_close':
                print('phone close')
                os.system(adb_path + ' shell input tap ' + str(x + 80) + ' ' + str(y + 100))