import streamlit as st

container = st.container()
# container.write("This is inside the container")
container.write("""
 <div style="background-color: #8693AB;  height: 100vh;  ">
           Content 1
        </div>
    """,unsafe_allow_html=True)
st.write("This is outside the container")

# Now insert some more in the container
# container.write("This is inside too")