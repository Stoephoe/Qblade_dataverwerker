import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Input parameters
Dataset1 = "Cp"       # This specifies the data to be analyzed (currently scripted to process cP data)
Dataset2 = "Ct"       # This specifies the data to be analyzed (currently scripted to process cT data)
x_as = "Lambda"       # X-Axis parameter name

min_a = -24           # For the processing of cP and cT data, the minimum simulated AOA is specified
max_a = 24            # For the processing of cP and cT data, the minimum simulated AOA is specified
interval = 1          # Interval used to simulate cP and cT data

# After this access is only granted to certified nerds, The risk of breaking this script is your own

# Generating an array of angles 'a_df' with specified min_a, max_a, and interval
a_df = np.linspace(min_a, max_a, int((abs(min_a) + abs(max_a)) / interval) + 1)

# Function to process and clean the dataset
def Dataverwerker(Dataset):
    # Construct the file path for the dataset
    handle = "Data\\{Dataset}.csv".format(Dataset=Dataset)
    # Read the dataset into a NumPy array
    data = np.array(pd.read_csv(handle, sep=';', skiprows=2))
    
    # Create an array to delete every other column
    DelIndexArray = (np.linspace(1, (np.shape(data)[1]), (np.shape(data)[1]), endpoint=False)).astype(int)
    DelIndexArray = DelIndexArray[DelIndexArray % 2 == 0]
    
    # Delete every other column in the data
    data = np.delete(data, DelIndexArray, 1)
    
    # Rotate the data and delete the first two rows
    data = np.rot90(data, 1)
    data = np.delete(data, [0, 1], 0)
    
    # Sort the data based on the last column
    data = data[data[:, -1].argsort()]
    
    # Create a Pandas DataFrame from the cleaned data and save it
    df = pd.DataFrame(data)
    df.to_csv("Results\\{Dataset}_clean.csv".format(Dataset=Dataset), index=False)
    
    # Create a plot for the data
    plt.figure()
    for i in range(0, (len(data) - 1)):
        plt.plot(data[i], label=a_df[i])
    
    # Customize the plot
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.xlabel(x_as)
    plt.ylabel(Dataset)
    plt.title("{Dataset} vs {x_as}".format(Dataset=Dataset, x_as=x_as))
    plt.grid()
    
    return data

# Process and clean the datasets
df1 = Dataverwerker(Dataset1)
df2 = Dataverwerker(Dataset2)

# Calculate the ratio of df1 to df2
df3 = np.divide(df1, df2)

# Function to filter a 2D array by x coordinate threshold
def filter_2d_array_by_x_threshold(df3, threshold):
    filtered_2d_array = []
    for line in df3:
        filtered_line = [line[0]]  # Start with the first point in the line
        for i in range(1, len(line)):
            x1, x2 = line[i-1], line[i]
            # Check if the difference in x coordinates is within the threshold and x2 is less than 1
            if abs(x2 - filtered_line[-1]) <= threshold and x2 < 1:
                filtered_line.append(x2)
        filtered_2d_array.append(filtered_line)
    return filtered_2d_array

# Set your x coordinate threshold
x_threshold = 10

# Apply the filtering to df3
df3 = filter_2d_array_by_x_threshold(df3, x_threshold)

# Create a Pandas DataFrame from the filtered data and save it
df = pd.DataFrame(df3)
df.to_csv("Results\\{Dataset1}_{Dataset2}_clean.csv".format(Dataset1=Dataset1, Dataset2=Dataset2))

# Create a plot for the filtered data
plt.figure()
for i in range(0, (len(df3) - 1)):
    plt.plot(df3[i], label=a_df[i])

# Customize the plot
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlabel(x_as)
plt.ylabel("{Dataset1}/{Dataset2}".format(Dataset1=Dataset1, Dataset2=Dataset2))
plt.title("{Dataset1}/{Dataset2} vs {x_as}".format(Dataset1=Dataset1, Dataset2=Dataset2, x_as=x_as))
plt.grid()
plt.ylim((-1, 1))
plt.show()
