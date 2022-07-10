from json import loads, dumps
import requests
from textwrap import dedent
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import settings
from django.http import HttpResponse, HttpRequest


@csrf_exempt
def catch_incoming_message(request: HttpRequest) -> HttpResponse:
    message_data = loads(request.body)
    bot_token = settings.TG_BOT_TOKEN
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

    message = message_data.get('message').get('text')

    if message == '/start':
        user_id = message_data['message']['from']['id']
        keyboard = dumps(
            {'keyboard':
                [
                    [
                        {'text': 'Отправить контакт',
                         'request_contact': True},
                    ]
                ],
                'one_time_keyboard': True
             }
        )

        text = "Привет, а дашь номер?"
        data = {
            'text': text,
            'chat_id': user_id,
            'reply_markup': keyboard
        }
        response = requests.post(url, data=data)
        response.raise_for_status()

        return HttpResponse({'Status': 200})

    else:
        contact_phone = message_data['message'].get('contact').get('phone_number')
        user_id = message_data['message']['chat']['id']
        if contact_phone:
            username = message_data['message']['from']['username']

            nova_post = requests.post(
                url='https://s1-nova.ru/app/private_test_python/',
                headers={'Content-Type': 'application/json; charset=UTF-8'},
                json={'phone': contact_phone,
                      'login': username}
            )
            nova_post.raise_for_status()

            text = dedent(
                f'''
                Ура-ура! Я сохранил твой номер на сервере тайной организации :)
                Теперь меня можно удалить, перезапустить и сохранить номер еще раз.
                ''')
            data = {
                'text': text,
                'chat_id': user_id,
            }
            response = requests.post(url, data=data)
            response.raise_for_status()

            return HttpResponse({'Status': 200})

        else:
            text = dedent(
                f'''
                Больше я ничего не умею, но ты можешь удалить меня, 
                начать общение заново, и я снова сохраню твой номер.
                Здорово, правда? :)
                ''')
            data = {
                'text': text,
                'chat_id': user_id,
            }
            response = requests.post(url, data=data)
            response.raise_for_status()

            return HttpResponse({'Status': 200})