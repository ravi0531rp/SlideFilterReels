from threading import Thread
from queue import Queue
from datetime import datetime
import time
import functools


class Streamer:
	def __init__(self, outputQueue):
		self.outputQueue = outputQueue
		self.end = False
		self.iteration = 0
	def start(self):
		Thread(target = self.stream , args = (self.outputQueue,)).start()

	def stream(self, outQueue):
		while not self.end:
			self.iteration += 1
			try:
				outQueue.put([self.iteration , datetime.now()])
				time.sleep(2)
			except:
				print("Exception occured while streaming")
			

	def stop(self):
		self.end = True
		print("Stopped streaming..")

class StreamIngestor:
	def __init__(self, inputQueue):
		self.inputQueue = inputQueue
		self.end = False
		self.ingestIter = 0
	def start(self):
		Thread(target = self.ingest , args = (self.inputQueue,)).start()

	def ingest(self, inputQueue):
		while not self.end:
			self.ingestIter += 1
			try:
				streamIter , timeData = inputQueue.get_nowait()
				print(f" streamIter : {streamIter} , ingestIter : {self.ingestIter} , timeData : {timeData} ")
				time.sleep(1)
			except:
				# print("Problem while reading..")
				pass

	def stop(self):
		self.end = True
		print("Stopped Reading")


if __name__ == "__main__":
	commonQueue = Queue()
	streamer = Streamer(commonQueue).start()
	ingestor = StreamIngestor(commonQueue).start()

