FROM python:3.8

WORKDIR /fastapi-app/
ADD requirements.txt .

RUN pip install -r /fastapi-app/requirements.txt
#RUN apt-get update
#RUN apt-get -f install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libnss3 lsb-release xdg-utils
#RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
#RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

COPY . /fastapi-app/

EXPOSE 8000

CMD ["python", "app/main.py"]


