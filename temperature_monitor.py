import random
import csv
import matplotlib.pyplot as plt

# Generate 50 temperature readings
temperatures = []

for i in range(50):
    temp = random.randint(20, 40)
    temperatures.append(temp)

print("50 temperature readings generated.")

# Save readings in CSV file
with open("temperature_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Reading", "Temperature"])

    for i, temp in enumerate(temperatures, start=1):
        writer.writerow([i, temp])

print("Data saved successfully.")

# Read and validate CSV data
valid_temperatures = []

with open("temperature_data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        try:
            temp = float(row[1])

            if 0 <= temp <= 50:
                valid_temperatures.append(temp)
            else:
                print("Invalid temperature:", temp)

        except (ValueError, IndexError):
            print("Missing or invalid data detected.")

# Calculate average
if valid_temperatures:
    average = sum(valid_temperatures) / len(valid_temperatures)
    print("Average temperature:", round(average, 2), "°C")

# Display high temperature warnings
for temp in valid_temperatures:
    if temp > 35:
        print("WARNING! High temperature:", temp, "°C")

# Create temperature graph
plt.plot(valid_temperatures)
plt.title("IoT Temperature Monitoring System")
plt.xlabel("Reading Number")
plt.ylabel("Temperature (°C)")

plt.savefig("temperature_graph.png")
plt.show()

print("Temperature monitoring completed.")
