FROM ubuntu:18.04
MAINTAINER Oscar Valerio Montes. <oscar.valerio@gorillalogic.com>

ADD . /automation
WORKDIR /automation

##########################################################################################################################################
# AUTOMATION EXECUTION
##########################################################################################################################################
#VARIABLES
ENV CHROME_DRIVER_VERSION 76.0.3809.12
ENV GECKODRIVER_VERSION 0.24.0
ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null
ENV CHROME_DRIVER_TARBALL https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip


RUN \
    echo -e "\n\n\n\n==> Install docker container other tools ..."      && \
    apt-get update -y                                                   && \
    apt-get install -y software-properties-common                       && \
    apt-get install -y --no-install-recommends                             \
        wget            \
        zip             \
        iputils-ping    \
        vim             \
        gnupg           \
        unzip


RUN \
    echo -e "\n\n\n\n==> Install Google-Chrome..."                                                  && \
    wget --no-verbose https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb     && \
    dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install                             && \
    rm -f google-chrome-stable_current_amd64.deb


RUN \
    echo -e "\n\n\n\n==> Install Firefox..."                && \
    add-apt-repository ppa:mozillateam/firefox-next -y      && \
    apt-get install firefox -y


RUN \
    echo -e "\n\n\n\n==> Install Python and PIP..."                             && \
    apt-get upgrade -y                                                          && \
    apt-get install -y                                                             \
        python3                                                                    \
        python3-pip


RUN \
    echo -e "\n\n\n\n==> Install Display..."                                    && \
    apt-get install -yqq --no-install-recommends xvfb


RUN \
    echo -e "\n\n\n\n==> Install Chromedriver..."                               && \
    wget  $CHROME_DRIVER_TARBALL                                                && \
    unzip chromedriver_linux64.zip                                              && \
    mv chromedriver /usr/bin/chromedriver                                       && \
    chmod +x /usr/bin/chromedriver                                              && \
    rm -f chromedriver_linux64.zip


RUN \
    echo -e "\n\n\n\n==> Install Geckodriver..."                               \
    && apt-get update -y                                                       \
    && wget --no-verbose -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz \
    && rm -rf /opt/geckodriver \
    && tar -C /opt -zxf /tmp/geckodriver.tar.gz \
    && rm /tmp/geckodriver.tar.gz \
    && mv /opt/geckodriver /opt/geckodriver-$GECKODRIVER_VERSION \
    && chmod 755 /opt/geckodriver-$GECKODRIVER_VERSION \
    && ln -fs /opt/geckodriver-$GECKODRIVER_VERSION /usr/bin/geckodriver \
    && ln -fs /opt/geckodriver-$GECKODRIVER_VERSION /usr/bin/wires


RUN \
    echo "\n\n\n\n==> Install requirements.txt libraries..."                    && \
    pip3 install -r requirements.txt


RUN \
    echo -e "\n\n\n\n==> Clean up..."                                           && \
    rm -rf /var/lib/apt/lists/*

ENV PATH /usr/lib/chromium/:$PATH
