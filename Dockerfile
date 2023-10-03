# Використовуємо базовий образ Python
FROM python:3.9

# Встановлюємо необхідні залежності для "Персонального помічника"
RUN pip install personal-assistant

# Вказуємо команду, яка виконується при старті контейнера
CMD ["personal-assistant"]
