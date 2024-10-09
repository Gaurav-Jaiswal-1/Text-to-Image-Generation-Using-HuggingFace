# make sure you're logged in with `huggingface-cli login`
from torch import autocast
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained(
	"CompVis/stable-diffusion-v1-4",
	use_auth_token=True
).to("cuda")

prompt = "man propose to there wife"
with autocast("cuda"):
    image = pipe(prompt)["images"][0]

image.save("man_wife.png")

