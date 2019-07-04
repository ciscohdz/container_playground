FROM python:3

RUN mkdir /src/
COPY ./py /src/

RUN pip3 install flask

CMD flask run --host=0.0.0.0
