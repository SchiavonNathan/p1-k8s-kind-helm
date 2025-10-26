FROM python:3.9-slim

WORKDIR /app

RUN pip install Flask

COPY app.py .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
