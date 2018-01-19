FROM debian:buster

RUN apt update
RUN apt install wget 
RUN dpkg --add-architecture i386
RUN wget -nc https://dl.winehq.org/wine-builds/Release.key
RUN apt-key add Release.key
RUN apt update
RUN apt install --install-recommends winehq-stable

RUN wget https://www.python.org/ftp/python/2.7.14/python-2.7.14.msi
RUN msiexec /a python-2.7.14.msi /qb TARGETDIR=C:\Python27

RUN mkdir -p /usr/app
WORKDIR /usr/app
COPY . /usr/app

CMD [ "wine ~/.wine/drive_c/Python27/python.exe eve_downloader.py && mv destiny_wrapper.py bin && cd bin && wine ~/.wine/drive_c/Python27/python.exe destiny_wrapper.py" ]
