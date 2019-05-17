from sense_hat import SenseHat
from time import sleep


sense = SenseHat()

X = [255, 0, 0]  # Red
O = [0, 0, 0]  # White
BLUE = [0, 0, 255]
GREEN = [50, 205, 50]
RED = [255, 0, 0]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
YELLOW = [255, 255, 0]

digitOne = ""
digitTwo = ""

ledArray = []


class Directions:
    north = [
        0, 0, 0, 0, 1, 0, 0, 0,
        0, 0, 0, 1, 1, 1, 0, 0,
        0, 0, 1, 0, 1, 0, 1, 0,
        0, 1, 0, 0, 1, 0, 0, 1,
        0, 0, 0, 0, 1, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 0, 0,
    ]
    northEast = [
        0, 0, 0, 0, 1, 1, 1, 1,
        0, 0, 0, 0, 0, 0, 1, 1,
        0, 0, 0, 0, 0, 1, 0, 1,
        0, 0, 0, 0, 1, 0, 0, 1,
        0, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0,
        0, 1, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
    ]
    east = [
        0, 0, 0, 0, 1, 0, 0, 0,
        0, 0, 0, 0, 0, 1, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1,
        0, 0, 0, 0, 0, 0, 1, 0,
        0, 0, 0, 0, 0, 1, 0, 0,
        0, 0, 0, 0, 1, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
    ]
    southEast = [
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 0, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0,
        0, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 0, 1,
        0, 0, 0, 0, 0, 1, 0, 1,
        0, 0, 0, 0, 0, 0, 1, 1,
        0, 0, 0, 0, 1, 1, 1, 1,
    ]
    south = [
        0, 0, 0, 0, 1, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1,
        0, 0, 1, 0, 1, 0, 1, 0,
        0, 0, 0, 1, 1, 1, 0, 0,
        0, 0, 0, 0, 1, 0, 0, 0,
    ]
    southWest = [
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 0,
        0, 0, 0, 0, 0, 1, 0, 0,
        0, 0, 0, 0, 1, 0, 0, 0,
        1, 0, 0, 1, 0, 0, 0, 0,
        1, 0, 1, 0, 0, 0, 0, 0,
        1, 1, 0, 0, 0, 0, 0, 0,
        1, 1, 1, 1, 0, 0, 0, 0,
    ]
    west = [
        0, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0,
        0, 1, 0, 0, 0, 0, 0, 0,
        1, 1, 1, 1, 1, 1, 1, 1,
        1, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 0, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0,
        0, 0, 0, 1, 0, 0, 0, 0,
    ]
    northWest = [
        1, 1, 1, 1, 0, 0, 0, 0,
        1, 1, 0, 0, 0, 0, 0, 0,
        1, 0, 1, 0, 0, 0, 0, 0,
        1, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 0, 0,
        0, 0, 0, 0, 0, 1, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
    ]


class Numbers:
    zero = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 1, 1, 1,
        0, 1, 0, 1,
        0, 1, 0, 1,
        0, 1, 0, 1,
        0, 1, 1, 1,
        0, 0, 0, 0,
    ]
    one = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 1, 0,
        0, 1, 1, 0,
        0, 0, 1, 0,
        0, 0, 1, 0,
        0, 1, 1, 1,
        0, 0, 0, 0,
    ]
    two = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 1, 1, 1,
        0, 0, 0, 1,
        0, 1, 1, 1,
        0, 1, 0, 0,
        0, 1, 1, 1,
        0, 0, 0, 0,
    ]
    three = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 1, 1, 1,
        0, 0, 0, 1,
        0, 0, 1, 1,
        0, 0, 0, 1,
        0, 1, 1, 1,
        0, 0, 0, 0,
    ]
    four = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 1, 0, 1,
        0, 1, 0, 1,
        0, 1, 1, 1,
        0, 0, 0, 1,
        0, 0, 0, 1,
        0, 0, 0, 0,
    ]
    five = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 1, 1, 1,
        0, 1, 0, 0,
        0, 1, 1, 1,
        0, 0, 0, 1,
        0, 1, 1, 1,
        0, 0, 0, 0,
    ]
    six = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 1, 1, 1,
        0, 1, 0, 0,
        0, 1, 1, 1,
        0, 1, 0, 1,
        0, 1, 1, 1,
        0, 0, 0, 0,
    ]
    seven = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 1, 1, 1,
        0, 0, 0, 1,
        0, 0, 0, 1,
        0, 0, 0, 1,
        0, 0, 0, 1,
        0, 0, 0, 0,
    ]
    eight = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 1, 1, 1,
        0, 1, 0, 1,
        0, 1, 1, 1,
        0, 1, 0, 1,
        0, 1, 1, 1,
        0, 0, 0, 0,
    ]
    nine = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 1, 1, 1,
        0, 1, 0, 1,
        0, 1, 1, 1,
        0, 0, 0, 1,
        0, 0, 0, 1,
        0, 0, 0, 0,
    ]


