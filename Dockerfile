FROM python:3.6.8-alpine3.8

WORKDIR /nginx

RUN apk add git wget openssh make g++ pcre-dev openssl-dev

# Building Nginx with Rtmp Support
RUN mkdir build &&\
    cd build &&\
    wget http://nginx.org/download/nginx-1.15.0.tar.gz &&\
    tar -xzf nginx-1.15.0.tar.gz &&\
    git clone https://github.com/arut/nginx-rtmp-module.git &&\
    cd nginx-rtmp-module &&\
    git checkout tags/v1.2.1 &&\
    cd ../nginx-1.15.0 &&\
    ./configure --add-module=../nginx-rtmp-module &&\
    make &&\
    make install &&\
    cd .. &&\
    rm -rf build
