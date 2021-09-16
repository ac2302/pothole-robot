from MotorModule import Motor
import WebcamModule
import flaskapp

motor = Motor(2, 3, 4, 17, 22, 27)

flaskapp.getImg = WebcamModule.getImg

sen = 1.3  # sensitivity
maxVal = 0.3  # max speed


if __name__ == '__main__':
    while True:
        motor.move(
            0.5 * flaskapp.state.speed,
            maxVal * flaskapp.state.curve,
            0.1
        )
