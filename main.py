# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import vk_api
import time
from loguru import logger as log
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

import data


def auth_handler():
    # При двухфакторной аутентификации вызывается эта функция.
    key = input("Enter authentication code: ")
    remember_device = True
    return key, remember_device


def send_message(vk, id_type, id, message, attachment=None):
    vk.method('messages.send',
              {id_type: id, 'message': message, 'random_id': get_random_id(), 'attachment': attachment})


vk = vk_api.VkApi(token=data.token)
vk.get_api()
longpoll = VkLongPoll(vk)
bot_status = True
student_id = 286259343  # id Светы
log.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="100 KB", compression="zip")
log.info("Bot Launched")


@log.catch()
def run():
    global bot_status
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            response = event.text.lower()
            if event.user_id == student_id and response == "+" and bot_status:
                time.sleep(3)
                send_message(vk, 'chat_id', event.chat_id, "+")
                log.info("'+' has been sent")
            if event.user_id == 273207132:  # from me
                if response == "test":
                    send_message(vk, 'user_id', event.user_id, bot_status)
                if response == "on":
                    bot_status = True
                    send_message(vk, 'user_id', event.user_id, 'Status: ON')
                if response == "off":
                    bot_status = False
                    send_message(vk, 'user_id', event.user_id, 'Status: OFF')


if __name__ == '__main__':
    run()
