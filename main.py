import speech_recognition as sr
from gtts import gTTS
import google.generativeai as genai
import pygame as pg
API="Your_API_Key"
genai.configure(api_key=API)

pg.mixer.init()

def listen_part():
    recognizer=sr.Recognizer()
    with sr.Microphone() as Source:
        text=None   
        try:
            print("Speak.. (CTRL+C to exit )")
            audio=recognizer.listen(Source)
            text=recognizer.recognize_google(audio)
            print(f"You said:{text}")
            model=genai.GenerativeModel("gemini-1.5-flash")
            response=model.generate_content(text)
            a = response.text            
            print(f"Gemini:{a if response else 'No response from Gemini.'}")        
            tts_fr = gTTS(a, lang='fr',slow=False)
            tts_fr.save("GG.mp3")
            
            pg.mixer.music.load("GG.mp3")
            pg.mixer.music.set_volume(1.0)  
            pg.mixer.music.play()

            while pg.mixer.music.get_busy():
                    # pg.time.Clock().tick(10) 
                '''uncomment above  if trash pc'''
                    pass

            pg.mixer.quit()                
    
        except sr.RequestError:
            print("Maintenance")
        except Exception as e:
            print("error(cooked fr)",e)


while True :
    listen_part()
