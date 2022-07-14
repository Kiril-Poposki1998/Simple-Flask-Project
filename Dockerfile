FROM python:3.9-alpine

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python init.py

CMD ["flask","run","--host=0.0.0.0","--port=8080"]