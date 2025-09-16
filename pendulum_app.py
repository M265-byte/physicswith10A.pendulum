import streamlit as st 

import numpy as np

import matplotlib.pyplot as plt

import time

 

st.title("🎯 Pendulum Simulation")

 

st.write("The period of a pendulum is given by:")

st.latex(r"T = 2 \pi \sqrt{\frac{L}{g}}")

 

# Sliders for input

L = st.slider("Length of pendulum (m)", 0.1, 5.0, 1.0, 0.1)

g = st.slider("Gravity (m/s²)", 1.0, 20.0, 9.8, 0.1)

amplitude = st.slider("Amplitude (degrees)", 5, 45, 20)

 

# Period calculation

T = 2 * np.pi * np.sqrt(L / g)

st.write(f"**Pendulum Period (T): {T:.2f} seconds**")

 

# Convert amplitude to radians

theta0 = np.radians(amplitude)

 

# Create a placeholder for the animation

placeholder = st.empty()

 

# Animation loop

steps = 200

for i in range(steps):

    t = i * T / steps

    theta = theta0 * np.cos(2*np.pi*t/T)  # SHM angle

   

    x = L * np.sin(theta)

    y = -L * np.cos(theta)

   

    # Create figure

    fig, ax = plt.subplots(figsize=(4,4))

    ax.set_xlim(-L-0.5, L+0.5)

    ax.set_ylim(-L-0.5, 0.5)

    ax.set_aspect('equal')

    ax.axis('off')

   

    # Draw pendulum

    ax.plot([0, x], [0, y], 'k-', lw=2)  # string

    ax.plot(x, y, 'o', markersize=20, color="blue")  # bob

    ax.plot([0], [0], 'ko')  # pivot

   

    # Update the same placeholder

    placeholder.pyplot(fig)

    time.sleep(0.05)