import streamlit as st

# st.set_page_config(
#     page_title="AI Detector",
#     page_icon="🤖",
#     layout="wide",
# )

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1698945746290-a9d1cc575e77?auto=format&fit=crop&q=80&w=1946&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}
[data-testid="stHeader"] {
    background-color: transparent;
}

data-testid="stToolbar"{
right: 2rem;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)




st.markdown(
    """
    <div style="position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center;">
        <h2 style="color: #000000;">ROVER CHATBOT</h2>
        <p style="color: #000000;">Powered by Meta Llama and Streamlit.</p>
    </div>
    """,
    unsafe_allow_html=True
)

