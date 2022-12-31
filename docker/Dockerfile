FROM selenium/standalone-chrome

USER root

# Upgrade installed packages
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Install python
RUN apt-get update && apt-get install -y python3.9 python3-pip && apt-get clean

# Install python packages
RUN pip3 install requests && \
    pip3 install pyTelegramBotAPI==3.6.6 && \
    pip3 install selenium==4.7

RUN mkdir /bot

WORKDIR /bot

COPY qwertee_bot.py /bot/qwertee_bot.py

CMD ["python3", "/bot/qwertee_bot.py"]