# **Text-to-Image Generation Using Hugging Face**

## **Project Overview**

This project demonstrates how to generate images from text descriptions using pre-trained models available on Hugging Face’s `transformers` and `diffusers` libraries. The model takes a simple text prompt as input and generates a corresponding image using a diffusion-based generative model.

## **Features**

- **Text Input**: Provide a descriptive text prompt.
- **Image Output**: Model generates an image based on the given text.
- **Customizable**: Users can tweak model parameters and text prompts for varied results.
- **Uses Hugging Face Models**: Pre-trained models for quick and accurate results.

## **Installation**

### **Prerequisites**

- Python 3.x
- Hugging Face `transformers` and `diffusers` libraries
- PyTorch (or TensorFlow, depending on your setup)

### **Install Dependencies**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Text-to-Image-Generation-HuggingFace.git
   cd Text-to-Image-Generation-HuggingFace
   ```

2. Install the required libraries:
   ```bash
   pip install transformers diffusers torch
   ```

## **Usage**

1. **Load the Pre-trained Model:**

   You can use the following script to load the text-to-image model and generate an image from a text prompt.

   ```python
   from transformers import pipeline

   # Load the pre-trained model
   model = pipeline("text-to-image-generation")

   # Provide the text prompt
   text_prompt = "A futuristic city skyline at sunset"
   
   # Generate the image
   images = model(text_prompt)

   # Save the output image
   images[0].save("output_image.png")
   ```

2. **Run the script:**

   ```bash
   python generate_image.py
   ```

3. **View the Generated Image:**
   Once the script finishes, the generated image will be saved as `output_image.png` in your project directory.

## **Sample Outputs**

**A dog plaing with a ball**


![pretrained model's dog img](https://github.com/user-attachments/assets/054b8121-cbaa-4f0f-92c5-738681b76b00)


_This is an example image generated from the prompt: **"A futuristic city skyline at sunset"**._

![Futuristic city](https://github.com/user-attachments/assets/e7dfb34b-f792-435c-9d10-4e95e2b261b8)

## **Model Customization**

You can customize the following aspects of the generation process:

- **Text Prompt**: Adjust the input text for varied outputs.
- **Model Parameters**: Modify generation parameters like the number of diffusion steps, or load different models from Hugging Face.
  
To experiment with different pre-trained models, simply change the model name in the `pipeline()` call.

```python
model = pipeline("text-to-image-generation", model="CompVis/stable-diffusion-v1-4")
```

## **Note-**

If you're using this repo then make sure that you're using in it google colab. Combine both the files and use it in colab


## **References**

- Hugging Face Diffusers: [https://huggingface.co/docs/diffusers](https://huggingface.co/docs/diffusers)
- Hugging Face Transformers: [https://huggingface.co/docs/transformers](https://huggingface.co/docs/transformers)

## **Contributions**

Feel free to open issues or submit pull requests for improvements!

---

### **License**

This project is licensed under the MIT License.

---

This README provides a comprehensive guide to understanding and using your text-to-image generation project. You can replace the sample output with an actual generated image from your project for GitHub!
