FROM ubuntu:focal AS builder

ADD id_rsa /root/.ssh/id_rsa

ARG CVETOOL_REPO=ssh://zuul-ci-robot@gerrit.mcp.mirantis.com:29418/mcp-ci/docker-image-scanner

ENV DEBIAN_FRONTEND=noninteractive

# Clone cvetool repository
RUN apt-get update && \
    apt-get install --no-install-recommends -y ssh-client git && \
    chmod 600 /root/.ssh/id_rsa && \
    ssh-keyscan -p 29418 gerrit.mcp.mirantis.com >> /root/.ssh/known_hosts && \
    git clone --branch release_071 --depth 1 "${CVETOOL_REPO}" /tmp/scanner && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


FROM ubuntu:focal

COPY --from=builder /tmp/scanner /scanner

# Install cvetool
RUN apt-get update && \
    apt-get install --no-install-recommends -y python3-pip git && \
    cd /scanner && pip3 install --no-cache-dir -r requirements.txt && python3 setup.py install && \
    mkdir /etc/cvetool && cp etc/config.cfg.sample /etc/cvetool/config.cfg && \
    sed -i 's/clair_severity = dist_severity/clair_severity = custom_format/g' /etc/cvetool/config.cfg && \
    rm -rf /scanner && rm -rf /var/lib/apt/lists/*

WORKDIR /cvetool-web

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /cvetool-web

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 5000

ENTRYPOINT ["gunicorn", "-c", "gunicorn.conf.py", "manage:app"]

