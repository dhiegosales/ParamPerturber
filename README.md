# ParamPerturber

**ParamPerturber** is a Python tool that introduces controlled random noise to specific parameters in hydrological data files, enhancing sensitivity analysis and model calibration processes.

## Features

- **Random Noise Generation**: Applies random perturbations within specified limits.
- **Customizable Parameters**: Allows users to specify which parameters to modify.
- **File Format Preservation**: Maintains the original format of the data file during modifications.

## How It Works

The program reads a specified data file (e.g., `PorousMedia_1.dat`), identifies defined parameters, and applies a random value (percentage noise) to their current values. The modified values are then saved back to the original file.

## Parameters

- `file_path`: Path to the input `.dat` file containing the hydrological parameters.
- `param_limits`: A tuple defining the lower and upper limits for noise generation (e.g., `(0.92, 1.05)`).
- `parameters`: A list of parameters to which the noise will be applied (e.g., `["THETA_R", "THETA_S", "ALPHA", "N_FIT", "SAT_K", "HORIZONTAL_K_FACTOR"]`).

## Usage

1. Ensure you have Python installed on your system.
2. Clone this repository or download the script.
3. Modify the `file_path`, `param_limits`, and `parameters` as needed in the `__main__` section of the code.
4. Run the script.

### Example

```python
if __name__ == "__main__":
    file_path = r"D:\PorousMedia_1.dat"
    param_limits = (0.92, 1.05)  
    parameters = ["THETA_R", "THETA_S", "ALPHA", "N_FIT", "SAT_K", "HORIZONTAL_K_FACTOR"]
    process_file(file_path, param_limits, parameters)
