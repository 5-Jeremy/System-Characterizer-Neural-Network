Use these MATLAB live scripts to generate new data for training/testing the neural networks. Currently, all of the scripts generate CSV files where each row contains the coefficients and step response characteristics for a randomly generated system. The step response characteristics are obtained directly from using the stepinfo function from MATLAB's Control Systems Toolbox. Different scripts are used to generate different types of systems or to generate systems with a specific proportion of different characteristics. The scripts are described below.

# Three Coefficients
The scripts titled 3C_Basic_Data_Generator and 3C_Balanced_Data_Generator generate systems with the following form of transfer function:

$$ \frac{s + N_0}{s^{2} + D_{1}s + D_0} $$

where $N_0$, $D_1$, and $D_0$ are coefficients which depend on the randomly chosen poles and zero. The pole values are chosen randomly from a uniform distribution with a default sample space of (-10, 0) (They must be negative to ensure stability). The zero value is chosen randomly from a uniform distribution with a default sample space of (-5, 5).

The script titled 3C_Balanced_Data_Generator is selective in which randomly generated systems it uses such that the resulting dataset contains an approximately equal number of systems which experience overshoot, undershoot, and neither. This is specifically for training a neural network to predict which of these three classes a system falls into. This is not done in 3C_Basic_Data_Generator, so the quantities are not equal for datasets generated using that script.
