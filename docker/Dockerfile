FROM python:3.7

RUN pip3.7 install requests==2.21.0 && \
pip3.7 install pyTelegramBotAPI==3.6.6

RUN mkdir /bot

WORKDIR /bot

COPY qwertee_bot.py /bot/qwertee_bot.py

CMD ["python", "/bot/qwertee_bot.py"]
