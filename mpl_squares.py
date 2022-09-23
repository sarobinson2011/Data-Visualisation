import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# set chart title and label axis
ax.set_title("Square numbers", fontsize=20)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Value^2", fontsize=12)

# set size of tick labels
ax.tick_params(axis='both', labelsize=12)

print(plt.style.available)
plt.show()

