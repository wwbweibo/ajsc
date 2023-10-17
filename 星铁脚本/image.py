import cv2
from os import path

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


def preset_image_loader():
    chat_continue = cv2.imread( path.join('images', 'chat-continue.png'), cv2.IMREAD_GRAYSCALE)
    chat_select = cv2.imread(path.join('images','chat-select.png'), cv2.IMREAD_GRAYSCALE)
    chat_begin = cv2.imread(path.join('images','chat-begin.png'), cv2.IMREAD_GRAYSCALE)
    chat_begintask = cv2.imread(path.join('images', 'chat-begintask.png'), cv2.IMREAD_GRAYSCALE)
    phone_select = cv2.imread(path.join('images','phone-select.png'), cv2.IMREAD_GRAYSCALE)
    phone_close = cv2.imread(path.join('images', 'phone-close.png'), cv2.IMREAD_GRAYSCALE)
    return chat_continue, chat_select, chat_begin, chat_begintask, phone_select, phone_close
