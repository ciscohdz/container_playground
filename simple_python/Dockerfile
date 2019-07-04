FROM python:3.7-alpine

RUN mkdir /src
WORKDIR /src/
VOLUME ["/src"]

COPY ./py/ /src/
COPY ./requirements.txt /src/requirements.txt

#RUN pip3 install pandas
# RUN pip3 install -r /src/requirements.txt


CMD ["python3", "/src/run.py"]