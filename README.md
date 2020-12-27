# hassio-ups

\# mkdir hassio-ups

\# cd hassio-ups

\# wget https://raw.githubusercontent.com/rocob/hassio-ups/main/Dockerfile

\# wget https://raw.githubusercontent.com/rocob/hassio-ups/main/ina219ups.py

\# docker build -t hassio-ups .

\# docker run -d --privileged --restart=always -v /mnt/date/supervisor/homeassistant:/root/config:rw --name ups hassio-ups
