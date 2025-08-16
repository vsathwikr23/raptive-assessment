import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

st.set_page_config(page_title="Beta Distribution Explorer", layout="centered")

st.title("Beta Distribution")
st.write("Explore how the **Beta distribution** changes with different α (alpha) and β (beta) values.")

# Sidebar controls
alpha = st.sidebar.slider("Alpha (α)", min_value=0.1, max_value=10.0, value=2.0, step=0.1)
beta_val = st.sidebar.slider("Beta (β)", min_value=0.1, max_value=10.0, value=2.0, step=0.1)

# Generate values
x = np.linspace(0, 1, 1000)
y = beta.pdf(x, alpha, beta_val)

# Plot
fig, ax = plt.subplots()
ax.plot(x, y, color='blue')
ax.set_title(f"Beta PDF (α={alpha}, β={beta_val})")
ax.set_xlabel("x")
ax.set_ylabel("Probability Density")
st.pyplot(fig)

# Extra: Show mean and variance
mean = alpha / (alpha + beta_val)
variance = (alpha * beta_val) / ((alpha + beta_val)**2 * (alpha + beta_val + 1))
st.markdown(f"**Mean:** {mean:.3f}")
st.markdown(f"**Variance:** {variance:.3f}")

# Simulated bot collab
st.info("This app was created in collaboration with @JulesBot and @CodexAI.")
