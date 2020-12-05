import vk_api
import time
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id


def auth_handler():
    # При двухфакторной аутентификации вызывается эта функция.
    key = input("Enter authentication code: ")
    remember_device = True
    return key, remember_device


def send_message(vk, id_type, id, message=None, attachment=None):
    vk.method('messages.send', {id_type: id, 'message': message, 'random_id': get_random_id(), 'attachment': attachment})


log, pas = "Ввести номер телефона сюда", "Ввести пароль сюда"
vk = vk_api.VkApi(login=log, password=pas, auth_handler=auth_handler, app_id=2685278)
vk.auth(token_only=True)
longpoll = VkLongPoll(vk)
student_id = 286259343  # id Светы
print("Bot Launched")

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            response = event.text.lower()
            if event.user_id == student_id and response == "+":
                time.sleep(4)
                send_message(vk, 'chat_id', event.chat_id, message="+")
                print("+")
            if event.user_id == 273207132 and response == "test":
                send_message(vk, 'user_id', event.user_id, message="Bot Launched")
                print("test")
