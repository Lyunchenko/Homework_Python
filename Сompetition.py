

class CAR:
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
		self._time_to_max = self._car_specs[name]['time_to_max']/3600
		self._acceleration = self._max_speed / self._time_to_max # ускорение = (v- v0)/t
		self._weather = WEATHER()

	def get_time(self, competitor_time):
		if competitor_time == 0:
			time = (2/self._acceleration)**0.5 # исходя из формулы пути тела: S = (a*t^2)/2
		else:
			speed = (competitor_time / self._time_to_max) * self._max_speed
			speed = self._max_speed if speed >= self._max_speed else speed
			speed = self._weather.correction_spead(speed, self._drag_coef)
			time = float(1) / speed
		return(time)


class WEATHER:
	"""Погода во время гонки"""

	_instance = None
	def __new__(cls, wind_speed = 10):
		if cls._instance == None: # возможно наличие только 1 экземпляра класса
			cls._wind_speed = wind_speed
			cls._instance = super().__new__(cls)
		return(cls._instance)

	def correction_spead(self, speed, drag_coef):
		wind_speed = self._get_wind_speed()
		if speed > wind_speed:
			speed -= (drag_coef * wind_speed)
		return(speed)

	def _get_wind_speed(self):
		from random import randint
		wind_speed = randint(0, self._wind_speed)
		return(wind_speed)


class COMPETITION:
	"""Гонка"""

	_instance = None
	def __new__(cls, distance):
		if cls._instance == None: # возможно наличие только 1 экземпляра класса
			WEATHER(20)
			competitors = cls._get_competitors(cls)
			cls._start(cls, distance, competitors)
			cls._instance = super().__new__(cls)
		return(cls._instance)

	def __init__(self, distance):
		self._print_result()

	def _get_competitors(self):
		competitors = [CAR('ferrary')]
		competitors.append(CAR('bugatti'))
		competitors.append(CAR('toyota'))
		competitors.append(CAR('lada'))
		competitors.append(CAR('sx4'))
		return(competitors)

	def _start(self, distance, competitors):
		self._result = []
		for competitor in competitors:
			competitor_time = 0
			for step in range(distance):
				time = competitor.get_time(competitor_time)
				competitor_time += time
			self._result.append({'competitor_name': competitor.name, 'competitor_time': competitor_time})

	def _print_result(self):
		for competitor in self._result:
			print("Car <%s> result: %f" % (competitor['competitor_name'], competitor['competitor_time']))


start = COMPETITION(10000)
