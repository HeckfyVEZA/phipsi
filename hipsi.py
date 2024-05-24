import streamlit as st, pandas as pd, numpy as np, plotly.graph_objects as go
st.set_page_config(layout="wide")
table = st.file_uploader("Таблицу с фи и пси сюда")
if table:
    df = pd.read_excel(table)
    x, y = df["Fi"], df["Psis"]
    polynome_power = st.number_input("Степень полинома", value=4, step=1, min_value=1)
    polynome = np.poly1d(np.polyfit(x, y, polynome_power))
    coefs = list(polynome.coefficients)
    poly_generate = " + ".join([f"A_{'{'+ str(i) +'}'} * \phi^{'{'+str(polynome_power - i)+'}'}" for i in range(polynome_power+1)])
    st.subheader(f"Полином:")
    st.latex("\psi_{s} = " + poly_generate)
    st.write(f"Коэффициенты:")
    st.dataframe(pd.DataFrame([[f'A{i}', coefs[i]] for i in range(polynome_power+1)], columns=['коэффициент', 'значение']), hide_index=True)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name='Испытания', mode='markers', marker=dict(color='red', size=10)))
    fig.add_trace(go.Scatter(x=x, y=polynome(x), name='Полином', mode='lines', marker=dict(color='blue')))
    fig.update_layout(title='График', xaxis_title='ϕ', yaxis_title='ψs', showlegend=True, width=1000, height=500, legend=dict(yanchor="top", y=0.99, xanchor="right", x=0.99), font=dict(family="Arial", size=18, color="black"), autosize=False, margin=dict(l=50, r=50, b=100, t=100, pad=4), paper_bgcolor="white", plot_bgcolor="white", hovermode="x unified", hoverlabel=dict(bgcolor="white", font_color="black"), title_x=0.5, title_font=dict(family="Arial", size=24, color="black"), title_font_color="black", title_xanchor="center", title_yanchor="top", title_y=0.99, xaxis=dict(showgrid=True, gridcolor='grey', gridwidth=1, tickmode='linear', dtick=0.0125), yaxis=dict(showgrid=True, gridcolor='grey', gridwidth=1, tickmode='linear', dtick=0.1))
    st.plotly_chart(fig)
