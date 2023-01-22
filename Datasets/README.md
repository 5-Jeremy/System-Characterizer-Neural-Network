The datasets are grouped based on the number of coefficients used to determine the transfer function. Within each of the folders here, all of the samples use the same formula for their transfer function. The generalized form of the transfer function is as follows:

$$ \frac{N_{K-1}s^{K-1} + N_{K-2}s^{K-2} + \cdots + N_0}{D_{K}s^{K} + D_{K-1}s^{K-1} + \cdots + D_0} $$

where $K$ is the order of the system, and each $N_i$ and $D_i$ is a coefficient. The values of the coefficients are determined by randomly selecting zero and pole locations from a uniform distribution of varying width, with the exception of $N_{K-1}$ and $D_{K}$ which are either fixed at 1 or chosen separately from a uniform distribution.

Datasets also vary by the number of samples and the proportion of the samples which exhibit overshoot or undershoot. Each folder contains its own README with those details.