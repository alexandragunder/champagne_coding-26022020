FROM python:slim

WORKDIR /usr/src/app

COPY prod/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./prod .
COPY ./models models

CMD [ "python", "./predict.py" ]
