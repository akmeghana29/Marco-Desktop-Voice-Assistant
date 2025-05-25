from app.marco import speak, takeCommand, wishMe

def run_assistant():
    print("Starting Marco Assistant CLI...")
    wishMe()

    while True:
        speak("Tell me how can I help you?")
        command = takeCommand().lower()

        if command == "none":
            continue

        if "stop" in command:
            speak("Shutting down, have a nice day!")
            print("Assistant stopped.")
            break

        print(f"Received command: {command}")

if __name__ == "__main__":
    run_assistant()
