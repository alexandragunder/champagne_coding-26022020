FROM python:slim

WORKDIR /app
COPY prod/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./prod prod
COPY ./models models

#COPY . .

EXPOSE 8080
CMD [ "python", "./prod/predict.py" ]
