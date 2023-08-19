import streamlit as st

# Function to calculate the number of GPUs needed
def calculate_gpus(tokens, hours, epochs, model_size):
    A = (tokens * epochs * model_size * 13.3) / hours
    H = A / 2
    return max(1, round(A)), max(1, round(H))

# Streamlit app
page_title = "LLM GPU Calculator"
st.set_page_config(page_title=page_title, page_icon="🔮")
st.title('🔮 ' + page_title)

# Create a form
with st.form(key='gpu_calculator'):

    # Input fields
    tokens = st.number_input('Enter the number of tokens (in billions)', value=1, format="%i")
    hours = st.number_input('Enter the time to finish (in hours)', value=40, format="%i")
    epochs = st.number_input('Enter the number of epochs', value=2, format="%i")
    model_size = st.number_input('Enter the model size (in billions)', value=30, format="%i")

    # Calculate button
    calculate = st.form_submit_button('Calculate')

    # Calculate the number of GPUs needed
    if calculate:
        A, H = calculate_gpus(tokens, hours, epochs, model_size)
        st.markdown(f'**Number of A100 (80G) GPUs needed: {A}**')
        st.markdown(f'**Number of H100 (80G) GPUs needed: {H}**')

# Put github link at the bottom https://github.com/hunkim/llm_gpt_cal
st.markdown('**Github:** https://github.com/hunkim/llm_gpu_cal')