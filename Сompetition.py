

class Car:
	"""Автомобиль участвующий в гонке"""

	_car_specs = {
		'ferrary': {"max_speed": 340, "drag_coef": 0.324, "time_to_max": 26},
		'bugatti': {"max_speed": 407, "drag_coef": 0.39, "time_to_max": 32},
		'toyota': {"max_speed": 180, "drag_coef": 0.25, "time_to_max": 40},
		'lada': {"max_speed": 180, "drag_coef": 0.32, "time_to_max": 56},
		'sx4': {"max_speed": 180, "drag_coef": 0.33, "time_to_max": 44},
	}

	def __init__(self, name):
		self.name = name
		self._max_speed = self._car_specs[name]['max_speed']
		self._drag_coef = self._car_specs[name]['drag_coef']
		self._time_to_max = self._car_specs[name]['time_to_max'] / 3600
		self._acceleration = self._max_speed / self._time_to_max
		self._weather = Weather()

	def get_time(self, competitor_time):
		if competitor_time == 0:
			# Исходя из формулы пути тела: S = (a*t^2)/2
			time = (2 / self._acceleration)**0.5
		else:
			speed = (competitor_time / self._time_to_max) * self._max_speed
			speed = self._max_speed if speed >= self._max_speed else speed
			speed = self._weather.correction_spead(speed, self._drag_coef)
			time = float(1) / speed
		return(time)


class Weather:
	"""Погода во время гонки"""

	_instance = None

	def __new__(cls, wind_speed=10):
		if cls._instance is None:
			# Возможно наличие только 1 экземпляра класса
			cls._wind_speed = wind_speed
			cls._instance = super().__new__(cls)
		return(cls._instance)

	def _get_wind_speed(self):
		return self._wind_speed

	def _set_wind_speed(self, value):
		self._wind_speed = value

	wind_speed = property(_get_wind_speed, _set_wind_speed, "I'm the 'wind_speed' property.")

	def correction_spead(self, speed, drag_coef):
		wind_speed = self._get_wind_speed()
		if speed > wind_speed:
			speed -= (drag_coef * wind_speed)
		return(speed)

	def _get_wind_speed(self):
		from random import randint
		wind_speed = randint(0, self._wind_speed)
		return(wind_speed)


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
		
	def set_wind_speed(self, wind_speed):
		obj_weather = Weather()
		obj_weather.wind_speed = wind_speed

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
			competitors.append(Car(competitor))
		return(competitors)

	def _get_result(self, distance, competitors):
		result = [] if len(competitors)>0 else False
		for competitor in competitors:
			competitor_time = 0
			for step in range(distance):
				time = competitor.get_time(competitor_time)
				competitor_time += time
			result.append({'competitor_name': competitor.name,
								 'competitor_time': competitor_time})
		return(result)
		
	def _print_result(self, result):
		if result:
			for competitor in result:
				print("Car <%s> result: %f" % (competitor['competitor_name'],
										   competitor['competitor_time']))
		else: print('None competitors!')


obj_competition = Competition(10000)
obj_competition.set_wind_speed(20)
obj_competition.set_competitors(['ferrary'])
obj_competition.set_competitors(['bugatti', 'toyota','lada','sx4'])
obj_competition.start()
