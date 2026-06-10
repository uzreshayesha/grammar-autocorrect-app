import streamlit as st
from model import GrammarAutocorrectModel

# Initialize backend logic
model = GrammarAutocorrectModel()

# UI Configuration
st.set_page_config(page_title="AI Grammar Assistant", page_icon="📝")
st.title("📝 AI Grammar Autocorrect Assistant")
st.write("You can correct the spelling and grammar of your text here.")

user_input = st.text_area("✍️ Enter your text here:", "hehlo i wants eating apple")

if st.button("✨ Correct Text", use_container_width=True):
    if user_input.strip():
        corrected_output = model.process_text(user_input)
        st.subheader("✅ Corrected Version:")
        st.success(corrected_output)
    else:
        st.warning("Please enter some text first!")
