from gpiozero import LED
from time import sleep
import serial, sys, json
from mux import Mux4, Mux16

class Sensor_Controller:
    def __init__(self) -> None:
        with open('config.json', 'r') as config:
            config = json.load(config)
            self.mux_top = Mux16(LED(config['mux_top_A']), LED(config['mux_top_B']))
            self.mux_bottom = Mux4(LED(config['mux_bottom_A']), LED(config['mux_bottom_B']))
            self.port = config['port']
            self.baud = config['baud']

    def run(self):
        try:
            ser = serial.Serial(self.port, self.baud)
        except serial.SerialException as e:
            sys.stderr.write(f'Could not open {self.port}: {e}\n')
            sys.exit(1)

        print('Start listening')
        while True:
            try:
                ch = int(ser.readline().decode().strip())
            except ValueError as e:
                ser.flush()
                sys.stderr.write(f'Invalid input: {e}\n')
                ser.write(f'Invalid input: {e}\n'.encode())
                continue
        
            print(f'receive {ch}')
            if ch in range(16):
                try:
                    self.mux_top.select(ch)
                    self.mux_bottom.select(ch % 4)
                    sleep(0.5)
                    print('ack: ok')
                    ser.write(f'ok {ch}'.encode())
                except Exception as e:
                    sys.stderr.write(f'Select ch{ch} failed: {e}\n')
                    ser.write(f'Select ch{ch} failed: {e}\n'.encode())
            else:
                sys.stderr.write('ch number out of range\n')
                ser.write(b'ch number out of range\n')


if __name__ == '__main__':
    sensor_controller = Sensor_Controller()
    sensor_controller.run()