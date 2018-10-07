import notification


class SpecificationCars:
	
	_instance = None

	def __new__(cls, *args, **kwargs):
		if cls._instance is None:
			# Возможно наличие только 1 экземпляра класса
			cls._instance = super().__new__(cls)
		return(cls._instance)

	_car_specifications = {
		'ferrary': {"max_speed": 340, "drag_coef": 0.324, "time_to_max": 26},
		'bugatti': {"max_speed": 407, "drag_coef": 0.39, "time_to_max": 32},
		'toyota': {"max_speed": 180, "drag_coef": 0.25, "time_to_max": 40},
		'lada': {"max_speed": 180, "drag_coef": 0.32, "time_to_max": 56},
		'sx4': {"max_speed": 180, "drag_coef": 0.33, "time_to_max": 44},
	}

	def get_spec(self, name_car):
		return(self._car_specifications[name_car])


class Car(notification.Observer):
	"""Автомобиль участвующий в гонке"""

	def __init__(self, name):
		self.name = name
		specification_car = SpecificationCars().get_spec(name)
		self._max_speed = specification_car['max_speed']
		self._drag_coef = specification_car['drag_coef']
		self._time_to_max = specification_car['time_to_max'] / 3600
		self._acceleration = self._max_speed / self._time_to_max

	def get_time(self, competitor_time, weather):
		if competitor_time == 0:
			# Исходя из формулы пути тела: S = (a*t^2)/2
			time = (2 / self._acceleration)**0.5
		else:
			speed = (competitor_time / self._time_to_max) * self._max_speed
			speed = self._max_speed if speed >= self._max_speed else speed
			speed = weather.correction_spead(speed, self._drag_coef)
			time = float(1) / speed
		return(time)

