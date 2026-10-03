import time
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

rows = np.random.randn(1,1)

'Growing Line Chart:'

placeholder = st.empty()
data = pd.DataFrame(rows)
placeholder.line_chart(data)

for i in range(1, 100):
    new_rows = rows[0] + np.random.randn(1, 1)

    data = pd.concat(
        [data, pd.DataFrame(new_rows)],
        ignore_index=True
    )
    placeholder.line_chart(data)
    rows = new_rows
    time.sleep(0.05)

    values = np.random.randn(10)
    'maplotlibs Line Chart:'
    fig, ax = plt.subplots()
    ax.plot(values)
    st.pyplot(fig)
