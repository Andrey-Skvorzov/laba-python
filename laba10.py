import matplotlib.pyplot as plt
x = ['Python ', 'C ', 'Java ', 'C++', 'C#', 'Visual Basic', 'JS']
popularity = [17.18, 15.08, 11.98, 10.75, 4.25, 4.11, 2.74]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color=(0.4, 0.6, 0.8, 1.0))
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("TIOBE Index for November 2022\n" + "November Headline: Rust keeps its top 7 position")
plt.xticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()