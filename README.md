# Bulk image tagging using OpenAI GPT-4 Vision
This script helps you prepare your photos and raster illustration artworks for uploading to image stocks.

The script reads every image in the directory provided and generates descriptions and keywords for each picture using GPT-4 Vision. 

## Demo
[Click to watch!](https://youtu.be/tqLcjiP0Lyc)
[![Watch the video](https://img.youtube.com/vi/tqLcjiP0Lyc/maxresdefault.jpg)](https://youtu.be/tqLcjiP0Lyc)

## Installation
> This project uses `poetry` for the dependency management. [Install Poetry](https://python-poetry.org/docs/) before you proceed to the next steps.

1. Clone this repository
2. Run `poetry install`

## Usage
Generate descriptions and keywords for each image in the directory and then save the output as `output.csv`:
```bash 
poetry run python keywords.py /path/to/directory/containing/images --openai YOUR_API_KEY
```

More information:
```bash
poetry run python keywords.py
```

## Features

- Bulk generate descriptions and keywords (tags) that best describe the picture's style, atmosphere, colors and objects
- [Shutterstock CSV support](https://submit.shutterstock.com/upload/footage/csv?language=en)
- Beautiful progress bar and colorful logging using [Rich](https://github.com/Textualize/rich)
- Uses the cutting-edge GPT-4 Vision model `gpt-4-vision-preview`
- Supported file formats are the same as those GPT-4 Vision supports: JPEG, WEBP, PNG
- Budget per image: ~65 tokens
- Provide the OpenAI API Key either as an environment variable or an argument
- Bulk add categories
- Bulk mark the content as mature (default: No)
- Bulk mark the content as editorial (default: No)

## Contributing
Add an issue or open a pull request on GitHub.
This software is maintained by [Vladimir Ignatev](https://github.com/vladignatyev).
