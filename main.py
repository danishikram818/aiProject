import streamlit as st

st.title("Simple Calculator")
if "expr" not in st.session_state:
    st.session_state.expr = ""


def press(x):
    st.session_state.expr += str(x)


def backspace():
    st.session_state.expr = st.session_state.expr[:-1]


def clear():
    st.session_state.expr = ""


def calculate():
    try:
        expr = (
            st.session_state.expr.replace("✖️", "*")
            .replace("➗️", "/")
            .replace("➕️", "+")
            .replace("➖️", "-")
        )
        st.session_state.expr = str(eval(expr))
    except:
        st.session_state.expr = "Error"


st.text_input("Calculator", key="expr", on_change=calculate)


buttons = [
    ["7", "8", "9", "➗️"],
    ["4", "5", "6", "✖️"],
    ["1", "2", "3", "➖️"],
    ["C", "0", "=", "➕️"],
    ["⌫"],
]


for row in buttons:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        if btn == "C":
            cols[i].button(btn, on_click=clear)
        elif btn == "=":
            cols[i].button(btn, on_click=calculate)
        elif btn == "⌫":
            cols[i].button(btn, on_click=backspace)
        else:
            cols[i].button(btn, on_click=press, args=(btn,))
