FROM python:3.11-slim

RUN mkdir /code

WORKDIR /code

COPY . .

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


EXPOSE 8000

WORKDIR /code/app

CMD ["python","-m","uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
