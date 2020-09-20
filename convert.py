import enum
import math
from operator import index
import gpxpy
#* Get track
def getTrack(name):
    n = "C:\\Users\\Michaël Peeters\\Documents\\GitHub\\gpx-data-conversion\\Fiets" + name
    gpx = gpxpy.parse(open(n))
    return gpx
name = "\\School_rit_" + "3" + ".gpx"
gpx = getTrack(name)

#* Round number
def round_half_up(num, decimals = 0):
    multiplier = 10 ** decimals
    return math.floor(num * multiplier + 0.5) / multiplier

track = gpx.tracks[0]
segment = track.segments[0]

#* Get Speeds from gpx file
speedsList = []
maxSpeed = 0
timeSinceStart = 0
print("Number of recorded points: " + str(len(segment.points)))
print("SPEEDS OF POINTS")
for index, point in enumerate(segment.points):
    #* Get speed per point (in Km/h)
    currentSpeed = segment.get_speed(index) * 3.6
    speedsList.append(currentSpeed)
    print(round_half_up(currentSpeed, 2))

    #* Get maxSpeed of list
    if currentSpeed > maxSpeed:
        maxSpeed = currentSpeed

print("TIME OF POINTS")
for index, point in enumerate(segment.points):
    if index - 1 >= 0:
        timeSinceStart += point.time_difference(segment.points[index - 1])
        print(timeSinceStart)
    else:
        timeSinceStart += point.time_difference(segment.points[index + 1])
        print(timeSinceStart)

#* Get Duration of activity
#prevTime = segment.points[index - 1]
timeSinceStart = segment.points[len(segment.points) - 1].time_difference(segment.points[0])
#print("Duration of activity:", timeSinceStart / 60, "min")

#* Calculate average speed
speedSum = 0
for i, v in enumerate(speedsList):
    speedSum += speedsList[i]
averageSpeed = speedSum / len(speedsList)   #* Sum of items / Amount of items
print("AverageSpeed:", averageSpeed, "Km/h")
#print("MaxSpeed:", maxSpeed, "Km/h")

#from pandas import DataFrame
#columns = ['Longitude', 'Latitude', 'Altitude', 'Time', 'Speed']
#df = DataFrame(data, columns=columns)
#df.head()
#print(df.to_string())