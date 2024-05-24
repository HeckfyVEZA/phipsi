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

    poly_generate = " + ".join([f"A{i} * \phi^{'{'+str(polynome_power - i)+'}'}" for i in range(polynome_power+1)])
    st.subheader(f"Полином:")
    st.latex("\psi = " + poly_generate)
    # coef_generate = " ; ".join([f"a{i} = {coefs[i]}" for i in range(polynome_power+1)])
    st.write(f"Коэффициенты:")
    tab_co = [[f'A{i}', coefs[i]] for i in range(polynome_power+1)]
    st.dataframe(pd.DataFrame(tab_co, columns=['коэффициент', 'значение']), hide_index=True)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name='Испытания', mode='x', marker=dict(color='red')))
    fig.add_trace(go.Scatter(x=x, y=polynome(x), name='Полином', mode='lines', marker=dict(color='blue')))
    fig.update_layout(title='График', xaxis_title='Fi', yaxis_title='Psis', showlegend=True, width=1000, height=500, legend=dict(yanchor="top", y=0.99, xanchor="right", x=0.99), font=dict(family="Arial", size=18, color="black"), autosize=False, margin=dict(l=50, r=50, b=100, t=100, pad=4), paper_bgcolor="white", plot_bgcolor="white", hovermode="x unified", hoverlabel=dict(bgcolor="white", font_color="black"), title_x=0.5, title_font=dict(family="Arial", size=24, color="black"), title_font_color="black", title_xanchor="center", title_yanchor="top", title_y=0.99)

    st.plotly_chart(fig)
