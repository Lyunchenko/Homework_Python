

class Observer:

	name = None

	def update(self, message):
		print('{0}: мой результат - {1}'.format(self.name, round(message[self.name],1)))


class NotificationManager:

	def __init__(self): 
		self.__subscribers = set()
    
	def subscribe(self, subscriber):
		self.__subscribers.add(subscriber)
        
	def unsubcribe(self, subscriber):
		self.__subscribers.remove(subscriber)
        
	def notify(self, message):
		for subscriber in self.__subscribers:
			subscriber.update(message)