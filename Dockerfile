FROM python:slim

WORKDIR /app

COPY prod/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
#COPY ./prod .
#COPY ./models models
COPY . .

CMD [ "python", "./prod/predict.py" ]
