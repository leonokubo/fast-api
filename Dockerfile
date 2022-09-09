FROM python:3.9

ENV APPLICATION_ROOT=/app
RUN mkdir -p $APPLICATION_ROOT
WORKDIR $APPLICATION_ROOT
COPY . $APPLICATION_ROOT

RUN make install
