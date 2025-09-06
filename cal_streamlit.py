import streamlit as st

st.title("Simple Calculator")

# Current expression
if "expr" not in st.session_state:
    st.session_state.expr = ""

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Display
st.text_input("Expression", value=st.session_state.expr, key="display", disabled=True)

# Button clicks
for row in buttons:
    cols = st.columns(len(row))
    for i, btn in enumerate(row):
        if cols[i].button(btn):
            if btn == "=":
                try:
                    st.session_state.expr = str(eval(st.session_state.expr))
                except:
                    st.session_state.expr = "Error"
            elif btn == "C":
                st.session_state.expr = ""
            else:
                st.session_state.expr += btn
