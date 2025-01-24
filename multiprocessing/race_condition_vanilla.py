import time
from threading import Thread

#"MUTEX"


class StingySpendy:
	money = 100

	def stingy(self):
		for i in range(1000000):
			self.money += 10
		print("Stingy done")

	def spendy(self):
		for i in range(1000000):
			self.money -= 10
		print("Spendy done")


ss = StingySpendy()

ee = Thread(target=ss.stingy, args=())
ei = Thread(target=ss.spendy, args=())

ee.start()
ei.start()

ee.join()
ei.join()

print("Money in the end: ", ss.money)