FROM python:3.9-slim

# Установим зависимости
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем весь проект
COPY . .

# Запускаем сервер
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
