import streamlit as st
import numpy as np
st.title("🎈 My first app")
st.write(
    "Let's start building! "
)
gp=st.radio('Which trigo graph do you want',['sin','cos','tan'],index=None,)
if gp=='sin':
    x=np.linspace(0,2*np.pi,100)
    y=np.sin(x)
    st.line_chart(y)
elif gp=='cos':
   x=np.linspace(0,2*np.pi,100)
   y=np.cos(x)
   st.line_chart(y)
else:
   x=np.linspace(0,2*np.pi,100)
   y=np.tan(x)
   st.line_chart(y)
