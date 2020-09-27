POOL_SIZE = 4

SENSORS = [
    'python-car.sensors.joystick.Joystick',
    'python-car.sensors.joystick.RightAxes',
    'python-car.sensors.trace.GroupTrace',
    # 'python-car.sensors.camera.Camera'
]

PARSERS = [
    'python-car.parsers.joystick.Joystick',
    'python-car.parsers.automatic.Automatic',
]

EXECUTORS = [
    'python-car.executors.motor.Motor',
    'python-car.executors.servo.Servo',
]
