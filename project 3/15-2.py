import matplotlib.pyplot as plt

x_values = list(range(5001))
cubes = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, cubes, c=cubes, cmap=plt.cm.PuBuGn, s=10)

ax.set_title("Cubes", fontsize=24)
ax.set_xlabel('Numbers', fontsize=18)
ax.set_ylabel('Cube of Numbers', fontsize=18)

ax.tick_params(axis='both', labelsize=14)
ax.axis([0, 5100, 0, 5100**3])

plt.show()