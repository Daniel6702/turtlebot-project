import time
import ultrasonic_sensor
import readFromLightSensor

def main():
    distance_sensor = ultrasonic_sensor.Dist()
    dist = distance_sensor.Measure(15)

    color_sensor = readFromLightSensor.color_sensor()
    color = color_sensor.getAndUpdateColour()

if __name__ == "__main__":
    main()