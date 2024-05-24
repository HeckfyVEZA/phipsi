import streamlit as st, pandas as pd, numpy as np, plotly.graph_objects as go
table = st.file_uploader("Таблицу с фи и пси сюда")
if table:
    df = pd.read_excel(table)
    x, y = df["Fi"], df["Psis"]
    polynome_power = st.number_input("Степень полинома", value=4, step=1, min_value=1)
    polynome = np.poly1d(np.polyfit(x, y, polynome_power))
    coefs = list(polynome.coefficients)
    st.latex("\psi_{s} = " + " + ".join([f"A_{'{'+ str(i) +'}'} * \phi^{'{'+str(polynome_power - i)+'}'}" for i in range(polynome_power+1)])[:-11])
    st.dataframe(pd.DataFrame([[f'A{i}', coefs[i]] for i in range(polynome_power+1)], columns=['коэффициент', 'значение']), hide_index=True, use_container_width=True)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name='Испытания', mode='markers', marker=dict(color='red', size=10)))
    fig.add_trace(go.Scatter(x=np.linspace(min(x), max(x), 50), y=polynome(np.linspace(min(x), max(x), 50)), name='Полином', mode='lines', marker=dict(color='blue')))
    fig.update_layout(title='', xaxis_title='ϕ', yaxis_title='ψs', showlegend=True, width=710, height=500, legend=dict(yanchor="top", y=0.99, xanchor="right", x=0.99), hovermode="x unified", hoverlabel=dict(bgcolor="white", font_color="black"), title_x=0.5, title_xanchor="center", title_yanchor="top", title_y=0.99, xaxis=dict(showgrid=True, gridwidth=.5, dtick=0.0125), yaxis=dict(showgrid=True, gridwidth=.5, dtick=0.1))
    st.plotly_chart(fig)