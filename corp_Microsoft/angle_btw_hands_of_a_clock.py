class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # the angle of hour + contribution from minutes
        h = hour % 12 * 30 + minutes / 60 * 30

        # the angle of minute
        m = minutes * 6

        angle = abs(m - h)

        if angle > 180:
            angle = 360 - angle

        return angle

# math, not much else