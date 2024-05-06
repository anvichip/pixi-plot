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
from test_modal import call_llm_api
import ast

def clean_input(final_prompts):
    final_prompts_lists = [ast.literal_eval(prompts) for prompts in final_prompts]
    flat_prompts = [item for sublist in final_prompts_lists for item in sublist]
    individual_prompts = [prompt.strip() for sublist in flat_prompts for prompt in sublist.split('\n') if prompt.strip()]
    print("Prompts after cleaning" + str(individual_prompts))

    generate_images_from_text_prompts(individual_prompts)

def generate_images_from_text_prompts(text_prompts_list):
    engine_id = "stable-diffusion-v1-6"
    api_host = os.getenv('API_HOST', 'https://api.stability.ai')
    api_key = 'sk-WYrGN6LYa7ojrivMpdnQv1pK1yc4udgJpmdNe9K8kSz8ZDDh'

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
            file_path = os.path.join("out", f"v1_txt2img_{i}_{j}.png")
            with open(file_path, "wb") as f:
                f.write(base64.b64decode(image["base64"]))


# Example usage:
# text_prompts = [" Tom, a mischievous young boy, longs for adventure and avoids school."," Tom is tasked with painting a fence as punishment, but he tries to find ways to avoid it"," Tom's relationships with his friends are established, showcasing his social skills."]
# final_texts , fnal_panels, final_prompts = call_llm_api(r"D:\deeplearning project\pixi-plot\tom_sawyer-4.pdf")
# print(len(final_prompts))
# print(final_prompts)
# flat_prompts = [item for sublist in final_prompts for item in sublist]
# final_prompts_lists = [ast.literal_eval(prompts) for prompts in final_prompts]
# flat_prompts = [item for sublist in final_prompts_lists for item in sublist]
# individual_prompts = [prompt.strip() for sublist in flat_prompts for prompt in sublist.split('\n') if prompt.strip()]
# final_prompts=['["\\n             Sure, here are the three most important points from Chapter 1 of \\"The Adventures of Tom Sawyer\\":\\n\\n1. Tom Sawyer is punished for not going to school by having to paint a fence.\\n2. Tom\'s friend Jim declines to paint the fence with him.\\n3. Tom trades the task of painting the fence for food and other boys come to watch and offer to paint themselves."]', '["\\n             Sure, here are the three simple prompts for the scene descriptions you provided:\\n\\n1. Tom paints a fence, making it beautiful and white, and his aunt is surprised and happy.\\n2. Tom plays with his friend Joe, highlighting his love for adventure and friendship.\\n3. A new girl moves in with yellow hair and blue eyes, but Tom can\'t talk to her."]', '["\\n            1. Tom runs late due to friend.\\n2. Tom talks to new classmate.\\n3. Tom invites classmate to walk with him."]', '["\\n             Sure, here are the 3 most important points from Chapter 3 of \\"The Adventures of Tom Sawyer\\":\\n\\n1. Tom and Huck witness a crime, but are too afraid to speak up.\\n2. Tom is haunted by his guilt and fear.\\n3. Tom and Huck keep their secret hidden from their friends and family."]', '["\\n             Sure, here is a simple prompt for each scene:\\n\\nScene 1: Three friends run away and feel free.\\n\\nScene 2: Friends cross river and feel happy, decide to stay.\\n\\nScene 3: Friends hear boat noise and become curious."]']
# individual_prompts = ['1. Tom Sawyer is punished for not going to school by having to paint a fence.',
#  "2. Tom's friend Jim declines to paint the fence with him.",
#  '3. Tom trades the task of painting the fence for food and other boys come to watch and offer to paint themselves.',
#  'Sure, here are the three simple prompts for the scene descriptions you provided:',
#  '1. Tom paints a fence, making it beautiful and white, and his aunt is surprised and happy.',
#  '2. Tom plays with his friend Joe, highlighting his love for adventure and friendship.',
#  "3. A new girl moves in with yellow hair and blue eyes, but Tom can't talk to her.",
#  '1. Tom runs late due to friend.',
#  '2. Tom talks to new classmate.',
#  '3. Tom invites classmate to walk with him.',
#  'Sure, here are the 3 most important points from Chapter 3 of "The Adventures of Tom Sawyer":',
#  '1. Tom and Huck witness a crime, but are too afraid to speak up.',
#  '2. Tom is haunted by his guilt and fear.',
#  '3. Tom and Huck keep their secret hidden from their friends and family.',
#  'Sure, here is a simple prompt for each scene:',
#  'Scene 1: Three friends run away and feel free.',
#  'Scene 2: Friends cross river and feel happy, decide to stay.',
#  'Scene 3: Friends hear boat noise and become curious.']

# generate_images_from_text_prompts(individual_prompts)
# clean_input(final_prompts)

