import enum
from operator import index
import gpxpy
gpx = gpxpy.parse(open('/home/noah/Downloads/Namiddagrit.gpx'))

track = gpx.tracks[0]
segment = track.segments[0]

#* Get Speeds from gpx file
speedsList = []
maxSpeed = 0
timeSinceStart = 0
for index, point in enumerate(segment.points):
    #* Get speed per point (in Km/h)
    currentSpeed = segment.get_speed(index) * 3.6
    speedsList.append(currentSpeed)

    #* Get maxSpeed of list
    if currentSpeed > maxSpeed:
        maxSpeed = currentSpeed

#* Get Duration of activity
#prevTime = segment.points[index - 1]
timeSinceStart = segment.points[len(segment.points) - 1].time_difference(segment.points[0])
print("Duration of activity:", timeSinceStart / 60, "min")

#* Calculate average speed
speedSum = 0
for i, v in enumerate(speedsList):
    speedSum += speedsList[i]
averageSpeed = speedSum / len(speedsList)   #* Sum of items / Amount of items
print("AverageSpeed:", averageSpeed, "Km/h")
print("MaxSpeed:", maxSpeed, "Km/h")
#from pandas import DataFrame

#columns = ['Longitude', 'Latitude', 'Altitude', 'Time', 'Speed']
#df = DataFrame(data, columns=columns)
#df.head()
#print(df.to_string())
