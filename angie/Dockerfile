FROM debian:12

LABEL org.opencontainers.image.authors="Release Engineering Team <devops@tech.wbsrv.ru>"

ARG DEBIAN_FRONTEND=noninteractive

RUN set -x \
     && apt-get update \
     && apt-get install --no-install-recommends --no-install-suggests -y \
          ca-certificates curl \
     && curl -o /etc/apt/trusted.gpg.d/angie-signing.gpg \
          https://angie.software/keys/angie-signing.gpg \
     && echo "deb https://download.angie.software/angie/$(. /etc/os-release && echo "$ID/$VERSION_ID $VERSION_CODENAME") main" \
          > /etc/apt/sources.list.d/angie.list \
     && apt-get update \
     && apt-get install --no-install-recommends --no-install-suggests -y \
          angie angie-module-geoip2 angie-module-njs \
     && rm -Rf /var/lib/apt/lists \
          /etc/apt/sources.list.d/angie.list \
          /etc/apt/trusted.gpg.d/angie-signing.gpg \
     && ln -sf /dev/stdout /var/log/angie/access.log \
     && ln -sf /dev/stderr /var/log/angie/error.log

RUN rm /etc/angie/http.d/default.conf
COPY angie.conf /etc/angie/
COPY default.conf /etc/angie/http.d/default.conf

CMD ["angie", "-g", "daemon off;"]