def determineEnglishDigit(number, digit):
    num = str(int(number))
    if num[digit] == "0":
        return Numbers.zero
    elif num[digit] == "1":
        return Numbers.one
    elif num[digit] == "2":
        return Numbers.two
    elif num[digit] == "3":
        return Numbers.three
    elif num[digit] == "4":
        return Numbers.four
    elif num[digit] == "5":
        return Numbers.five
    elif num[digit] == "6":
        return Numbers.six
    elif num[digit] == "7":
        return Numbers.seven
    elif num[digit] == "8":
        return Numbers.eight
    elif num[digit] == "9":
        return Numbers.nine


def combineDigitArrays(digitOneArray, digitTwoArray, OnColor, OffColor):
    i = 0
    j = 0
    while i < len(digitOneArray):
        if digitOneArray[i] == 0:
            ledArray.append(OffColor)
        if digitOneArray[i] == 1:
            ledArray.append(OnColor)
        if (i+1) % 4 == 0:
            while j <= i:
                if digitTwoArray[j] == 0:
                    ledArray.append(OffColor)
                if digitTwoArray[j] == 1:
                    ledArray.append(OnColor)
                j += 1
        i += 1
    return ledArray


def translateDirectionToColors(direction, OnColor, OffColor):
    k = 0
    while k < len(direction):
        if direction[k] == 0:
            ledArray.append(OffColor)
        if direction[k] == 1:
            ledArray.append(OnColor)
        k += 1
    return ledArray


def convertTemp(temp):
    tempF = (temp * 9 / 5) + 32
    if tempF >= 100:
        return 99
    else:
        return tempF


def convertPressureToPercent(pressure):
    print("Raw Pressure: " + pressure);
    press = (pressure/1080)*100
    return press


temperature = convertTemp(sense.get_temperature())
humidity = sense.get_humidity()
pressure = convertPressureToPercent(sense.get_pressure())

sense.clear()


def getCurrentTemperature():
    print("Temperature: " % temperature)
    sense.set_pixels(
        combineDigitArrays(determineEnglishDigit(temperature, 0), determineEnglishDigit(temperature, 1), RED, BLACK))
    sense.set_pixel(0, 0, RED);
    sleep(2)
    sense.clear()


def getCurrentHumidity():
    print("Humidity: " % humidity)
    sense.set_pixels(
        combineDigitArrays(determineEnglishDigit(humidity, 0), determineEnglishDigit(humidity, 1), BLUE, BLACK))
    sense.set_pixel(1, 0, BLUE);
    sleep(2)
    sense.clear()


def getCurrentPressure():
    print("Pressure: " % pressure)
    sense.set_pixels(
        combineDigitArrays(determineEnglishDigit(pressure, 0), determineEnglishDigit(pressure, 1), GREEN, BLACK))
    sense.set_pixel(2, 0, GREEN);
    sense.set_pixel(0, 6, GREEN);
    sense.set_pixel(1, 7, GREEN);
    sleep(2)
    sense.clear()


def getCurrentDirection():
    sense.set_imu_config(True, False, False)
    north = sense.get_compass()
    north = int(north)
    print("North: %s" % north)

    if north > 21 and north <= 69:
        print("North: %s" % north)
        sense.set_pixels(translateDirectionToColors(Directions.northEast, YELLOW, BLACK))
    elif north > 70 and north <= 109:
        sense.set_pixels(translateDirectionToColors(Directions.east, YELLOW, BLACK))
    elif north > 111 and north <= 159:
        sense.set_pixels(translateDirectionToColors(Directions.southEast, YELLOW, BLACK))
    elif north > 160 and north <= 212:
        sense.set_pixels(translateDirectionToColors(Directions.south, YELLOW, BLACK))
    elif north > 213 and north <= 249:
        sense.set_pixels(translateDirectionToColors(Directions.southWest, YELLOW, BLACK))
    elif north > 250 and north <= 289:
        sense.set_pixels(translateDirectionToColors(Directions.west, YELLOW, BLACK))
    elif north > 290 and north <= 339:
        sense.set_pixels(translateDirectionToColors(Directions.northWest, YELLOW, BLACK))
    elif north > 340 and north <= 360 or north >= 0 and north < 69:
        sense.set_pixels(translateDirectionToColors(Directions.north, YELLOW, BLACK))

    sleep(1)
    sense.clear()

while True:
    for event in sense.stick.get_events():
        if event.action != "released":
            # print("The joystick was {} {}".format(event.action, event.direction))
            if event.direction == "left":
                ledArray = []
                getCurrentTemperature()
            if event.direction == "up":
                ledArray = []
                getCurrentHumidity()
            if event.direction == "right":
                ledArray = []
                getCurrentPressure()
            if event.direction == "middle":
                ledArray = []
                getCurrentDirection()







