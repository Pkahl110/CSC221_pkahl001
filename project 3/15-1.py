import matplotlib.pyplot as plt


x_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

fig, ax = plt.subplots()
ax.scatter(x_values, cubes, s=40)

ax.set_title("Cubes", fontsize=24)
ax.set_xlabel('Number', fontsize=18)
ax.set_ylabel('Cube of Number', fontsize=18)

ax.tick_params(axis='both', labelsize=14)

plt.show()