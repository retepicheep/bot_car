from gpiozero import DistanceSensor

def ultrasonic():
    return DistanceSensor(echo=17, trigger=4).distance