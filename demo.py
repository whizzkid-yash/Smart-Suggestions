import streamlit as st 
from smart_reply_suggestions import get_response
st.title("Smart Reply Suggestions")

st.header("Input text")



# Define function to process input text and return list of 3 values
def process_text(input_text):
    # replace this with your own function that processes the text and returns a list
    output_list = [input_text.upper(), len(input_text), input_text.count(" ")+1]
    return output_list



# Add text input field to the app
input_text = st.text_input("Enter some text here:")

# Process the input text using the function when the user clicks the button
if st.button("Process Text"):
    output_list = get_response(input_text)
    
    for i in range(len(output_list)):
    # Display each value in a separate rectangular box
        st.info(f"{output_list[i]}")

