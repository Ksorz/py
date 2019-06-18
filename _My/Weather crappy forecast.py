import pyowm
owm = pyowm.OWM(input('Enter API key:').strip())
_city = None
while True:
    if _city == None:
        _city = input('\nWhat city? ')
    if _city == 'q':
        break
    try:
        observation = owm.weather_at_place(_city)
        w = observation.get_weather()
        print('\nIn ' + _city + ', it is ' + w.get_detailed_status())
        print(str(round(w.get_temperature('celsius')['temp'])) + ' degrees celsius')
        if round(w.get_temperature('celsius')['temp']) > 20:
            print('RAZDEVAISA')
        elif round(w.get_temperature('celsius')['temp']) > 10:
            print('RAZDEVAISA NO NE SLISHKOM')
        else:
            print('ODEVAI SHUBU')
        _city = None
    except:
        _city = input('Couldn`t find, try again: ')
