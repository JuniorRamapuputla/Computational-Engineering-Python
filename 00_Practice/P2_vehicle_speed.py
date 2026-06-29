"""
TITLE: Vehicle Speed and Distance
DESCRIPTION: A program that calculates the instantaneous speed, distance and average speed under constant acceleration
AUTHOR: [Junior Ramapuputla]
DATE: 2026/06/27
"""
from scipy import integrate, constants
#Vehicles velocity equation: (v = 20-15t^2)
v = lambda t: 20-15*t**2 

# Calculates the instantaneous speed of the vehicle after time in seconds
def ins_speed(time):
    return v(time)

# Calculates the distance covered by the vehicle in a time interval
# Returns a dictionary with the distances in km,m, cm and mm respectively
def distance(startTime, endTime):
    #The distance is found by integrating the velocity equation
    distance = integrate.quad(v, startTime, endTime)
    
    #Convert to kilometer using SI Constants from scipy
    kilo = distance[0]/constants.kilo
    meter = distance[0]
    cm = distance[0]/constants.centi
    mm = distance[0]/constants.milli
    
    return [kilo,meter, cm, mm]

#calculates the average speed of the vehicle within the given time interval
# returns the average speed in both m/s and km/h
def average_speed(startTime, endTime):
    #Average speed is found by: Total distance/Total Time
    
    TotalDistance = distance(startTime , endTime)
    TotalTime = endTime - startTime
    
    mPerSecond = TotalDistance[1]/TotalTime
    kmPerHour = (TotalDistance[1]/TotalTime)/constants.kmh
    
    return [mPerSecond, kmPerHour]

def main():
    time = (float)(input("Enter the time at which to find the instantaneous speed: "))
    startTime = (float)(input("Enter the starting time: "))
    endTime = (float)(input("Enter the ending time: "))
    
    
    insSpeed = ins_speed(time)
    print(f"The instantaneous speed is:" , insSpeed , "m/s\n")
    
    distances = distance(startTime, endTime)
    print(f"The distance in kilometers:" ,distances[0], "km")
    print(f"The distance in meters:" ,distances[1], "m")
    print(f"The distance in centimeters:" ,distances[2], "cm")
    print(f"The distance in millimeters:" ,distances[3], "mm\n")
    
    avg_speed = average_speed(startTime, endTime)
    print(f"The average speed in m/s:" ,avg_speed[0], "m/s")
    print(f"The average speed in km/h:" , avg_speed[1], "km/h")
    
    
    
if __name__ == '__main__':
    main()