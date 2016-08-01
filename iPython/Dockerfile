#!/usr/bin/env bash

#FROM continuumio/anaconda:latest
FROM centos:latest

# PICA Anaconda Docker Image
#
# VERSION               0.0.1
# pica/notebook 

LABEL Description="Jupyter Notebook Base Version"
MAINTAINER      Brian Brewer <brbrew01@gmail.com>

# Export env settings
ENV TERM=xterm
ENV LANG en_US.UTF-8

#Install base tools
RUN yum -y  update
RUN yum -y install yum-utils

#Group install is dependent on yum-utils
#RUN yum -y groupinstall "Development Tools"
RUN yum -y install gcc libffi-devel python-devel openssl-devel

gfortran g++
libatlas-base-dev liblapack-dev

#Key packages
RUN yum -y install wget bzip2 ca-certificates git nano openssl e2fsprogs 
#mercurial subversion 

#Clean
RUN yum -y clean all

# Install Annaconda
RUN export PATH=/opt/conda/bin:$PATH

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/archive/Anaconda2-4.0.0-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh

# Install Additional Anaconda Packages
RUN /opt/conda/bin/conda install -y gensim seaborn pymongo theano twisted paramiko pyodbc

#Clean cache
RUN /opt/conda/bin/conda clean --all -y

# Set up new user
RUN useradd --create-home --home-dir /home/pica --shell /bin/bash pica
RUN gpasswd -a pica wheel

ADD run_jupyter.sh /home/pica
RUN chmod +x /home/pica/run_jupyter.sh
RUN chown pica /home/pica/run_jupyter.sh

EXPOSE 8888
#RUN usermod -a -G sudo pica
RUN echo "pica ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER pica
RUN mkdir -p /home/pica/notebooks
ENV PATH /opt/conda/bin:$PATH
ENV HOME=/home/pica
ENV SHELL=/bin/bash
ENV USER=pica
VOLUME /home/pica/notebooks
WORKDIR /home/pica/notebooks

CMD ["/home/pica/run_jupyter.sh"]
