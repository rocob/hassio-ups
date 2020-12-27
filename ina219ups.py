# IMPORT THE LIBERARY.
from ina219 import INA219
from ina219 import DeviceRangeError
SHUNT_OHMS = 0.05

from datetime import datetime
#today = date.today()
now = datetime.now()
dt = now.strftime("%Y-%m-%d")
tm = now.strftime("%H:%M")

def read():
    """Define method to read information from coulometer."""
    ina = INA219(shunt_ohms=SHUNT_OHMS, busnum=1)
    ina.configure()
    print("Date:", dt)
    print("Time:", tm)
    print("Voltage: %.3f V" % ina.voltage())
    try:
        print("Current: %.3f mA" % ina.current())
        print("Power: %.3f mW" % ina.power())
        print("Shunt: %.3f mV" % ina.shunt_voltage())
    except DeviceRangeError as e:
        print(e)

if __name__ == "__main__":
    read()
