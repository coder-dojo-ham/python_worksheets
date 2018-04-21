from geopy.distance import vincenty
import requests
import time


DOJO_LOCATION = (51.403149, -0.303703)


def get_iss_data():
    iss_data = requests.get('http://api.open-notify.org/iss-now.json').json()

    iss_latitude = iss_data['iss_position']['latitude']
    iss_longitude = iss_data['iss_position']['longitude']

    timestamp = iss_data['timestamp']

    return vincenty(DOJO_LOCATION, (iss_latitude, iss_longitude)), timestamp


# Get the ISS location at two time points.
distance1, time1 = get_iss_data()
time.sleep(5)
distance2, time2 = get_iss_data()

print('The ISS is currently {} KM away'.format(distance1.kilometers))

# Figure out the ISS speed
total_time_moving = time2 - time1

distance_change = distance2.kilometers - distance1.kilometers

speed_per_second = distance_change / total_time_moving

speed_per_hour = speed_per_second * 60 * 60

print('The ISS is travelling at a speed of {} km/s or {} km/h'.format(speed_per_second, speed_per_hour))
