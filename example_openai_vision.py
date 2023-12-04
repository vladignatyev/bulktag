import os

from openai import OpenAI

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
import base64


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


image_path = '/home/vaurum/Downloads/newupload/jpeg/stacy404_17288_Christmas_decoration_on_wooden_background_with_c_16306142-05b5-413a-a893-a361ae4bb1ab.jpg'

base64_image = encode_image(image_path)

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Assist me in tagging this image by acting step-by-step. Do not communicate with me except as of instruction below.\n"
                                 "1. Understand what objects are presented on this image.\n"
                                 "2. Understand the style of the composition pictured, the atmosphere, the main colors.\n"
                                 "3. Understand what possible usage could be of this picture and what event or holiday it may help to design for.\n"
                                 "4. Generate the output in a form of JSON containing the following fields: `keywords`, `description`. Put into keywords a comma-separated detailed list of objects, styles, colors, usages, holidays, events, atmosphere of the picture. Put as many keywords into the list as you can. Put into `description` a short description of the picture, including possible usage."
                                 },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}",
            "detail": "low"
          },
        },
      ],
    }
  ],
  max_tokens=800,
)

import json

json_text = json.loads('\n'.join(response.choices[0].message.content.split('\n')[1:-1]))
print(json_text)
import pdb; pdb.set_trace()

