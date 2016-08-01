#!/usr/bin/env bash
# docker build -t pica/python .

FROM continuumio/anaconda:latest

# Anaconda Docker Image
#
# VERSION               0.0.1

LABEL Description="Python Base Version"
MAINTAINER      Brian Brewer <brbrew01@gmail.com.com>

# Export env settings
ENV LANG en_US.UTF-8

# Install Additional Anaconda Packages
RUN /opt/conda/bin/pip install --upgrade pip tweepy twython pika elasticsearch neo4j-driver marathon --no-cache-dir

#Clean cache
RUN /opt/conda/bin/conda clean --all -y


RUN mkdir -p /run/src
RUN chmod +x /run/src

COPY test.py /run/src/test.py

RUN /opt/conda/bin/python /run/src/test.py

EXPOSE 8888

ENV PATH /opt/conda/bin:$PATH
ENV HOME=/run/src
ENV SHELL=/bin/bash
VOLUME /run/src
WORKDIR /run/src

ENTRYPOINT ["/opt/conda/bin/python"]
CMD ["test.py"]
