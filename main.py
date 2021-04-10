import speech_recognition as sr
import webbrowser as wb



r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()


# getting the options
with sr.Microphone() as source:
    print('google or youtube')
    print('speak')
    audio = r1.listen(source)
    print(r2.recognize_google(audio))

#if bith "google" and "YouTube" are present in your spoken word , priority is given to Google

# executed if "Google" exists in your spoken words
if 'Google' in r2.recognize_google(audio):
    with sr.Microphone() as source:
        print('enter query')
        wb.get().open_new('www.google.com/search?q='+(r2.recognize_google(r2.listen(source))))

#executed if "YouTube" exists in your open words
elif 'YouTube' in r2.recognize_google(audio):
    #print('youtube!!!!!!!!!!!'+r2.recognize_google(audio))
    with sr.Microphone() as source:
        print('enter query')
        wb.get().open_new('www.YouTube.com/results?search_query='+(r2.recognize_google(r2.listen(source))))


    #print('youtube!!!!!!!!!!!'+r2.recognize_google(audio)