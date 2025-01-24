import time
from threading import Thread, Lock

#"MUTEX"


class StingySpendy:
	money = 100

	lock = Lock()

	def stingy(self):
		for i in range(1000000):
			self.lock.acquire()
			self.money += 10
			self.lock.release()
		print("Stingy done")

	def spendy(self):
		for i in range(1000000):
			self.lock.acquire()
			self.money -= 10
			self.lock.release()
		print("Spendy done")


ss = StingySpendy()

ee = Thread(target=ss.stingy, args=())
ei = Thread(target=ss.spendy, args=())

ee.start()
ei.start()

ee.join()
ei.join()

print("Money in the end: ", ss.money)