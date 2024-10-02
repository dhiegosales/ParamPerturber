import random
import re

# Function to generate a random value between a lower and upper limit
def generate_random_value(limits):
    return random.uniform(limits[0], limits[1])

# Function to process the PorousMedia_1.dat file
def process_file(file_path, param_limits, parameters):
    # Opening the original file for reading
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Storing the randomly generated values for each parameter passed
    random_values = {param: generate_random_value(param_limits) for param in parameters}
    
    # Displaying the randomly generated values for each parameter
    print("Randomly generated values (percentage):")
    for param, value in random_values.items():
        print(f"{param}: {value:.4f}")
    
    # Processing the file line by line
    new_lines = []
    for line in lines:
        for param in parameters:
            # Searching for the keyword followed by ": <value>"
            match = re.search(rf"({param}\s+:\s+)([\d\.eE+-]+)", line)
            if match:
                base_value = float(match.group(2))  # Base value extracted from the file
                modified_value = base_value * random_values[param]  # Applying the fixed percentage noise
                
                # Rewriting the line with the modified value, preserving the format
                formatted_value = f"{modified_value:.5e}" if 'e' in match.group(2) else f"{modified_value:.5f}"
                # Corrected here: using \g<1> to reference the first capture group
                new_line = re.sub(rf"({param}\s+:\s+)[\d\.eE+-]+", rf"\g<1>{formatted_value}", line)
                new_lines.append(new_line)
                break
        else:
            new_lines.append(line)

    # Saving the modifications to the original file
    with open(file_path, 'w') as file:
        file.writelines(new_lines)
    
    print(f"Modifications applied and saved to the file {file_path}")


# Usage example
if __name__ == "__main__":
    # Path to the .dat file of from MOHID-Land model
    file_path = r"D:\PorousMedia_1.dat"

    # Lower and upper limits for each parameter (in tuple format). Example of a limit between 95% (0.95) and 105% (1.05)
    param_limits = (0.92, 1.05)  

    # List of parameters to apply the noise to (you can modify this)
    parameters = ["THETA_R", "THETA_S", "ALPHA", "N_FIT", "SAT_K", "HORIZONTAL_K_FACTOR"] # Modify any parameter that is in the .dat fime you have passed.

    # Processing the file
    process_file(file_path, param_limits, parameters)
