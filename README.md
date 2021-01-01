# hassio-ups
this manual is how to ups board SKU: EP-0118 in home assistant and rpi4

# 1. step
enable i2c:<br>
https://www.home-assistant.io/hassio/enable_i2c/

# 2. step
in config folder download files and build docker image:

```
# git clone https://github.com/rocob/hassio-ups.git
# cd hassio-ups
# docker build -t hassio-ups .
```

> this build cca 25 minutes

start docker container:

```# docker run -d --privileged --restart=always -v /mnt/date/supervisor/homeassistant:/root/config:rw --name ups hassio-ups```<br>

after docker container every 1 minute update file with name **ina219.txt** with this content:

Date: 2021-01-01<br>
Time: 17:22<br>
Voltage: 5.148 V<br>
Current: 778.561 mA<br>
Power: 4103.902 mW<br>
Shunt: 39.450 mV<br>

# 3. step
create sensors in **configuration.yaml** file:

```
sensor:
  - platform: command_line
    name: UPS Voltage
    command: "cat /config/hassio_ups/ina219.txt | grep Voltage | cut -d ' ' -f2"
    unit_of_measurement: "V"
    #value_template: '{{ value | multiply(0.001) | round(1) }}'
```

ups board home page:<br>
https://wiki.52pi.com/index.php/UPS_(With_RTC_%26_Coulometer)_For_Raspberry_Pi_SKU:_EP-0118

