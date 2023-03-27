import streamlit as st
import os
 
def list_files(endpoint_url, bucket):
    # Call AWS CLI command to list files recursively and write the output to a file
    os.system(f"aws --endpoint-url={endpoint_url} s3 ls s3://{bucket}/ --recursive --no-sign-request > output.txt")
    # Read the contents of the output file and return it as a string
    with open('output.txt', 'r') as file:
        file_contents = file.read()
    return file_contents

def download_file(file_contents):
    # Download the output file as a text file
    with open('output.txt', 'w') as file:
        file.write(file_contents)
    st.download_button('Download File', 'output.txt', 'text/plain')

def main():
    # Create Streamlit app
    st.title('List Public S3 Files')
    # Get user inputs
    st.write("Example: ```https://s3.us-central-1.example.com/seed/```")
    endpoint_url = st.text_input('Endpoint URL', placeholder="https://s3.us-central-1.example.com")
    bucket = st.text_input('Bucket Name', placeholder="seed")
    # Call list_files function to list files and return the output
    if st.button('List Files'):
        file_contents = list_files(endpoint_url, bucket)
        # Display the output file contents
        st.text_area('Output', file_contents)
        # Allow user to download the output file
        download_file(file_contents)

if __name__ == '__main__':
    
    main()
    st.warning("This tool is for educational purposes only. The creator is not responsible for any unethical use of this tool.")
