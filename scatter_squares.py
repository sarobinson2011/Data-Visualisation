import matplotlib.pylab as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('bmh')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=50)

# set chart title & label axis
ax.set_title("Square Numbers", fontsize=12)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Values^2", fontsize=12)

# set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=12)

plt.show()