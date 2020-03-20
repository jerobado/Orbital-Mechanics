# learning how to use skyfield

from skyfield.api import Topos, load

stations_url = 'https://celestrak.com/NORAD/elements/stations.txt'
satellites = load.tle(stations_url)
ISS = satellites['ISS (ZARYA)']
print(ISS)
