from pyfiglet import figlet_format
import os


from menu import menu
from edit import create_custom_card

CARD_VALUES = [
    #"1M",
    "2M",
    "3M",
    "4M",
    "5M",
    "10M",
    #"WILD CARD",
]

TITLE = figlet_format("MONOPOLY DEAL CARD CREATOR", font="3d-ascii", width=150, justify="center")

title = lambda : (os.system("clear"), print(TITLE))

def get_input() -> tuple[int, str, str]:
    
    value = menu(f"{TITLE}\n\nSelect The Value Of The Card", CARD_VALUES, 'cyan')
    
    name = input("Enter the name of the card: ")
    title()
    
    description = input("Enter the description of the card: ")
    title()
    if name == "" or description == "":
        raise ValueError("Name and description cannot be empty")

    if len(name) > 25:
        raise ValueError("Name cannot be longer than 25 characters")
    if len(description) > 100:
        raise ValueError("Description cannot be longer than 100 characters")

    return value, name, description

def main():
    title()
    card_value, card_name, card_description = get_input()
    print(f"Card Value: {CARD_VALUES[card_value]}")
    print(f"Card Name: {card_name}")
    print(f"Card Description: {card_description}")

    title()
    create_custom_card(CARD_VALUES[card_value], card_name, card_description)
    
    
main()