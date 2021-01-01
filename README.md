# hassio-ups
this manual is how to ups board SKU: EP-0118 in home assistant and rpi4

# 1. step
in config folder create new folder:

\# mkdir hassio-ups

\# cd hassio-ups

\# wget https://raw.githubusercontent.com/rocob/hassio-ups/main/Dockerfile

\# wget https://raw.githubusercontent.com/rocob/hassio-ups/main/ina219ups.py

\# docker build -t hassio-ups .

this build cca 25 minutes

\# docker run -d --privileged --restart=always -v /mnt/date/supervisor/homeassistant:/root/config:rw --name ups hassio-ups

when every 1 minute update file name ina219.txt with this content:

Date: 2021-01-01<br>
Time: 17:22<br>
Voltage: 5.148 V<br>
Current: 778.561 mA<br>
Power: 4103.902 mW<br>
Shunt: 39.450 mV<br>

ups board home page:

https://wiki.52pi.com/index.php/UPS_(With_RTC_%26_Coulometer)_For_Raspberry_Pi_SKU:_EP-0118

enable i2c:

https://www.home-assistant.io/hassio/enable_i2c/
