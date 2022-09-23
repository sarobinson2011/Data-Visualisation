import matplotlib.pylab as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('bmh')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=1)

# set chart title & label axis
ax.set_title("Square Numbers", fontsize=11)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Values^2", fontsize=12)

# set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=12)

# set the range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()