
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# xlim is 86400 seconds (1 day), ylim is a 100 MHz range
fig = plt.figure()
plt.xlim(0,86400)
plt.ylim(0,100)

def animate(i):
    
    # Define initial values
    entry = []
    time_full = []
    time_sec = []
    time_min = []
    time_hr = []
    time_sum = []
    freq = []
    pow = []

    text_file = open("usrp_data.txt", "r")

    # Read in and seperate each line in file
    lines = text_file.readlines()
    text_file.close()
    
    # Get rid of trailing \n
    for x in range (0, len(lines) - 1):
        lines[x] = lines[x].rstrip()

    # Split data file into each value i.e. time, power, freq
    for x in range (0, len(lines) - 1):
        entry.append(lines[x].split(" "))

    # Split all the data into seperate arrays
    for x in range (0, len(entry) - 1):
        time_full.append(entry[x][1].split(":"))
        time_sec.append(time_full[x][2])
        time_min.append(time_full[x][1])
        time_hr.append(time_full[x][0])
        freq.append(entry[x][2])
        pow.append(entry[x][3])

    # Get rid of leftover whitespace
    for x in range (0, (len(time_sec) - 1)):
        time_sec[x] = time_sec[x].strip()
        time_min[x] = time_min[x].strip()
        time_hr[x] = time_hr[x].strip()

    # Convert time values from string to float
    for x in range (0, len(time_sec)):
        time_sec[x] = float(time_sec[x])
        time_min[x] = float(time_min[x])
        time_hr[x] = float(time_hr[x])

    # Sum sec, min, hr to create x-values measured in seconds since midnight
    for x in range (0, len(time_sec)):
        time_sum.append(time_sec[x] + 60 * time_min[x] + 3600 * time_hr[x])

    # Change freq and pow from strings to floats
    freq = [float(l) for l in freq]
    pow = [float(m) for m in pow]

    # Plot
    fig.clear()
    plt.hist2d(time_sum, freq, bins = [8640, 100], weights = pow)

# Have program loop and keep plotting data as it comes into file
ani = animation.FuncAnimation(fig, animate)
plt.show()
