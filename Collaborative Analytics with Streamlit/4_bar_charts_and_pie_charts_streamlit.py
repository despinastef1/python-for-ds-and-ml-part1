import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

animals = ['cat', 'cow','dog', 'goat']
heights = [30,150,80,60]
weights = [5,400,40,50]

fig, ax = plt.subplots()

x = np.arange(len(heights))
width = 0.40

ax.bar(x - width/2, heights, width, color = 'red')
ax.bar(x + width/2, weights, width, color = 'orange')

ax.legend(['heights', 'weights'])
ax.set_xticks(x)
ax.set_xticklabels(animals)

st.pyplot(fig)

explode = [0.2, 0.1, 0.1, 0.1]
plot_pie, ax = plt.subplots()
ax.pie(heights, labels=animals, explode=explode, autopct='%1.1f%%', shadow = True)
ax.axis('equal')
st.pyplot(plot_pie)
