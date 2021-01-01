# hassio-ups
this manual is how to ups board SKU: EP-0118 in home assistant and rpi4

# 1. step
enable i2c:<br>
https://www.home-assistant.io/hassio/enable_i2c/

# 2. step
in config folder create new folder:

```# mkdir hassio-ups```<br>
```# cd hassio-ups```<br>
```# wget https://raw.githubusercontent.com/rocob/hassio-ups/main/Dockerfile```<br>
```# wget https://raw.githubusercontent.com/rocob/hassio-ups/main/ina219ups.py```<br>
```# docker build -t hassio-ups .```<br>

> this build cca 25 minutes
start docker:

```# docker run -d --privileged --restart=always -v /mnt/date/supervisor/homeassistant:/root/config:rw --name ups hassio-ups```<br>

after every 1 minute update file with name **ina219.txt** with this content:

Date: 2021-01-01<br>
Time: 17:22<br>
Voltage: 5.148 V<br>
Current: 778.561 mA<br>
Power: 4103.902 mW<br>
Shunt: 39.450 mV<br>

# 3. step
create sensors in **configuration.yaml** file:

```sensor:```<br>
  ``- platform: command_line``<br>
    ``name: UPS Voltage``<br>
```    command: "cat /config/hassio_ups/ina219.txt | grep Voltage | cut -d ' ' -f2"```<br>
```    unit_of_measurement: "V"```<br>
```    \#value_template: '{{ value | multiply(0.001) | round(1) }}'```<br>


ups board home page:<br>
https://wiki.52pi.com/index.php/UPS_(With_RTC_%26_Coulometer)_For_Raspberry_Pi_SKU:_EP-0118

