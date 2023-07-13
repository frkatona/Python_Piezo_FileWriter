import matplotlib.pyplot as plt

# Open the file and read the data
with open("output.txt", "r") as file:
    data = file.readlines()

# Convert the data to integers
data = [int(line.strip()) for line in data]

# Create a list of time points
time_points = range(len(data))

# Create a plot
plt.figure(figsize=(10,5))
plt.plot(time_points, data)

# Add labels
plt.xlabel('Time points')
plt.ylabel('Piezo signal')

# Display the plot
plt.show()
