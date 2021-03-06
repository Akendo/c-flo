FROM node:6

# Export the Websocket port for Flowhub connection
EXPOSE 3569

# Reduce npm install verbosity, overflows Travis CI log view
ENV NPM_CONFIG_LOGLEVEL warn

RUN mkdir -p /var/c-flo
WORKDIR /var/c-flo

COPY . /var/c-flo

# Install msgflo-python
RUN apt-get update && apt-get install -y \
  python \
  python-dev \
  python-pip
RUN pip install -r requirements.pip

# Install MsgFlo and dependencies
RUN npm install

# Map the volumes
VOLUME /var/c-flo/graphs /var/c-flo/components /var/c-flo/spec

CMD npm start
