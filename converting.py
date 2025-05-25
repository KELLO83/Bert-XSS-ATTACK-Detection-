from pptx2md import convert, ConversionConfig
from pathlib import Path

# Basic usage
convert(
    ConversionConfig(
        pptx_path=Path('BERT발표.pptx'),
        output_path=Path('output.md'),
        image_dir=Path('img'),
        disable_notes=True
    )
)

print("Conversion completed successfully!")
# This code converts a PowerPoint file to Markdown format using the pptx2md library.