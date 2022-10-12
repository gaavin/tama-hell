from asyncio import create_task, get_event_loop, sleep
from random import choice
from serial import Serial

class Button:
	def __init__(self, tama, button):
		self._button = button
		self._tama = tama

	def press(self):
		self._tama._write(f"{self._button}")

class Tama:
	def __init__(self):
		self._serial = Serial("/dev/tty.usbmodem1201", 115200)
		self.A = Button(self, "A")
		self.B = Button(self, "B")
		self.C = Button(self, "C")

	def _write(self, line):
		self._serial.write(f"{line}\r\n".encode())

async def torture(tama):
	while True:
		choice([tama.A, tama.B, tama.C]).press()

async def main():
	tama = Tama()
	await create_task(torture(tama))

if __name__ == "__main__":
	loop = get_event_loop()
	loop.run_until_complete(main())