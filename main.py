from gpiozero import LED
from time import sleep
import serial, sys, json
from mux import Mux4, Mux16

class Sensor_Controller:
    def __init__(self) -> None:
        with open('config.json', 'r') as config:
            config = json.load(config)
            self.mux4_1 = Mux4(LED(config['mux1_A']), LED(config['mux1_B']))
            self.mux4_2 = Mux4(LED(config['mux2_A']), LED(config['mux2_B']))
            self.mux4_3 = Mux4(LED(config['mux3_A']), LED(config['mux3_B']))
            self.mux4_4 = Mux4(LED(config['mux4_A']), LED(config['mux4_B']))
            self.mux16 = Mux16(
                LED(config['mux0_A']), LED(config['mux0_B']),
                ch = [self.mux4_1, self.mux4_2, self.mux4_3, self.mux4_4]
                )
            self.port = config['port']
            self.baud = config['baud']

    def run(self):
        try:
            ser = serial.Serial(self.port, self.baud)
        except serial.SerialException as e:
            sys.stderr.write(f'Could not open {self.port}: {e}\n')
            sys.exit(1)

        while True:
            ch = int(ser.readline().decode().strip())
            if ch in range(16):
                try:
                    self.mux16.select(ch)
                    sleep(0.5)
                    ser.write(f'ok {ch}'.encode())
                except Exception as e:
                    sys.stderr.write(f'Select ch{ch} failed: {e}')
                    ser.write(f'Select ch{ch} failed: {e}'.encode())
            else:
                sys.stderr.write('ch number out of range')
                ser.write(b'ch number out of range')


if __name__ == '__main__':
    sensor_controller = Sensor_Controller()
    sensor_controller.run()