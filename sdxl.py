# import torch
# from diffusers import StableDiffusionXLPipeline, UNet2DConditionModel, EulerDiscreteScheduler
# from safetensors.torch import load_file
# import json
# import wget
# import subprocess


# def initiate_sdxl():
#     url = 'https://huggingface.co/ByteDance/SDXL-Lightning/resolve/main/sdxl_lightning_2step_unet.safetensors'
#     #!wget https://huggingface.co/ByteDance/SDXL-Lightning/resolve/main/sdxl_lightning_2step_unet.safetensors

#     model = wget.download(url)
#     model_id = "stabilityai/stable-diffusion-xl-base-1.0"

#     # Load model
#     unet = UNet2DConditionModel.from_config(model_id, subfolder="unet").to("cuda", torch.float16)

#     unet.load_state_dict(load_file("sdxl_lightning_2step_unet.safetensors", device="cuda"))

#     pipe = StableDiffusionXLPipeline.from_pretrained(model_id,
#                                                  unet=unet,
#                                                  torch_dtype=torch.float16,
#                                                  variant="fp16").to("cuda")
#     # Ensure sampler uses "trailing" timesteps
#     pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config, timestep_spacing="trailing")

#     return pipe

# def gen_image(prompt,pipe):
#     prompt = prompt

#     image = pipe(prompt,
#              num_inference_steps=2,
#              width = 512,
#              height = 512,
#              guidance_scale=0).images[0]

#     return image



import os
import base64
import requests
def clean_input(text):
    # text = """["\n            1. Tom lives with Aunt Polly after parents' death.\n            2. Tom doesn't like school or work, prefers play and adventure.\n 
    #        3. Aunt Polly angry, assigns fence painting as punishment, later allows others to join in for food."]"""
    prompts = text.split('\n')
    text_prompts_cleaned = []
    for i in prompts:
        j = i.strip()
        if len(j) > 5:
            text_prompts_cleaned.append(j)
        else:
            continue
        

    print(text_prompts_cleaned)
    # return text_prompts_cleaned
    generate_images_from_text_prompts(text_prompts_cleaned)


def generate_images_from_text_prompts(text_prompts_list):
    engine_id = "stable-diffusion-v1-6"
    api_host = os.getenv('API_HOST', 'https://api.stability.ai')
    api_key = 'sk-pfQyjo3qsZYXJPCGFO5zFHz8rhkvTHYsuxXmrGCTcNykYTuo '

    if api_key is None:
        raise Exception("Missing Stability API key.")
    os.makedirs("out", exist_ok=True)
    for i, text_prompt in enumerate(text_prompts_list):
        response = requests.post(
            f"{api_host}/v1/generation/{engine_id}/text-to-image",
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer {api_key}"
            },
            json={
                "text_prompts": [
                    {
                        "text": text_prompt
                    }
                ],
                "cfg_scale": 7,
                "height": 512,
                "width": 512,
                "samples": 1,
                "steps": 30,
            },
        )

        if response.status_code != 200:
            raise Exception(f"Non-200 response for prompt {i}: " + str(response.text))

        data = response.json()

        for j, image in enumerate(data["artifacts"]):
            with open(f"./out/v1_txt2img_{i}_{j}.png", "wb") as f:
                f.write(base64.b64decode(image["base64"]))

# Example usage:
text_prompts = [" Tom, a mischievous young boy, longs for adventure and avoids school."," Tom is tasked with painting a fence as punishment, but he tries to find ways to avoid it"," Tom's relationships with his friends are established, showcasing his social skills."]
generate_images_from_text_prompts(text_prompts)

