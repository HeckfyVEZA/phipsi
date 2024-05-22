import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
st.set_page_config(layout="wide")
table = st.file_uploader("Таблицу с фи и пси сюда")
if table:
    df = pd.read_excel(table)
    x = df["Fi"]
    y = df["Psis"]

    polynome_power = st.number_input("Степень полинома", value=4, step=1, min_value=1)

    polynome = np.poly1d(np.polyfit(x, y, polynome_power))

    coefs = list(polynome.coefficients)

    poly_generate = " + ".join([f"a{i} * Fi^{polynome_power - i}" for i in range(polynome_power+1)])
    st.write(f"Полином: {poly_generate}")
    # coef_generate = " ; ".join([f"a{i} = {coefs[i]}" for i in range(polynome_power+1)])
    st.write(f"Коэффициенты:")
    tab_co = [[f'a{i}', coefs[i]] for i in range(polynome_power+1)]
    st.dataframe(pd.DataFrame(tab_co, columns=['коэффициент', 'значение']))

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name='Psis', mode='markers', marker=dict(color='red')))
    x_diap = [x[0], x[-1]]
    dens = 1000
    polix = [x_diap[0] + (x[diap[1]] - x[diap[0]]) * i / dens for i in range(dens+1)]
    fig.add_trace(go.Scatter(x=polix, y=polynome(polix), name=f'f(x) = {poly_generate}', mode='lines', marker=dict(color='blue')))
    st.plotly_chart(fig, use_container_width=True)
