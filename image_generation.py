import os

from huggingface_hub import InferenceClient

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"]
)

prompt = "Create the most beautiful image of a dog"

image = client.text_to_image(
    prompt=prompt,
    model="black-forest-labs/FLUX.1-Krea-dev"
)

image.save("generated_image.png")

print("Image generated successfully!")