import matplotlib.pyplot as plt

file = open('output.txt')
x = []
y = []
z = []

for i in file:
    vals = i.split();
    x.append(float(vals[0]))
    y.append(float(vals[1]))
    z.append(float(vals[2]))

plt.plot(x, label="x")
plt.plot(y, label="y")
plt.plot(z, label="z")
plt.legend()
plt.ylabel("acc (m/s^2)")
plt.xlabel("timestep (dimensionless)")
plt.show()