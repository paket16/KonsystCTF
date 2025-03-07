# Build:
``` 
Создаём контейнер
docker build -t selfhash .
```

# Start:
```
docker run -p 9999:9999 --name selfhash_tmp selfhash
```

# Usage:
```
nc localhost 9999

transform sometext
```
