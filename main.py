from googletrans import Translator

def text_translator(text='Hello friend ', src='en', dest='ru'):
    try:
        translator = Translator()
        translator = translator.translate(text=text, src=src , dest=dest)

        return translator.text
    except Exception as ex:
        return ex
    
def main():
    print(text_translator(text='Hello', src='en', dest='uz'))

if __name__ =='__main__':
    main()