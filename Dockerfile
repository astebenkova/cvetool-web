FROM ubuntu:focal

ADD id_rsa /root/.ssh/id_rsa

ARG CVETOOL_REPO=ssh://zuul-ci-robot@gerrit.mcp.mirantis.com:29418/mcp-ci/docker-image-scanner

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -yq python3 python3-pip git wget && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install cvetool
RUN chmod 600 /root/.ssh/id_rsa && \
    ssh-keyscan -p 29418 gerrit.mcp.mirantis.com >> /root/.ssh/known_hosts && \
    git clone --branch release_071 --depth 1 "${CVETOOL_REPO}" /scanner && \
    cd /scanner && pip3 install --no-cache-dir -r requirements.txt && python3 setup.py install && \
    mkdir /etc/cvetool && cp etc/config.cfg.sample /etc/cvetool/config.cfg && \
    sed -i 's/clair_severity = dist_severity/clair_severity = NVD_cvssv3/g' /etc/cvetool/config.cfg && \
    rm -rf /root/.ssh/id_rsa /scanner

WORKDIR /cvetool-web

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /cvetool-web

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 5000

ENTRYPOINT ["gunicorn", "-c", "gunicorn.conf.py", "manage:app"]