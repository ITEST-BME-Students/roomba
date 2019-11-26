from library import Misc


def kinematics(velocity_norm, omega_degrees):
    d = 235
    omega =  - omega_degrees * 0.0174533 # sign inversion to keep sense of rotation equal to create2 package
    velocity = velocity_norm * 500

    left = (2 * velocity + d * omega) / 2
    right = left - d * omega

    left = Misc.constrain(left, -500, 500)
    right = Misc.constrain(right, -500, 500)

    v = ((left + right) / 2) / 500
    omega = ((left - right) / d) / 0.0174533
    return left, right, v, omega