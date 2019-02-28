# DailyQwertee
[![Join Daily Qwertee on Telegram](https://patrolavia.github.io/telegram-badge/chat.png)](https://t.me/DailyQwertee)

Sends you the 3 daily tshirts from qwertee.com, scheduled with cron to be executed at 23:10 every day

In order to use the Docker setup, use the following commands:

```bash
#inside the project folder

$ docker build -t qwerteebot .

$ docker run -v <ABSOLUTE_PATH_TO_BOT_TOKEN>:/bot/token.txt qwerteebot
```

May change the Dockerfile to a light base image (probably alpine) in the future.
