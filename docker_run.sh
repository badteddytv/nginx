#!/bin/bash

set -e
set -x

sudo docker rm -f bad_teddy/nginx || true
sudo docker build -t badteddy/nginx:latest .
sudo docker run -v '/run/secrets':'/run/secrets' -it --rm --network=host --name nginx badteddy/nginx
