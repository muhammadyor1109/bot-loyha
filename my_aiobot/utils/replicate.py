import replicate
import os
from config import REPLICATE_API_TOKEN

os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

async def generate_image(prompt):
    output = replicate.run(
        "stability-ai/stable-diffusion:db21e45b",
        input={"prompt": prompt}
    )
    return output[0]
