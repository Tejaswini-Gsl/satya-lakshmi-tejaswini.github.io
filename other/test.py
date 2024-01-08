import streamlit as st


st.set_page_config(page_title="Two Columns Layout", layout="wide")

page_bg_img= """
<style>
[data-testid= "stAppViewContainer"]{
background-color: #f0f0f0;
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.write("""
        <div style="background-color: #8693AB;padding: 150px;  ">
           Content 1
        </div>
    """, unsafe_allow_html=True)

with col2:  
    st.write("""
        <div style="background-color: #B2D6FF; padding: 300px; ">
           Content 2
        </div>
    """, unsafe_allow_html=True)

with col1:
    st.write("""
        <div style="background-color: #DDBEA9; padding: 150px; ">
           Content 3
        </div>
    """, unsafe_allow_html=True) 

# with col2:
#     st.write("""
#         <div style="background-color: #FFE1A8; padding: 150px; ">
#            Content 4
#         </div>
#     """, unsafe_allow_html=True)

    