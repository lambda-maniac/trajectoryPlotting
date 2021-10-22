from math import sin, tan, cos, pi

import numpy             as np
import matplotlib.pyplot as plt

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Arc:
    def __init__(self, origin, angle, velocity, gravity, worldX, worldY):
        self.origin     = origin
        self.angle      = angle * pi / 180
        self.rawAngle   = angle
        self.velocity   = velocity
        self.gravity    = -gravity
        self.rawGravity = gravity
        self.worldX     = worldX
        self.worldY     = worldY

    def trajectory(self, time):
        """
        ::: Formula:
        :::     y = xtanθ + gx² / 2v0.cos²θ + h
        :::
        ::: Where:
        :::     x is time.
        :::     v is the velocity, and v0 is velocity in function of time 0.
        :::     g is the gravity, and must be negative.
        :::     θ is the angle.
        """
        return time * tan(self.angle) + (
            (self.gravity * (time ** 2))
                         /                                
            (2 * (self.velocity ** 2) * (cos(self.angle) ** 2))
        ) + self.origin.y

    # Formula: v0²sin2θ / g
    @property# It can be a property because there's no need to function in time.
    def R(self): return ((self.velocity ** 2) * sin(2 * self.angle)) / self.rawGravity

    # Formula: (v0²sin²θ / 2g) [+ h]
    @property# It can be a property because there's no need to function in time.
    def H(self): return (((self.velocity ** 2) * (sin(self.angle) ** 2)) / (2 * self.rawGravity)) + self.origin.y

    def plotArc(self):
        xs = np.linspace(self.origin.x, self.worldX.y if self.rawAngle <= 90 else self.worldX.x)
        ys = self.trajectory(xs)

        plt.plot(xs, ys, "--g")

    def plotRange(self):
        plt.hlines(self.origin.y, self.origin.x, self.R, "y", "dashed")

    def plotHeight(self):
        plt.vlines(self.R / 2, self.origin.y, self.H, "r", "dashed")

def main():
    # ========== \Setup ========== #
    X_LIM = Vector2(-10, 10)
    Y_LIM = Vector2(-10, 20)
    plt.axis([X_LIM.x, X_LIM.y, Y_LIM.x, Y_LIM.y])

    # Some more constants:
    ANGLE    = 100
    VELOCITY = 14.45
    GRAVITY  = 10

    # Draw Thrower:
    THROWER = Vector2(0, 5)
    plt.scatter(THROWER.x, THROWER.y)

    # Draw a Target:
    PSEUDO_TARGET1 = Vector2(X_LIM.x + 2, 0)
    plt.scatter(PSEUDO_TARGET1.x, PSEUDO_TARGET1.y)

    # Draw a Target:
    PSEUDO_TARGET2 = Vector2(X_LIM.y / 2, 0)
    plt.scatter(PSEUDO_TARGET2.x, PSEUDO_TARGET2.y)

    # Draw ground:
    plt.hlines(0, X_LIM.x, X_LIM.y)

    # Draw Thrower's tower:
    plt.vlines(THROWER.x, 0, THROWER.y)

    # Some naming:
    plt.xlabel("TIME")
    plt.ylabel("f(x)")
    # ========== /Setup ========== #

    # ========== \Trajectory calculating ========== #

    TRAJECTORY1 = Arc(THROWER, ANGLE, VELOCITY, GRAVITY, X_LIM, Y_LIM)
    TRAJECTORY1.plotArc()
    TRAJECTORY1.plotRange()
    TRAJECTORY1.plotHeight()

    TRAJECTORY2 = Arc(THROWER, 80, 11.15, GRAVITY, X_LIM, Y_LIM)
    TRAJECTORY2.plotArc()
    TRAJECTORY2.plotRange()
    TRAJECTORY2.plotHeight()

    # ========== /Trajectory calculating ========== #

    plt.show()

if __name__ == '__main__': main(); exit(0)
