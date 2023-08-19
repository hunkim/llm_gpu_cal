import streamlit as st
import math

# Function to calculate the number of GPUs needed
def calculate_gpus(tokens, hours, epochs, model_size):
    A = math.ceil((tokens * epochs * model_size * 13.3) / hours)
    H = math.ceil(A / 2)
    st.markdown(f'**Number of A100 (80G) GPUs needed: {A}**')
    st.markdown(f'**Number of H100 (80G) GPUs needed: {H}**')

def calculate_gpus_inference(throughput, qpm, output_tokens):
    A = math.ceil(output_tokens / throughput * qpm / 60)
    H = math.ceil(A / 2)
    st.markdown(f'**Number of A100 (80G) GPUs needed: {A}**')
    st.markdown(f'**Number of H100 (80G) GPUs needed: {H}**')

# Streamlit app
page_title = "LLM GPU Calculator"
st.set_page_config(page_title=page_title, page_icon="🔮")
st.title('🔮 ' + page_title)

# Create a form
st.markdown('## Training GPUs')
with st.form(key='gpu_calculator_training'):

    # Input fields
    tokens = st.number_input('Enter the number of tokens (in billions)', value=1, format="%i")
    hours = st.number_input('Enter the time to finish (in hours)', value=40, format="%i")
    epochs = st.number_input('Enter the number of epochs', value=2, format="%i")
    model_size = st.number_input('Enter the model size (in billions)', value=30, format="%i")

    # Calculate button
    st.form_submit_button('Calculate Training GPUs', on_click=calculate_gpus(tokens, hours, epochs, model_size))

st.markdown('## Inference GPUs')
with st.form(key='gpu_calculator_inference'):

    # Input fields
    throughput = st.number_input('Enter the model throughput (in tokens/sec)', value=30, format="%i")
    qpm = st.number_input('Enter the max number queries per minute', value=10, format="%i")
    output_tokens = st.number_input('Enter the average number of output tokens', value=300, format="%i")

    # Calculate button
    st.form_submit_button('Calculate Inference GPUs', on_click=calculate_gpus_inference(throughput, qpm, output_tokens))

# Put github link at the bottom https://github.com/hunkim/llm_gpt_cal
st.markdown('**Github:** https://github.com/hunkim/llm_gpu_cal')