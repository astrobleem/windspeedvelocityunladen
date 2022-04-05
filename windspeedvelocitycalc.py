
import statistics
import math

# compute the wind speed velocity of an unladen swallow
def calculateWindSpeedVelocity(windSpeed, windDirection):
    windSpeed = float(windSpeed)
    windDirection = float(windDirection)
    windSpeedVelocity = windSpeed * (math.cos(windDirection))
    return windSpeedVelocity



def findSpeedofBird(windSpeed, windDirection, birdHeight):
    windSpeedVelocity = calculateWindSpeedVelocity(windSpeed, windDirection)
    birdHeight = float(birdHeight)
    birdSpeed = windSpeedVelocity * (math.sin(birdHeight))
    return birdSpeed

birdType = input("What type of bird are you flying? ")
#only accept birdType of "swallow"
if birdType == "swallow":
    # ask if is a european or african swallow
    birdOrigin = input("Is this a European or African swallow? ")
    # if european, add 10 to the wind speed, if african, subtract 10
    if birdOrigin == "European":
        windSpeed = input("What is the wind speed? ")
        windDirection = input("What is the wind direction? ")
        birdHeight = input("What is the bird's height? ")
        birdSpeed = findSpeedofBird(windSpeed, windDirection, birdHeight)
        print("The bird's speed is", birdSpeed)
    elif birdOrigin == "African":
        windSpeed = input("What is the wind speed? ")
        windDirection = input("What is the wind direction? ")
        birdHeight = input("What is the bird's height? ")
        birdSpeed = findSpeedofBird(windSpeed, windDirection, birdHeight)
        print("The bird's speed is", birdSpeed)
    else:
        print("That is not a valid answer.")
else:
    windSpeed = input("What is the wind speed? ")
    windDirection = input("What is the wind direction? ")
    birdHeight = input("What is the height of the bird? ")
    birdSpeed = findSpeedofBird(windSpeed, windDirection, birdHeight)
    print("The bird's speed is", birdSpeed)













