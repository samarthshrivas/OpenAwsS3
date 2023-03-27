import streamlit as st
import subprocess as sp 
import tempfile

def list_files(endpoint_url, bucket):
    # Call AWS CLI command to list files recursively and write the output to a file
    with tempfile.NamedTemporaryFile() as f:

    
        sp.call(f"aws --output json s3api list-objects --bucket {bucket} --no-sign-request --endpoint-url {endpoint_url} > {f.name}", shell = True)
    # Read the contents of the output file and return it as a string
        # print(f.name)
        st.write('Output File', f.name)
        with open(f.name, 'r') as g:
            st.download_button('Download File', data=g, file_name="output.json", mime='text/plain')


def main():
    # Create Streamlit app
    st.title('Public S3 Files Download')
    # Get user inputs
    st.write("Example: ```https://s3.us-central-1.example.com/seed/```")
    endpoint_url = st.text_input('Endpoint URL', placeholder="https://s3.us-central-1.example.com")
    bucket = st.text_input('Bucket Name', placeholder="seed")
    # Call list_files function to list files and return the output
    if st.button('Start'):
        list_files(endpoint_url, bucket)
        # Display the output file contents

        


if __name__ == '__main__':
    
    main()
    st.warning("This tool is for educational purposes only. The creator is not responsible for any unethical use of this tool.")
