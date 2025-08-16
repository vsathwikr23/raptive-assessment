import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

st.set_page_config(page_title="Beta Distribution & Bayesian Update", layout="centered")

st.title("Beta Distribution & Bayesian Inference")
st.write("Explore how the **Beta distribution** behaves and how it updates after observing data using **Bayesian inference**.")

st.sidebar.header("Prior Distribution")
alpha = st.sidebar.slider("Alpha (α)", min_value=0.1, max_value=10.0, value=2.0, step=0.1)
beta_val = st.sidebar.slider("Beta (β)", min_value=0.1, max_value=10.0, value=2.0, step=0.1)

st.sidebar.header("Observed Data")
trials = st.sidebar.number_input("Number of trials (n)", min_value=1)
successes = st.sidebar.number_input("Number of successes (x)", min_value=0, max_value=trials)

x = np.linspace(0, 1, 1000)

# Prior
prior_y = beta.pdf(x, alpha, beta_val)

# Posterior
posterior_alpha = alpha + successes
posterior_beta = beta_val + trials - successes
posterior_y = beta.pdf(x, posterior_alpha, posterior_beta)

fig, ax = plt.subplots()
ax.plot(x, prior_y, label=f"Prior Beta(α={alpha}, β={beta_val})", color='blue')
ax.plot(x, posterior_y, label=f"Posterior Beta(α={posterior_alpha}, β={posterior_beta})", color='green')
ax.set_xlabel("x (e.g., conversion rate)")
ax.set_ylabel("Probability Density")
ax.set_title("Prior vs Posterior Distributions")
ax.legend()
st.pyplot(fig)

st.markdown("Distribution Statistics")
prior_mean = alpha / (alpha + beta_val)
posterior_mean = posterior_alpha / (posterior_alpha + posterior_beta)

prior_var = (alpha * beta_val) / ((alpha + beta_val)**2 * (alpha + beta_val + 1))
posterior_var = (posterior_alpha * posterior_beta) / ((posterior_alpha + posterior_beta)**2 * (posterior_alpha + posterior_beta + 1))

st.markdown(f"Prior Mean: {prior_mean:.3f},  Prior Variance: {prior_var:.4f}")
st.markdown(f"Posterior Mean: {posterior_mean:.3f},  Posterior Variance: {posterior_var:.4f}")
