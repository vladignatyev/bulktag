from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn
from rich.console import Console

import time

from keywords import list_files_in_directory

files = list_files_in_directory('/home/vaurum/Downloads/Shutter/jpeg/')

console = Console()

with Progress(
    SpinnerColumn(),
    *Progress.get_default_columns(),
    TimeElapsedColumn(),
    console=console,
    transient=True,
) as progress:
    console_task = progress.add_task("[bold white]Downloading", total=len(files))

    for i, file_info in enumerate(files):
        file_path, file_name = file_info
        progress.log("Requesting AI...")
        time.sleep(0.1)
        json_text = {
            'keywords': 'Christmas tree, oranges, cinnamon sticks, star anise, gingerbread star, fir branches, pine cones, gold baubles, white background, holiday season, festive, warm colors, brown, orange, gold, Christmas, New Year, decorating, winter holidays, cozy, traditional holiday spices, aromatherapy, crafting, natural elements, food photography, top view',
            'description': 'A festive composition with a Christmas tree made of oranges, cinnamon, and star anise on a white background, ideal for holiday designs.'
        }
        keywords = json_text['keywords']
        description = json_text['description']
        
        progress.log(f"Working on file #{file_path}")
        progress.update(console_task, advance=1)

        # table.add_row(file_path, description, keywords)