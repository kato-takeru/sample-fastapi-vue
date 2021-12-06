FROM node:16.13.1-alpine

WORKDIR /app

RUN npm config set unsafe-perm true

RUN apk update && \
    npm install -g npm @vue/cli