import streamlit as st

st.set_page_config(
    page_title="AI Restaurant Support Assistant",
    page_icon="🍔",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.answer-box {
    background-color: #E8F5E9; /* Light Green */
    color: #1B5E20; /* Dark Green Text */
    padding: 20px;
    border-radius: 15px;
    border-left: 8px solid #4CAF50;
    margin-top: 15px;
    font-size: 18px;
}

.source-box {
    background-color: #FFF3E0; /* Light Orange */
    color: #E65100;
    padding: 15px;
    border-radius: 10px;
    margin-top: 10px;
}

.stButton>button {
    background-color: #FF6B35;
    color: white;
    border-radius: 10px;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: #E85D2A;
}
</style>
""", unsafe_allow_html=True)

st.title("🍔 AI Restaurant Support Assistant")

question = st.text_input("Ask your question:")

if st.button("Get Answer"):
    answer = "Your refund will be processed within 5-7 business days."

    st.markdown(
        f"""
        <div class="answer-box">
            <b>Answer:</b><br>
            {answer}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="source-box">
            <b>Source:</b> Restaurant FAQ Knowledge Base
        </div>
        """,
        unsafe_allow_html=True
    )
