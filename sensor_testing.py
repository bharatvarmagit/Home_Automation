from gpiozero import DistanceSensor

from gpiozero import LED

from time import sleep



sensor = DistanceSensor(echo=8, trigger=25)

#led = LED(18)

people = 4



while True:

	sensor_value0 = sensor.distance*100

	sensor_value1 = sensor.distance*100

	sleep(1)

	sensor_value2 = sensor.distance*100

	v = sensor_value1 - sensor_value2

#	if people > 0:

#		led.on()

#	if people == 0:

#		led.off

	if people < 0:

		print("???")





	if abs(v) > 3 and abs(v) < 20:

		if v > 0:

			people = people +1

		if v < 0:

			people = people -1

	else:

		people = people



	print(sensor_value1)

	print(sensor_value2)

	print(v)

	print(people)

	sleep(1)
