import csv
import datetime
import astropy.time
import matplotlib.pyplot as plt


# Defining a function to parse the CSV data and find the current positions
def set_position(planet, color, file, inner=True):

    data = csv.reader(open(file))

    for line in data:
        if float(line[0]) == today:
            fig.suptitle(line[1], y=.85)
            ax1.scatter(float(line[2]), float(line[3]), s=25, color=color, label=planet)
            ax2.scatter(float(line[2]), float(line[3]), s=25, color=color, label=planet)
            if inner == False:
                ax3.scatter(float(line[2]), float(line[3]), s=25, color=color, label=planet)
            break


# Converting the date to the Julian Day for simple CSV file reading
today = datetime.date.today()
today = astropy.time.Time(str(today))
today = today.jd


# Initiating the plots
plt.style.use('dark_background')

fig = plt.figure()

ax1 = plt.subplot2grid((1, 3), (0, 1))
ax2 = plt.subplot2grid((1, 3), (0, 0))
ax3 = plt.subplot2grid((1, 3), (0, 2))

ax1.scatter(0, 0, s=25, color='yellow', label='Sun')
ax2.scatter(0, 0, s=25, color='yellow', label='Sun')
ax3.scatter(0, 0, s=25, color='yellow', label='Sun')


# Using the function to graph the planets
set_position('Mercury', 'orange', r'csv_data/mercury_positions.csv')
set_position('Venus', 'crimson', r'csv_data/venus_positions.csv')
set_position('Earth', 'green', r'csv_data/earth_positions.csv')
set_position('Mars', 'red', r'csv_data/mars_positions.csv')
set_position('Jupiter', 'orange', r'csv_data/jupiter_positions.csv', False)
set_position('Saturn', 'grey', r'csv_data/saturn_positions.csv', False)
set_position('Uranus', 'cyan', r'csv_data/Uranus_positions.csv', False)
set_position('Neptune', 'blue', r'csv_data/neptune_positions.csv', False)


# Setting the title and limits of the graphs
ax1.set_title('All Planets')
ax1.set_xlim(-35,35)
ax1.set_ylim(-35,35)
ax1.set_aspect('equal')

ax2.set_title('Inner Planets')
ax2.set_xlim(-2,2)
ax2.set_ylim(-2,2)
ax2.set_aspect('equal')

ax3.set_title('Outer Planets')
ax3.set_xlim(-32,32)
ax3.set_ylim(-32,32)
ax3.set_aspect('equal')

plt.tight_layout()


plt.show()
