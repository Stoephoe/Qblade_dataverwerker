import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=np.array(pd.read_csv("Results\\df3.csv",sep=',',skiprows=0))
data=np.delete(data,0,1)
data=np.delete(data,-1,0)


# Function to calculate the heading (angle) between two points
def calculate_heading(point1, point2):
    delta = point2 - point1
    return np.arctan2(delta[1], delta[0])

# Function to filter out values when heading changes suddenly
def filter_values(data, threshold_degrees):
    filtered_data = [data[0]]  # Initialize with the first data point
    threshold_radians = np.deg2rad(threshold_degrees)
    
    for i in range(1, len(data)):
        prev_heading = calculate_heading(filtered_data[-1], data[i])
        current_heading = calculate_heading(data[i-1], data[i])
        print(current_heading)
        # Check if the change in heading is less than the threshold
        if abs(current_heading - prev_heading) <= threshold_radians:
            filtered_data.append(data[i])
    
    return np.array(filtered_data)

# Example usage

threshold_degrees = 2 # Adjust this threshold as needed
filtered_data = filter_values(data, threshold_degrees)

print("Original Data:")
print(data)

print("\nFiltered Data (After Removing Sudden Heading Changes):")
print(filtered_data)

for i in range(0, (len(filtered_data)-1)):
        plt.plot(filtered_data[i])


df = pd.DataFrame(filtered_data)
df.to_csv("Results\\test.csv")
plt.show()