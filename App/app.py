import gradio as gr
import numpy as np
import pickle

# Load the saved model
loaded_model = pickle.load(open('sonar_model.pkl', 'rb'))

# Prediction function
def sonar_prediction(input_data):

    # Convert input string into list of float values
    input_data = [float(x) for x in input_data.split(',')]

    # Convert into numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Prediction
    prediction = loaded_model.predict(input_data_reshaped)

    # Output
    if prediction[0] == 'R':
        return "The Object is a Rock"
    else:
        return "The Object is a Mine"


# Gradio Interface
interface = gr.Interface(
    fn=sonar_prediction,
    inputs=gr.Textbox(
        lines=4,
        placeholder="Enter 60 comma-separated sonar values",
        label="Sonar Input Values"
    ),
    outputs=gr.Textbox(label="Prediction Result"),
    title="Sonar Rock vs Mine Prediction",
    description="Enter 60 sonar values separated by commas to predict whether the object is a Rock or Mine."
)

# Launch app
interface.launch()
