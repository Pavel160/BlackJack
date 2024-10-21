from dotenv import load_dotenv
import os

load_dotenv()

HEARTS = chr(int(os.getenv('HEARTS')))  # Character 9829 is '♥'.
DIAMONDS = chr(int(os.getenv('DIAMONDS')))  # Character 9830 is '♦'.
SPADES = chr(int(os.getenv('SPADES')))  # Character 9824 is '♠'.
CLUBS = chr(int(os.getenv('CLUBS')))  # Character 9827 is '♣'.
