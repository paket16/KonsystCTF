# Используем базовый образ с Python3
FROM python:3
# Задаём имя создателя
MAINTAINER Konstantin Omelchuk <psgreckoj@gmail.com>
#Выбираем временную зону для контенера
ENV TZ = Asia/Yekaterinburg
# Создаем рабочую директорию
WORKDIR /app
# Копируем файл проекта в рабочую директорию
COPY main.py ./
# Указываем порт, на котором будет работать приложение
EXPOSE 9999
# Запускаем приложение
CMD ["python3", "main.py"]
