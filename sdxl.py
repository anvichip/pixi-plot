import torch
from diffusers import StableDiffusionXLPipeline, UNet2DConditionModel, EulerDiscreteScheduler
from safetensors.torch import load_file
import json
import wget
import subprocess


def initiate_sdxl():
    url = 'https://huggingface.co/ByteDance/SDXL-Lightning/resolve/main/sdxl_lightning_2step_unet.safetensors'
    #!wget https://huggingface.co/ByteDance/SDXL-Lightning/resolve/main/sdxl_lightning_2step_unet.safetensors

    model = wget.download(url)
    model_id = "stabilityai/stable-diffusion-xl-base-1.0"

    # Load model
    unet = UNet2DConditionModel.from_config(model_id, subfolder="unet").to("cuda", torch.float16)

    unet.load_state_dict(load_file("sdxl_lightning_2step_unet.safetensors", device="cuda"))

    pipe = StableDiffusionXLPipeline.from_pretrained(model_id,
                                                 unet=unet,
                                                 torch_dtype=torch.float16,
                                                 variant="fp16").to("cuda")
    # Ensure sampler uses "trailing" timesteps
    pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config, timestep_spacing="trailing")

    return pipe

def gen_image(prompt,pipe):
    prompt = prompt

    image = pipe(prompt,
             num_inference_steps=2,
             width = 512,
             height = 512,
             guidance_scale=0).images[0]

    return image
