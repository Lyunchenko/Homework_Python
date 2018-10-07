import car
import weather
import notification


class Competition:
	"""Гонка"""

	_instance = None

	def __new__(cls, *args, **kwargs):
		if cls._instance is None:
			# Возможно наличие только 1 экземпляра класса
			cls._instance = super().__new__(cls)
		return(cls._instance)

	def __init__(self, distance):
		self._distance = distance
		self._competitors = []
		self._weather = weather.BaseWeather()
		self._notification_manager = notification.NotificationManager()
		
	def set_weather(self, wind_speed=None, ice = None):
		if not wind_speed is None:
			try:
				if not self._weather.wind_speed is None:
					self._weather.wind_speed = wind_speed
			except Exception as e:
				self._weather = weather.Wind(self._weather)
				self._weather.wind_speed = wind_speed

		if not ice is None:
			try:
				if not self._weather.ice is None:
					self._weather.ice = ice
			except Exception as e:
				self._weather = weather.Ice(self._weather)
				self._weather.ice = ice
			
	def set_competitors(self, competitors):
		for competitor in competitors:
			if not competitor in self._competitors:
				self._competitors.append(competitor)

	def start(self):
		competitors = self._get_cars()
		result = self._get_result(self._distance, competitors)
		self._print_result(result)

	def _get_cars(self):
		competitors=[]
		for competitor in self._competitors:
			this_car = car.Car(competitor)
			competitors.append(this_car)
			self._notification_manager.subscribe(this_car)
		return(competitors)

	def _get_result(self, distance, competitors):
		result = {} if len(competitors)>0 else False
		for competitor in competitors:
			competitor_time = 0
			for step in range(distance):
				time = competitor.get_time(competitor_time, self._weather)
				competitor_time += time
			result[competitor.name] = competitor_time
		return(result)
		
	def _print_result(self, result):
		if result:
			self._notification_manager.notify(result)
		else: print('None competitors!')


obj_competition = Competition(10000)
obj_competition.set_weather(wind_speed=20)
obj_competition.set_weather(wind_speed=40, ice = True)
obj_competition.set_competitors(['ferrary'])
obj_competition.set_competitors(['bugatti', 'toyota','lada','sx4'])
obj_competition.start()
