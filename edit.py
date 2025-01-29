from turtle import position
from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm


# CORDS= (min_x, max_x), (min_y, max_y)
ACTION_CARD_TITLE_CORDS = (500, 1300), (500, 800)
CARD_NAME_CORDS = (500, 1300), (1100, 2000)
CARD_DESCRIPTION_CORDS = (300, 1450), (2200, 2500)
PLAY_IN_CENTER_CORDS = (500, 1300), (2600, 2700)

CARD_PATHS = {
    #"1M": "templates/Action Card Template 1Mil.png",
    "2M": "templates/Action Card Template 2Mil.png",
    "3M": "templates/Action Card Template 3Mil.png",
    "4M": "templates/Action Card Template 4Mil.png",
    "5M": "templates/Action Card Template 5Mil.png",
    "10M": "templates/Action Card Template 10Mil.png",
    #"WILD CARD": "templates/Wild Card Template.png",
}

def get_center(cords:tuple[tuple[int, int], tuple[int, int]]) -> tuple[int, int, int, int]:
    """
    Returns
    Center_x, Center_y, Width, Height
    """
    min_x = cords[0][0]
    max_x = cords[0][1]
    min_y = cords[1][0]
    max_y = cords[1][1]
    return (min_x + max_x) // 2, (min_y + max_y) // 2, max_x - min_x, max_y - min_y

def action_card_title(draw:ImageDraw.ImageDraw, font:ImageFont.ImageFont):
    center_x, center_y, width, height = get_center(ACTION_CARD_TITLE_CORDS)
    
    bbox = draw.textbbox((center_x, center_y), "ACTION CARD", font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = (center_x - text_width // 2, center_y - text_height // 2)
    draw.text(position, "ACTION CARD", font=font, fill="black")
    
def card_name(draw:ImageDraw.ImageDraw, font:ImageFont.ImageFont, name:str):
    center_x, center_y, width, height = get_center(CARD_NAME_CORDS)
    
    bbox = draw.textbbox((center_x, center_y), name, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = (center_x - text_width // 2, center_y - text_height // 2)
    draw.text(position, name, font=font, fill="black")

def card_description(draw:ImageDraw.ImageDraw, font:ImageFont.ImageFont, description:str):
    center_x, center_y, width, height = get_center(CARD_DESCRIPTION_CORDS)
    
    bbox = draw.textbbox((center_x, center_y), description, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = (center_x - text_width // 2, center_y - text_height // 2)
    draw.text(position, description, font=font, fill="black")

def play_in_center(draw:ImageDraw.ImageDraw, font:ImageFont.ImageFont):
    center_x, center_y, width, height = get_center(PLAY_IN_CENTER_CORDS)
    
    bbox = draw.textbbox((center_x, center_y), "(play in center to use)", font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = (center_x - text_width // 2, center_y - text_height // 2)
    draw.text(position, "(play in center to use)", font=font, fill="black")

def create_custom_card(value:str, title:str, description:str):
    load = tqdm(total=100, desc="Creating Card", position=0, leave=False)
    path = CARD_PATHS[value]
    card = Image.open(path)
    
    draw = ImageDraw.Draw(card)
    
    font = ImageFont.load_default()
    
    action_card_title(draw, font)
    card_name(draw, font, title)
    card_description(draw, font, description)
    play_in_center(draw, font)

    
    card.save(f"cards/{title}.png")