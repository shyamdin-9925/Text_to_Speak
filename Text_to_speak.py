import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        text = input("Enter text (or type 'exit' to quit): ")
        if text.lower() == 'exit':
            print("Exiting the program.")
            break
        text_to_speech(text)

if __name__ == "__main__":
    main()
