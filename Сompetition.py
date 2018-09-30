

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

	def get_speed(self, competitor_time, wind_speed):
		if competitor_time == 0:
			speed = 1
		else:
			speed = (competitor_time / self._time_to_max) * self._max_speed
			speed = self._max_speed if speed >= self._max_speed else speed
			if speed > wind_speed:
				speed -= (self._drag_coef * wind_speed)
		return(speed)


class WEATHER:
	"""Погода во время гонки"""

	def __init__(self, wind_speed = 20):
		self._wind_speed = wind_speed

	def get_wind_speed(self):
		from random import randint
		wind_speed = randint(0, self._wind_speed)
		return(wind_speed)


class COMPETITION:
	"""Гонка - cинглетный класс"""

	_instance = None
	def __new__(self, distance):
		if self._instance == None:
			# Возможно наличие только 1 экземпляра класса
			self._instance = self
			competitors = self._get_competitors(self)
			weather = WEATHER()
			self._start(self, distance, competitors, weather)
		self._print_result(self)
		return(self._instance)

	def _get_competitors(self):
		competitors = [CAR('ferrary')]
		competitors.append(CAR('bugatti'))
		competitors.append(CAR('toyota'))
		competitors.append(CAR('lada'))
		competitors.append(CAR('sx4'))
		return(competitors)

	def _start(self, distance, competitors, weather):
		self._result = []
		for competitor in competitors:
			competitor_time = 0
			for step in range(distance):
				wind_speed = weather.get_wind_speed()
				speed = competitor.get_speed(competitor_time, wind_speed)
				competitor_time += float(1) / speed
			self._result.append({'competitor_name': competitor.name, 'competitor_time': competitor_time})

	def _print_result(self):
		for competitor in self._result:
			print("Car <%s> result: %f" % (competitor['competitor_name'], competitor['competitor_time']))


start = COMPETITION(10000)

