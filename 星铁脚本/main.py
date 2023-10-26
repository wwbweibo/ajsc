import os 
import cv2
import time


from image import check_game_status

from pc import start_game, capture_image, preset_image_loader

if __name__ == "__main__":
    actions = preset_image_loader()
    offsetx, offsety = start_game()
    print('game started')
    while True:
        edge = capture_image()
        action = check_game_status(edge, actions)
        if action is not None:
            action_name, func, x, y = action
            print('run action %s at %d, %d' % (action_name, x, y))
            func(x + offsetx, y + offsety)
        # if status is not None:
        #     t, x, y = status
        #     x = x + offsetx
        #     y = y + offsety
        #     if t == 'chat_continue':
        #         print('chat continue')
        #         click_at(x, y)
        #     if t == 'chat_select':
        #         print('chat select')
        #         click_at(x,y)
        #     if t == 'chat_begin':
        #         print('chat begin')
        #         game_chat(x, y)
        #     if t == 'chat_begintask':
        #         print('chat begintask')
        #         click_at(x, y)
        #     if t == 'phone_select':
        #         print('phone select')
        #         click_at(x + 10, y + 10)
        #     if t == 'phone_close':
        #         print('phone close')
        #         click_at(x + 80, y + 100)