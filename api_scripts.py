from PIL import Image
import json
import base64

## convert images to json
def image_to_json(image_path):
    try:
        data = {}
        with open(image_path, mode='rb') as file:
            img = file.read()
            data['img'] = base64.encodebytes(img).decode('utf-8')


            return json.dumps(data)
    except Exception as e:
        print("Error:", e)

# Example usage:
image_path = r"D:\pixi_plot\Taj_Mahal_(Edited).jpeg"
# json_data = image_to_json(image_path)
# if json_data:
#     print(json_data)
