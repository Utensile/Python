import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import random as rand
import math

plt.style.use("fivethirtyeight")

time = [0.000, 0.093, 0.186, 0.279, 0.357, 0.435, 0.530, 0.623, 0.701, 0.793, 0.870, 0.962, 1.040, 1.133, 1.228, 1.305, 1.398, 1.475, 1.570, 1.649, 1.743, 1.820, 1.914, 1.991, 2.085, 2.164, 2.256, 2.333, 2.426, 2.504, 2.504, 2.596, 2.673, 2.766, 2.859, 2.936, 3.014, 3.108, 3.186, 3.279, 3.373, 3.450, 3.545, 3.623, 3.717, 3.795, 3.873]
force =[0.00, 0.36, 1.19, 1.86, 2.85, 5.06, 9.56, 15.09, 20.06, 24.57, 28.97, 33.07, 37.00, 41.24, 44.70, 46.35, 41.78, 30.35, 20.68, 16.20, 14.23, 12.75, 11.27, 9.86, 9.05, 8.50, 8.19, 7.70, 6.92, 6.37, 6.37, 5.99, 5.43, 4.76, 4.22, 3.77, 3.37, 3.04, 2.80, 2.57, 2.40, 2.25, 2.11, 2.02, 1.93, 1.86, 1.84]

plt.plot(time, force, linewidth=3, color="#FF0000",label="Force(N)")
plt.title("Force(N) in time(s)")
plt.xlabel("Time(s)")
plt.ylabel("Force(N)")
plt.fill_between(time, force, alpha=0.2, color="#FF0000", label="Impulse(N*s)")
plt.legend()
plt.grid(True)
plt.tight_layout()
print("Showing... ")
plt.show()

