import os
import requests
import threading




from googletrans import Translator





def translate_text(text, source_lang, target_lang):
    translator = Translator()
    text_to_translate = text
    translation = translator.translate(text_to_translate, src='en', dest='mr')
    print(text_to_translate)
    return translation.text

# Function to read lines from a file
def read_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

# Function to write lines to a file
def write_lines(filename, lines):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)

# Function to translate lines and write to a file
def translate_and_write(input_filename, output_filename, source_lang, target_lang):
    lines = read_lines(input_filename)
    translated_lines = [translate_text(line.strip(), source_lang, target_lang) + '\n' for line in lines]
    write_lines(output_filename, translated_lines)
    print(f"Translation of {input_filename} is saved in {output_filename}")

# List of input file names (change these to your actual file names)
file_names = ["t3.txt", "t4.txt", "t5.txt", "t6.txt"]

source_lang = "en"  # Assuming files are in English
target_lang = "mr"   # Marathi language code

# Create threads for each file translation
threads = []
for filename in file_names:
    output_filename = os.path.splitext(filename)[0] + "_translated.txt"
    thread = threading.Thread(target=translate_and_write, args=(filename, output_filename, source_lang, target_lang))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All translations completed.")
