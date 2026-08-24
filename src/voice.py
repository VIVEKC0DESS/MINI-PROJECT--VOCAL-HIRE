import speech_recognition as sr

def test_microphone():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Hardware verified. Calibrating for background noise... please wait 2 seconds.")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        
        print("\nSUCCESS! The microphone is live.")
        print("Say something like 'Hello Interviewer'...")
        
        try:
            # Listen for up to 5 seconds
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("\nProcessing audio...")
            
            # Send to Google's free API
            text = recognizer.recognize_google(audio)
            print(f"I heard you say: '{text}'")
            
        except sr.WaitTimeoutError:
            print("Error: You didn't speak in time.")
        except sr.UnknownValueError:
            print("Error: I heard noise, but couldn't understand the words.")
        except sr.RequestError as e:
            print(f"Error: Could not reach Google's servers; {e}")

if __name__ == "__main__":
    test_microphone()