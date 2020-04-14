POOL_SIZE = 4

SENSORS = [
    'python-car.sensors.joystick.Joystick',
    'python-car.sensors.camera.Camera'
]

PARSERS = [
    'python-car.parsers.joystick.Joystick'
]

EXECUTORS = [
    'python-car.executors.motor.Motor',
    'python-car.executors.servo.Servo'
]

INIT_ACTIVATE_SIGNALS = {
    'Joystick.press_buttons': [(9, )]
}
