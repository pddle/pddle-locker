# RUN COMMAND: env FLASK_APP=app.py flask run
# env FLASK_APP=app.py flask run --host=0.0.0.0 --port=5000
# Calling apis using CURL: curl -X METHOD_TYPE url

# DOOR OPENED STATUS_DOOR_X PIN VALUE = 0
# DOOR CLOSED STATUS_DOOR_X PIN VALUE = 1

# import libraries
import time
from flask import Flask, jsonify
from flask_cors import CORS
import RPi.GPIO as GPIO

# import GPIO constants & functions
from lockerActions import openDoor, checkDoorState, turnOnDoorLights, listenDoorEquipmentState, turnOffDoorLights, listenDoorEquipmentStateForEndRental
from gpioActions import initializePins, readPinVoltage
from multiplexorActions import setDoorSelectionMultiplexor, setDoorSensorsMultiplexor

# curl -X POST http://127.0.0.1:5000/open-door-lights/14


app = Flask(__name__)
CORS(app)

# if __name__ == '__main__':
#     app.run(debug=True, port=8080, host='0.0.0.0')

app.run(host="0.0.0.0", port=5000)

@app.route('/open-door-lights/<doorNumber>', methods=['POST'])
def openDoorLightsApi(doorNumber):
    print('\nAPI CALL START___________openDoorLightsApi method called___________API CALL START\n')
    turnOnDoorLights(doorNumber)
    print('\nAPI CALL END___________openDoorLightsApi method called___________API CALL END\n')
    return f'POWER-UP FINISH'



# curl -X POST http://127.0.0.1:5000/close-door-lights/14

@app.route('/close-door-lights/<doorNumber>', methods=['POST'])
def closeDoorLightsApi(doorNumber):
    print('\nAPI CALL START___________openDoorLightsApi method called___________API CALL START\n')
    turnOffDoorLights(doorNumber)
    print('\nAPI CALL END___________openDoorLightsApi method called___________API CALL END\n')
    return f'POWER-UP FINISH'



# curl -X POST http://127.0.0.1:5000/set-pin-high/15


@app.route('/set-pin-high/<pinNumber>', methods=['POST'])
def setPinHighApi(pinNumber):
    print('\nAPI CALL START___________setPinHighApi method called___________API CALL START\n')
    pin = int(pinNumber)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    print('set pin ', pin, 'HIGH')

    print('\nAPI CALL END___________setPinHighApi method called___________API CALL END\n')
    return f'POWER-UP FINISH'

# curl -X POST http://127.0.0.1:5000/set-pin-low/15


@app.route('/set-pin-low/<pinNumber>', methods=['POST'])
def setPinLowApi(pinNumber):
    print('\nAPI CALL START___________setPinLowApi method called___________API CALL START\n')
    pin = int(pinNumber)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

    print('set pin ', pin, 'LOW')

    print('\nAPI CALL END___________setPinLowApi method called___________API CALL END\n')
    return f'POWER-UP FINISH'


# curl -X POST http://127.0.0.1:5000/read-pin/15

@app.route('/read-pin/<pinNumber>', methods=['POST'])
def readPinApi(pinNumber):
    print('\nAPI CALL START___________readPinApi method called___________API CALL START\n')

    pin = int(pinNumber)
    print('pin', pin, 'state', readPinVoltage(pin))

    print('\nAPI CALL END___________readPinApi method called___________API CALL END\n')
    return f'POWER-UP FINISH'

# curl -X POST http://127.0.0.1:5000/set-door-multiplexor/15


@app.route('/set-door-multiplexor/<doorNumber>', methods=['POST'])
def setMultiplexorApi(doorNumber):
    print('\nAPI CALL START___________readPinApi method called___________API CALL START\n')

    setDoorSelectionMultiplexor(doorNumber)
    print('\nAPI CALL END___________readPinApi method called___________API CALL END\n')
    return f'POWER-UP FINISH'

# curl -X POST http://127.0.0.1:5000/set-sensor-multiplexor/15


@app.route('/set-sensor-multiplexor/<doorNumber>', methods=['POST'])
def setSensorMultiplexorApi(doorNumber):
    print('\nAPI CALL START___________readPinApi method called___________API CALL START\n')

    setDoorSensorsMultiplexor(doorNumber)
    print('\nAPI CALL END___________readPinApi method called___________API CALL END\n')
    return f'POWER-UP FINISH'