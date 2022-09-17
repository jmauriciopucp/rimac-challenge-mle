FROM python:3.9.14-alpine3.15

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY ./app.py /code

COPY ./model /code/model

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]