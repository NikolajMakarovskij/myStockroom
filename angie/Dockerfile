# Building angie image
FROM alpine:3.21 AS building
# install angie
RUN set -x \
     && apk add --no-cache ca-certificates curl \
     && curl -o /etc/apk/keys/angie-signing.rsa https://angie.software/keys/angie-signing.rsa \
     && echo "https://download.angie.software/angie/alpine/v$(egrep -o \
          '[0-9]+\.[0-9]+' /etc/alpine-release)/main" >> /etc/apk/repositories \
     && apk add --no-cache angie angie-module-geoip2 angie-module-njs \
     && rm /etc/apk/keys/angie-signing.rsa \
     && ln -sf /dev/stdout /var/log/angie/access.log \
     && ln -sf /dev/stderr /var/log/angie/error.log

RUN rm /etc/angie/http.d/default.conf
COPY angie.conf /etc/angie/
COPY default.conf /etc/angie/http.d/default.conf

CMD ["angie", "-g", "daemon off;"]

# Build Stage
FROM node:23-bookworm-slim as build
WORKDIR /app
COPY --from=frontend . /app
RUN npm i --force
RUN npm run build

# Production Stage
FROM building AS prod
RUN mkdir /frontend
RUN mkdir /frontend/dist
COPY --from=build /app/dist /frontend/dist
