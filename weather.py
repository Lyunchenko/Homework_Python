
from abc import ABC, abstractmethod


class CreatureWeather(ABC):

	@abstractmethod
	def correction_spead(self, speed, drag_coef):
		return(speed)


class BaseWeather(CreatureWeather):

	def correction_spead(self, speed, drag_coef):
		#print('Без корректировки скорости!')
		return(speed)


class AbstractDecoratorWeather(CreatureWeather):

	def __init__(self, base_weather):
		self.base_weather = base_weather
 
	def correction_spead(self, speed, drag_coef):
		return(self.base_weather.correction_spead(speed, drag_coef))


class Wind(AbstractDecoratorWeather):

	def _set_wind_speed(self, wind_speed):
		self._wind_speed = wind_speed

	def _get_wind_speed(self):
		from random import randint
		wind_speed = randint(0, self._wind_speed)
		return(wind_speed)

	wind_speed = property(_get_wind_speed, _set_wind_speed)
	
	def correction_spead(self, speed, drag_coef):
		speed = self.base_weather.correction_spead(speed, drag_coef)
		#print("Корректировка скорости (макс скорость ветра = {0})".format(self._wind_speed))
		rnd_wind_speed = self.wind_speed
		if speed > rnd_wind_speed:
			speed -= (drag_coef * rnd_wind_speed)
		return(speed)


class Ice(AbstractDecoratorWeather):

	ice = False
	
	def correction_spead(self, speed, drag_coef):
		speed = self.base_weather.correction_spead(speed, drag_coef)
		if self.ice:
			#print('корректировка на гололед!')
			speed = speed*0.9
		return(speed)