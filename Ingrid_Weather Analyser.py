
import random
daily_temperatures = [random.randint(0, 35) for _ in range(30)]

hottest_temperature = max(daily_temperatures)
coldest_temperature = min(daily_temperatures)
average_temperature = sum(daily_temperatures) / 30

print ("Question 1")
print('---------------------------------')
print("The hottest Temperature is: \n {0}°C".format(hottest_temperature))
print('---------------------------------')
print("The coldest Temperature is: \n {0}°C".format(coldest_temperature))
print('---------------------------------')
print("The average Temperature is :\n {0:.0f}°C".format(average_temperature))
print('---------------------------------')

daily_rainfall = [random.randint(0, 10) for _ in range(30)]

worst_day = 1  
worst_temperature = daily_temperatures[0]
worst_rainfall = daily_rainfall[0]

for day, (temperature, rainfall) in enumerate(zip(daily_temperatures, daily_rainfall), start=1):
    if rainfall > worst_rainfall or (rainfall == worst_rainfall and temperature < worst_temperature):
        worst_day = day
        worst_temperature = temperature
        worst_rainfall = rainfall


print ("Question 2")
print("The worst weather conditions occurred on day {}".format(worst_day))
print("Temperature: {}°C".format(worst_temperature))
print("Rainfall: {}mm".format(worst_rainfall))
print('---------------------------------')

weekly_temperatures = [[random.randint(-1, 10) for _ in range(7)] for _ in range(4)]

freezing_weeks = []
for week, temperatures in enumerate(weekly_temperatures, start=1):
    if any(temp < 0 for temp in temperatures):
        freezing_weeks.append(week)

print ("Question 3")
print("Weeks with freezing temperatures:", freezing_weeks)

def hottest_coldest_average(temperatures):

    hottest_temperature = max(temperatures)
    coldest_temperature = min(temperatures)
    average_temperature = sum(temperatures) / 30

    return hottest_temperature, coldest_temperature, average_temperature


hca = hottest_coldest_average(daily_temperatures)


def worst_day_record(temperatures, rainfall):
    if not temperatures or not rainfall or len(temperatures) != len(rainfall):
        return None 

    worst_day = 1
    worst_temperature = temperatures[0]
    worst_rainfall = rainfall[0]

    for day, (temperature, rain) in enumerate(zip(temperatures, rainfall), start=1):
        if (rain > worst_rainfall) or (rain == worst_rainfall and temperature < worst_temperature):
            worst_day = day
            worst_temperature = temperature
            worst_rainfall = rain

    return worst_day, worst_temperature, worst_rainfall

worst_day, worst_temperature, worst_rainfall = worst_day_record(daily_temperatures, daily_rainfall)

print('-------------------------------------')
print ("Question 4")
print("the hottest temperature is: {}°C".format(hca[0]))
print("the coldest temperature is: {}°C".format(hca[1]))
print("the average temperature is: {:.0f}°C".format(hca[2]))
print('-------------------------------------')
print("Worst day:", worst_day)
print("Worst day conditions - Temperature: {}°C, Rainfall: {}mm".format(worst_temperature, worst_rainfall))
print('-------------------------------------')

international_weather = {
    'Ireland': {
        'temperatures': [random.randint(0, 35) for _ in range(30)],
        'rainfall': [random.randint(0, 10) for _ in range(30)]
    },
    'Spain': {
        'temperatures': [random.randint(0, 35) for _ in range(30)],
        'rainfall': [random.randint(0, 10) for _ in range(30)]
    },
    'France': {
        'temperatures': [random.randint(0, 35) for _ in range(30)],
        'rainfall': [random.randint(0, 10) for _ in range(30)]
    }
}

print ("Question 5")
for country, data in international_weather.items():    
 print("{}:".format(country))
 print("Temperature: {}".format(data['temperatures']))
 print("rainfall: {}".format(data['rainfall']))
 print()
print('-------------------------------------')


import random

countries = ['ireland', 'spain', 'france']
print ("Question 6")
while True:
    print('Enter one of the following countries or "Done" to exit:')
    print("{0}, {1}, {2}".format('ireland', 'spain', 'france'))
    country = input().lower()

    if country == 'done':
        break

    if country not in countries:
        print('Error. Please enter a valid country name.')
    else:
        daily_temperatures = [random.randint(0, 35) for _ in range(30)]
        daily_rainfall = [random.randint(0, 10) for _ in range(30)]

        hca = hottest_coldest_average(daily_temperatures)
        worst_day_data = worst_day_record(daily_temperatures, daily_rainfall)

        
        print("Hottest Temperature: {0}°C".format(hca[0]))
        print("Coldest Temperature: {0}°C".format(hca[1]))
        print("Average Temperature: {0:.0f}°C".format(hca[2]))
        print("Worst Day: Day {0}, Temperature {1}°C, Rainfall {2}mm".format(worst_day_data[0], worst_day_data[1], worst_day_data[2]))
        
