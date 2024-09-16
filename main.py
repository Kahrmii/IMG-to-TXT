import pytesseract
from PIL import ImageGrab, Image
import pyperclip
import keyboard
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\a.frost\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

keyboard.send('windows+shift+s')
time.sleep(5)
    
def extract_text_from_clipboard():
    image = ImageGrab.grabclipboard()
    
    if image is None:
        raise ValueError("img not found")
    
    image = image.convert('L') # convert to grayscale
    
    initial_text = pytesseract.image_to_string(image)
    
    language = detect_language(initial_text)

    text = pytesseract.image_to_string(image, lang=language)
    return text

def detect_language(text):
    german_words = ["der", "und", "in", "den", "von", "zu", "das", "mit", "sich",
    "des", "auf", "für", "ist", "im", "dem", "nicht", "ein", "eine",
    "als", "auch", "es", "an", "werden", "aus", "er", "hat", "dass", "sie",
    "nach", "wird", "bei", "einer", "Der", "um", "am", "sind", "noch", "wie",
    "einem", "über", "einen", "Das", "so", "Sie", "zum", "war", "haben", "nur",
    "oder", "aber", "vor", "zur", "bis", "mehr", "durch", "man", "sein", "wurde",
    "sei", "In", "Prozent", "hatte", "kann", "gegen", "vom", "können", "schon", "wenn",
    "habe", "seine", "Mark", "ihre", "dann", "unter", "wir", "soll", "ich", "eines",
    "Es", "Jahr", "zwei", "Jahren", "diese", "dieser", "wieder", "keine", "Uhr", "seiner",
    "worden", "Und", "will", "zwischen", "Im", "immer", "Millionen", "Ein", "was", "sagte"]
    
    english_words = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
    "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
    "or", "an", "will", "my", "one", "all", "would", "there", "their", "what",
    "so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
    "when", "make", "can", "like", "time", "no", "just", "him", "know", "take",
    "people", "into", "year", "your", "good", "some", "could", "them", "see", "other",
    "than", "then", "now", "look", "only", "come", "its", "over", "think", "also",
    "back", "after", "use", "two", "how", "our", "work", "first", "well", "way",
    "even", "new", "want", "because", "any", "these", "give", "day", "most", "us"]

    german_count = sum(word in text for word in german_words)
    english_count = sum(word in text for word in english_words)

    if german_count > english_count:
        return 'deu'
    else:
        return 'eng'
    
def copy_text_to_clipboard(text):
    pyperclip.copy(text)

text = extract_text_from_clipboard()
copy_text_to_clipboard(text)