
import streamlit as st
from scripts_flask_final import main_flask
import tempfile
import os
import streamlit_ace

def save_uploaded_file(uploaded_file):
    try:
        with tempfile.NamedTemporaryFile(delete=False) as fp:
            fp.write(uploaded_file.getvalue())
            return fp.name
    except Exception as e:
        st.error(f"Error: {e}")
        return None

st.title('Welcome to Pixi-Plot!')

uploaded_file = st.file_uploader("Your story book please...", type="pdf")

if 'processed' not in st.session_state:
    st.session_state.processed = False

if uploaded_file is not None and not st.session_state.processed:
    temp_path = save_uploaded_file(uploaded_file)
    if temp_path is not None:
        # Call the main_flask function with the path of the saved file
        main_flask(temp_path)
        # Remove the temporary file
        os.remove(temp_path)
        st.session_state.processed = True
        st.success('File processed successfully.')
    else:
        st.error('File processing failed.')

if st.button('Get your comic here :)'):
    st.download_button(
        label="Download output.pptx",
        data=open(r"output.pptx", 'rb'),
        file_name='output.pptx',
        mime='application/vnd.openxmlformats-officedocument.presentationml.presentation'
    )

