# Бот для сохранения номера телефона (Django)

Бот в телеграм: @ivve_g_bot

## Установка
Вам понадобится установленный Python 3.8+ и git.

Склонируйте репозиторий:
```bash
git clone git@github.com:IlyaG96/tg-bot-catcher.git
```

Создайте в этой папке виртуальное окружение:
```bash
cd tg-bot-catcher
python3 -m venv env
```

Активируйте виртуальное окружение и установите зависимости:
```bash
source env/bin/activate
pip install -r requirements.txt
```

## Настройка перед использованием

### Переменные окружения

Перед использованием вам необходимо заполнить .env.example файл или иным образом передать переменные среды:
- `TELEGRAM_TOKEN` - токен бота Telegram. Можно получить у [@BotFather](https://t.me/BotFather).
- `DEBUG`= настройка Django для включения отладочного режима. Принимает значения `TRUE` или `FALSE`. [Документация Django](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-DEBUG).
- `SECRET_KEY`= обязательная секретная настройка Django. Это соль для генерации хэшей. Значение может быть любым, важно лишь, чтобы оно никому не было известно. [Документация Django](https://docs.djangoproject.com/en/3.2/ref/settings/#secret-key).
- `ALLOWED_HOSTS`= настройка Django со списком разрешённых адресов. Если запрос прилетит на другой адрес, то сайт ответит ошибкой 400. Можно перечислить несколько адресов через запятую, например: `127.0.0.1,192.168.0.1,site.test`. [Документация Django](https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts).
- `NOVA_PRIVATE_URL`= секретный адрес организации, хранящей телефонные номера (зочем?).



## Использование

- Разверните приложение на одном из своих серверов, используя [эту](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04-ru) инструкцию.
- Доменное имя можно купить [здесь](https://www.reg.ru/).
- Получите бесплатный SSL-сертификат, следуя [инструкциям](https://certbot.eff.org/).
- активируйте вебхук, без него бот работать не собирается. Сделать это можно прямо в адресной строке браузера:
`https://api.telegram.org/botBOT_TOKEN/setWebhook?url=https://mydomain.ru:443/tg-webhook/`
- Телеграм сообщит, что вебхук установлен. После этого можно пользоваться ботом.
