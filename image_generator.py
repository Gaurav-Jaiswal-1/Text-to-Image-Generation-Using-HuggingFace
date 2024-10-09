import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
import gradio as gr
from pretrained_model import pipe, prompt


# Load the model using Hugging Face Diffusers
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    use_auth_token=True
).to("cuda")

# Define the image generation function
def generate_image(prompt):
    with autocast("cuda"):
        image = pipe(prompt)["images"][0]  # Generate image from prompt
    return image

# Create the Gradio interface
interface = gr.Interface(
    fn=generate_image,             # Function to call
    inputs="text",                 # Input type (text prompt)
    outputs="image",               # Output type (generated image)
    title="Stable Diffusion Image Generator",   # Title for the interface
    description="Enter a text prompt and generate an image using Stable Diffusion."
)

# Launch the Gradio app
interface.launch()
