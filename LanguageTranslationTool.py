from googletrans import Translator, LANGUAGES

def language_translation_tool(text, dest_language):
    translator = Translator()
    
    translated = translator.translate(text, dest=dest_language)
    return translated.text
    

def main():
    untranslated_text = input("Enter text: ")
    
    print("Choose a language you want to translate to:")
    print(', '.join(f'{k}:{v}' for k, v in LANGUAGES.items()))
    target_language = input()

    while target_language not in LANGUAGES:
        print("Invalid language code. Please try again.")
        print("Choose a language you want to translate to:")
        target_language = input()

    translated_text = language_translation_tool(untranslated_text, target_language)
    print("Translated text: " + translated_text)
   

if __name__ == "__main__":
    main()
