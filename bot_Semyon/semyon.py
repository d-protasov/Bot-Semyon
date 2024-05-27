import threading
import requests

TOKEN = 'YOUR-TOKEN'


def send_message(chat_id, text):
    print(f"Отправка сообщения: {text}")
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=data)
    return response.json()


def read_messages():
    offset = None
    while True:
        url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
        params = {'offset': offset, 'timeout': 30}
        response = requests.get(url, params=params)
        data = response.json()

        if 'result' in data:
            messages = data['result']

            for message in messages:
                update_id = message['update_id']
                offset = update_id + 1
                chat_id = message['message']['chat']['id']
                text = message['message']['text']

                print(f'Received message: {text}')


def send_message_console():
    chat_id = 'YOUR CHAT ID'
    text = input("Введите текст сообщения: ")

    send_message(chat_id, text)


if __name__ == '__main__':
    while True:
        choice = input(
            "Выберите действие:\n1. Прочитать сообщения из Telegram\n2. Отправить сообщение через консоль\n")

        if choice == '1':
            thread = threading.Thread(target=read_messages)
            thread.start()
        elif choice == '2':
            send_message_console()
        else:
            print("Неверный выбор. Попробуйте снова.")
