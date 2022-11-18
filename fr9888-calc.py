import re


resistors = [1, 10, 100, 1000, 10000, 100000, 1000000, 1.1, 11, 110, 1100, 11000, 110000, 1100000, 1.2, 12, 120, 1200, 12000, 120000, 1200000, 1.3, 13, 130, 1300, 13000, 130000, 1300000, 1.5, 15, 150, 1500, 15000, 150000, 1500000, 1.6, 16, 160, 1600, 16000, 160000, 1600000, 1.8, 18, 180, 1800, 18000, 180000, 1800000, 2, 20, 200, 2000, 20000, 200000, 2000000, 2.2, 22, 220, 2200, 22000, 220000, 2200000, 2.4, 24, 240, 2400, 24000, 240000, 2400000, 2.7, 27, 270, 2700, 27000, 270000, 2700000, 3, 30, 300, 3000, 30000, 300000, 3000000,
             3.3, 33, 330, 3300, 33000, 330000, 3300000, 3.6, 36, 360, 3600, 36000, 360000, 3600000, 3.9, 39, 390, 3900, 39000, 390000, 3900000, 4.3, 43, 430, 4300, 43000, 430000, 4300000, 4.7, 47, 470, 4700, 47000, 470000, 4700000, 5.1, 51, 510, 5100, 51000, 510000, 5100000, 5.6, 56, 560, 5600, 56000, 560000, 5600000, 6.2, 62, 620, 6200, 62000, 620000, 6200000, 6.8, 68, 680, 6800, 68000, 680000, 6800000, 7.5, 75, 750, 7500, 75000, 750000, 7500000, 8.2, 82, 820, 8200, 82000, 820000, 8200000, 9.1, 91, 910, 9100, 91000, 910000, 9100000, 10000000]


class Combination:
    def __init__(self, r1, r2, v):
        self.r1 = r1
        self.r2 = r2
        self.v = v

    def toString(self):
        return "voltage=" + str(self.v) + " R1=" + str(self.r1) + " R2=" + str(self.r2)


def sortingFunction(c):
    return c.v


results = []
# A = 1 + R2/R1
for r1 in resistors:
    for r2 in resistors:
        voltage = 0.925 * (1+r1/r2)
        # target 2.725
        if voltage > 6.45 and voltage < 6.55:
            results.append(Combination(r1, r2, voltage))

#results.sort(key=lambda x: x.calcVoltage())
results.sort(key=sortingFunction)

for i in results:
    print(i.toString())