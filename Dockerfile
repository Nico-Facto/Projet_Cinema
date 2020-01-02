FROM python:3.7-buster

RUN pip install argparse mysql-connector-python beautifulsoup4 pandas requests datetime schedule matplotlib bigml scikit-learn seaborn numpy pyqt5 
RUN apt-get clean && apt-get update && apt-get install -y locales
RUN apt-get install -y python-pyqt5

# RUN apt install -qq --assume-yes mesa-utils libgl1-mesa-glx libxcursor1 libxrandr2 libxxf86vm1 x11-xserver-utils xfonts-base xserver-common dos2unix libxkbcommon-x11-dev libdbus-glib-1-dev libdbus-1-dev libqt5x11extras5 libx11-xcb1 libqt5designer5 qttools5-dev-tools 
# if issue with QT see this link for debug : https://stackoverflow.com/questions/24095968/docker-for-gui-based-environments

RUN echo 'fr_FR.UTF-8 UTF-8' >> /etc/locale.gen 
RUN echo 'en_US ISO-8859-1 ' >> /etc/locale.gen 
RUN echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen 
RUN echo 'fr_FR ISO-8859-1' >> /etc/locale.gen
RUN locale-gen

COPY . /usr/src/themoviepredictor

WORKDIR /usr/src/themoviepredictor/
CMD python scrap.py movies scrap yes 