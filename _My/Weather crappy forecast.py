import pyowm
owm = pyowm.OWM('362efc6c6d191d0e2e1d642f9aafd1b2')
_city = input('Wich city? ')
w = None
for i in range(5):
    try:
        observation = owm.weather_at_place(_city)
        w = observation.get_weather()
        print('\nIn ' + _city + ', it is ' + w.get_detailed_status())
        print(str(round(w.get_temperature('celsius')['temp'])) + ' degrees celsius')
        break
    except:
        _city = input('Couldn`t find, try again: ')
