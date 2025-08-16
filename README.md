# Beta distribution Visualizer with Bayesian Inference

This is a repository to a streamlit application which allows users to interact and explore the beta distribution, a probability distribution commonly used to model probabilites and proportions. 

This app has two main components:

**Beta Distribution Visualizer**
It uses sliders to dynamically change the shape parameters, alpha and beta, and visualize how the Probability Density Function (PDF) of the Beta distribution changes. It also calculates mean and variance of the distribution for each selection. This line on the plot is represented with a blue curve as Prior Beta.

**Bayesian Inference Demo**
This demonstrates how the beta distribution acts as a conjugate prior in the bayesian inference for binomial processes. There are 2 fields with trials and successes which denote the new observed data. Using this and the prior data, posterior distribution is calculated, reflecting how beliefs are updated with new evidence.

**Use cases**: There are a lot of use cases in this beta distribution like success probabilities, conversion rates, etc.
