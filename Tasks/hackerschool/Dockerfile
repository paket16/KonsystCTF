# Используем базовый образ с apache
FROM trafex/php-nginx
# Задаём имя создателя
MAINTAINER Vlasov Aleksandr <vlasov1488@gmail.com>
#Выбираем временную зону для контенера
ENV TZ = Asia/Yekaterinburg
# Создаем рабочую директорию
WORKDIR /var/www/html/
# Копируем файлы проекта в рабочую директорию
RUN mkdir -p /var/www/html/assets
COPY index.html
COPY style.css
COPY ./assets/index.php ./assets/index.php
# Указываем порт, на котором будет работать приложение
EXPOSE 9998
# Запускаем приложение