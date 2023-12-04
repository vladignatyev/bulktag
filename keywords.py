#!/env/bin/python

import os
import sys
import json
import base64

import pandas as pd

from argparse import ArgumentParser

from openai import OpenAI

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn



def encode_image(image_path):
    """Encodes file contents as Base64"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def list_files_in_directory(path):
    """Lists files in the given directory and returns a list of filenames and their sizes."""
    files_data = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            # size = os.path.getsize(file_path)
            file_name = os.path.basename(file_path)
            if file_name.lower().endswith('.jpeg') or file_name.lower().endswith('.jpg'):
                files_data.append([file_path, file_name])
    return files_data


def write_to_csv(data, filename):
    """Writes the data to a CSV file."""
    df = pd.DataFrame(data, columns=['Filename', 'Description', 'Keywords', 'Categories', 'Mature content', 'Editorial'])
    df.to_csv(filename, index=False)


def generate_tags(client, image_path):
    """Requests OpenAI Vision API for generating tags and descriptions."""
    encoded_image = encode_image(image_path)

    user_prompt = "Assist me in tagging this image by acting step-by-step. Do not communicate with me except as of instruction below.\n" \
                  "1. Understand what objects are presented on this image.\n" \
                  "2. Understand the style of the composition pictured, the atmosphere, the main colors.\n" \
                  "3. Understand what possible usage could be of this picture and what event or holiday it may help to design for.\n" \
                  "4. Generate the output in a form of JSON containing the following fields: `keywords`, `description`. " \
                  "Put into keywords a comma-separated detailed list of objects, styles, colors, usages, holidays, events, " \
                  "atmosphere of the picture. Put as many keywords into the list as you can. Put into `description` " \
                  "a short description of the picture at most 200 characters long, including possible usage. " \
                  "Do not include introductory words and avoid enumerations."

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
            "role": "user",
            "content": [
                {"type": "text", "text": user_prompt},
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{encoded_image}",
                    "detail": "low"
                },
                },
            ],
            }
        ],
        max_tokens=800,
    )
    return json.loads('\n'.join(response.choices[0].message.content.split('\n')[1:-1]))


def get_args():
    """Parses and returns command-line arguments."""
    parser = ArgumentParser(description="List files in a directory and output to a CSV file.")
    parser.add_argument("path", type=str, help="Directory path to list files from")
    parser.add_argument("--file", type=str, default="output.csv", help="Output CSV file name")
    parser.add_argument("--openai", type=str, default="", help="OpenAI API key")
    

    parser.add_argument("--mature", type=str, default="No", help="Is it a mature content? Yes or No")
    parser.add_argument("--editorial", type=str, default="No", help="Is it an editorial content? Yes or No")
    parser.add_argument("--categories", type=str, default="Holidays,Backgrounds/Textures", help="One or two categories separated by commas in English as stated on https://submit.shutterstock.com/upload/footage/csv?language=en")
    
    return parser.parse_args()


def main():
    args = get_args()
    console = Console()
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY', args.openai))

    if not os.path.isdir(args.path):
        console.log("[bold red]The specified path is not a directory.[/bold red]")
        sys.exit(1)

    mature, editorial, categories = args.mature, args.editorial, args.categories

    files = list_files_in_directory(args.path)

    output_data = []

    with Progress(
        SpinnerColumn(),
        *Progress.get_default_columns(),
        TimeElapsedColumn(),
        console=console,
        transient=True,
    ) as progress:
        console_task = progress.add_task("[bold white] Processing images", total=len(files))

        for file_path, file_name in files:
            progress.update(console_task, advance=0)
            progress.log(f"[bold white]File:[/bold white] [cyan]{file_path}[/cyan]\n")

            json_from_ai = generate_tags(client, file_path)
            keywords, description = json_from_ai['keywords'], json_from_ai['description']
            
            progress.log(f"\r\r[bold white]Description[/bold white]: [cyan]{description}[/cyan]\n")
            progress.log(f"[bold white]Tags[/bold white]: [cyan]{keywords}[/cyan]\n")
            
            output_data += [[file_name, description, keywords, categories, mature, editorial]]

            progress.update(console_task, advance=1)
            write_to_csv(output_data, args.file)

        progress.log(":thumbs_up: Well done.")
        progress.log(f"[bold white]Saved to:[/bold white] [cyan]{args.file}[/cyan]\n")


if __name__ == "__main__":
    main()
