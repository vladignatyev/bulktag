# Bulk image tagging using OpenAI GPT-4 Vision
This script helps you prepare your photo and raster illustration artworks for uploading to image stocks.
Script reads every image in directory provided and generate description and keywords for every picture using GPT-4 Vision. 

## Demo
[![Watch the video](https://img.youtube.com/vi/tqLcjiP0Lyc/maxresdefault.jpg)](https://youtu.be/tqLcjiP0Lyc)

## Installation
> This project uses `poetry` for dependency management. [Install Poetry](https://python-poetry.org/docs/) before proceeding to next steps.

1. Clone this repository
2. Run `poetry install`

## Usage
To generate description and keywords and save as `output.csv`:
```bash 
poetry run python keywords.py /path/to/directory/containing/images --openai YOUR_API_KEY
```

For more information:
```bash
poetry run python keywords.py
```

## Features

- Bulk generate description and keywords (tags) best describing picture style, atmosphere, colours and objects
- [ShutterStock CSV support](https://submit.shutterstock.com/upload/footage/csv?language=en)
- Beautiful progress bar and colorful logging using [rich](https://github.com/Textualize/rich)
- Uses the cutting-edge GPT-4 Vision model `gpt-4-vision-preview`
- Supported file formats are the same as GPT-4 Vision support: JPEG, WEBP, PNG
- Budget per image: ~65 tokens
- Provide OpenAI API Key either as environmental variable or argument
- Bulk add categories
- Bulk mark the content as mature (default: No)
- Bulk mark the content as editorial (default: No)

## Contributing
Add an issue or open a pull request on GitHub.
This software is maintained by [Vladimir Ignatev](https://github.com/vladignatyev).
