from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm
import os

# Define coordinates for the areas where text needs to be placed
ACTION_CARD_TITLE_CORDS = (500, 1300), (500, 800)
CARD_NAME_CORDS = (500, 1300), (1100, 2000)
CARD_DESCRIPTION_CORDS = (300, 1450), (2200, 2500)
PLAY_IN_CENTER_CORDS = (500, 1300), (2600, 2700)

# Dictionary to load card templates
CARD_PATHS = {
    "2M": "templates/Action Card Template 2Mil.png",
    "3M": "templates/Action Card Template 3Mil.png",
    "4M": "templates/Action Card Template 4Mil.png",
    "5M": "templates/Action Card Template 5Mil.png",
    "10M": "templates/Action Card Template 10Mil.png",
}

# Check if 'cards/' directory exists, if not, create it
if not os.path.exists('cards'):
    os.makedirs('cards')

# Function to calculate the center of a rectangle defined by four points
def get_center(cords:tuple[tuple[int, int], tuple[int, int]]) -> tuple[int, int, int, int]:
    """
    Returns Center_x, Center_y, Width, Height
    """
    min_x = cords[0][0]
    max_x = cords[0][1]
    min_y = cords[1][0]
    max_y = cords[1][1]
    return (min_x + max_x) // 2, (min_y + max_y) // 2, max_x - min_x, max_y - min_y

# Function to add title text to the image
def action_card_title(draw:ImageDraw.ImageDraw, font:ImageFont.ImageFont):
    center_x, center_y, width, height = get_center(ACTION_CARD_TITLE_CORDS)
    
    # Calculate the text bounding box to center it
    bbox = draw.textbbox((center_x, center_y), "ACTION CARD", font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = (center_x - text_width // 2, center_y - text_height // 2)
    draw.text(position, "ACTION CARD", font=font, fill="black")

# Function to add card name text to the image
def card_name(draw:ImageDraw.ImageDraw, font:ImageFont.ImageFont, name:str):
    center_x, center_y, width, height = get_center(CARD_NAME_CORDS)
    
    bbox = draw.textbbox((center_x, center_y), name, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = (center_x - text_width // 2, center_y - text_height // 2)
    draw.text(position, name, font=font, fill="black")

# Function to add description text to the image
def card_description(draw:ImageDraw.ImageDraw, font:ImageFont.ImageFont, description:str):
    center_x, center_y, width, height = get_center(CARD_DESCRIPTION_CORDS)
    
    bbox = draw.textbbox((center_x, center_y), description, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = (center_x - text_width // 2, center_y - text_height // 2)
    draw.text(position, description, font=font, fill="black")

# Function to add a note at the center of the card
def play_in_center(draw:ImageDraw.ImageDraw, font:ImageFont.ImageFont):
    center_x, center_y, width, height = get_center(PLAY_IN_CENTER_CORDS)
    
    bbox = draw.textbbox((center_x, center_y), "(play in center to use.)", font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = (center_x - text_width // 2, center_y - text_height // 2)
    draw.text(position, "(play in center to use.)", font=font, fill="black")

# Main function to create the custom card
def create_custom_card(value:str, title:str, description:str):
    load = tqdm(total=100, desc="Creating Card", position=0, leave=False)
    path = CARD_PATHS.get(value)
    
    if not path:
        print("Template path is missing.")
        return

    # Try to open the image template
    try:
        card = Image.open(path)
    except FileNotFoundError:
        print(f"Error: Template file '{path}' not found.")
        return
    
    # Ensure that the image mode is RGB so it supports text drawing
    card = card.convert("RGB")
    
    draw = ImageDraw.Draw(card)
    
    # Use a better font (make sure the font file is available)
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        print("Warning: 'arial.ttf' font not found, using default font.")
        font = ImageFont.load_default()
    
    # Add all the texts to the card
    action_card_title(draw, font)
    card_name(draw, font, title)
    card_description(draw, font, description)
    play_in_center(draw, font)
    
    # Save the modified image to the 'cards/' folder
    output_path = f"cards/{title}.png"
    card.save(output_path)
    print(f"Custom card saved to {output_path}")

# Example usage
create_custom_card("2M", "Bankrupt", "Force a player to give you all their properties.")
