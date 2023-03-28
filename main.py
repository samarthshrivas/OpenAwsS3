import streamlit as st
import subprocess as sp 
import tempfile
import json
from pathlib import Path
import os
def list_files(endpoint_url, bucket):
    # Call AWS CLI command to list files recursively and write the output to a file
    with tempfile.NamedTemporaryFile() as f:

    
        sp.call(f"aws --output json s3api list-objects --bucket {bucket} --no-sign-request --endpoint-url {endpoint_url} > {f.name}", shell = True)
    # Read the contents of the output file and return it as a string
        # print(f.name)
        
        with open(f.name, 'r') as g:
            js = json.load(g)
            st.write('Total Files', len(js["Contents"]))
            st.download_button('Download Json', data=Path(f.name).read_text(), file_name="output.json", mime='application/json')
            st.download_button("Download Links.txt", data='\n'.join([os.path.join(endpoint_url,bucket,x["Key"]) for x in js["Contents"]])(), file_name="links.txt" )


def main():
    # Create Streamlit app
    st.title('Public S3 Files Download')
    # Get user inputs
    st.write("Example: ```https://s3.us-central-1.example.com/seed/```")
    endpoint_url = st.text_input('Endpoint URL', placeholder="https://s3.us-central-1.example.com")
    bucket = st.text_input('Bucket Name', placeholder="seed")
    # Call list_files function to list files and return the output

    if endpoint_url:
        if st.button('Start'):
            print("Working on -------------------", endpoint_url, bucket)
            list_files(endpoint_url, bucket)
            

        


if __name__ == '__main__':
    
    main()
    st.warning("Disclaimer: This tool is for educational purposes only. The creator is not responsible for any unethical use of this tool.")
