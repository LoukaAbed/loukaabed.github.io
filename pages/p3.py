import streamlit as st

st.title('Testing Streamlit and code implementation')


if 'counter' not in st.session_state:
    st.session_state['counter']=0
with st.form('batch_files_upload', clear_on_submit=True):
    uploaded=st.file_uploader("Upload multiple files dataset", type=None, accept_multiple_files=True, key='upload')
    upload_button = st.form_submit_button('Upload Dataset')

if st.session_state['upload']:
    dataset=st.session_state['upload']
    for file in dataset:
        st.write(f"File: {file.name} was successfully uploaded")
else:
    st.warning('Please upload the files before clicking submit')