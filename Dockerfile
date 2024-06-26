FROM python:3.12.4

### setup driver
ARG GOOGLE_CHROME_VERSION=126.0.6478.114-1
ARG CHROMEDRIVER_VERSION=126.0.6478.63

# install chrome and chromedriver
RUN apt-get update -y && \
    apt-get install -y wget gnupg wget && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | \
        gpg --dearmor -o /usr/share/keyrings/google-linux-signing-key.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux-signing-key.gpg]" \
        "http://dl.google.com/linux/chrome/deb/ stable main" \
        > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update -y && \
    apt-get install -y google-chrome-stable=$GOOGLE_CHROME_VERSION && \
    wget -O /tmp/chromedriver-linux64.zip \
        https://storage.googleapis.com/chrome-for-testing-public/$CHROMEDRIVER_VERSION/linux64/chromedriver-linux64.zip && \
    unzip /tmp/chromedriver-linux64.zip -d /tmp && \
    mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

### setup app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY /requirements.txt ./requirements.txt

RUN pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install -r requirements.txt

COPY app .
