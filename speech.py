#import library
import speech_recognition as sr

# Initialize recognizer class for recognizing the speech
R = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable

with sr.AudioFile('I-dont-know.wav') as source:
    
    audiotext = R.listen(source)
    
# recoginize_() method
    try:
        
        # using google speech recognition
        text = R.recognize_google(audiotext)
        print('Convert audio into text ...')
        print(text)
     
    except:
         print('run again...')
