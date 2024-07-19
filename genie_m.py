import pyttsx3
import speech_recognition
import os
import requests
from bs4 import BeautifulSoup
import datetime
import pyautogui
import random
import webbrowser



from email.mime.text import MIMEText
from google.oauth2 import service_account
import google.auth.transport.requests
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os
import base64
from google.oauth2 import service_account
from email.mime.multipart import MIMEMultipart
import pickle
 



import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage





engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 150
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

if __name__ == "__main__":
    while True:

        #query = takeCommand().lower()
        
        #speak("Enter password to start")

        #pw_file = open("password.txt","r")
        #pw = pw_file.read()
        #pw_file.close()
        #query = takeCommand().lower()
        #if (query==pw):
            #print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
            #break
        #elif (i==2 and query!=pw):
            #exit()

        #elif (query!=pw):
                #print("Try Again")


        query = takeCommand().lower()
        if "khul ja sim sim" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok maam , You can me call anytime")
                    break 
                elif "hello" in query:
                    speak("Hello maam, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, maam")
                elif "thank you" in query:
                    speak("you are welcome, maam")
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
               
                elif "temperature" in query:
                    search = "temperature in bangalore"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
               
                elif "weather" in query:
                    search = "temperature in bangalore"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")

                elif "finally sleep" in query:
                    speak("Going to sleep,maam")
                    exit()

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,maam")

                elif "amazon" in query:
                    from SearchNow import searchAmazon
                    searchAmazon(query)

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,maam")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, maam")
                    volumedown()

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me "+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me" + remember.read())

                #elif "tired" in query:
                    #speak("Playing your favourite songs, sir")
                    #a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                    #b = random.choice(a)
                    #if b==1:
                        #webbrowser.open(https://music.youtube.com/watch?v=T5RFL9NMQJI&list=RDAMVM8PTOkwze0Vw)
                    #if b==2:
                        #webbrowser.open(https://music.youtube.com/watch?v=Cb6wuzOurPc)
                    #elif b==3:
                        #webbrowser.open(https://music.youtube.com/watch?v=k3g_WjLCsXM)
                                        

                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    #shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if "shutdown" in query:
                        os.system("shutdown /s /t 1")

                    elif "no" in query:
                        break  

                
                elif "screenshot" in query:
                    import pyautogui #pip install pyautogui
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")





                elif "email" in query:
                    SCOPES = ['https://www.googleapis.com/auth/gmail.send']

    # Initialize the recognizer and text-to-speech engine
                    listener = sr.Recognizer()
                    engine = pyttsx3.init()

                    def talk(text):
                        engine.say(text)
                        engine.runAndWait()

                    def get_info():
                        try:
                            with sr.Microphone() as source:
                                print('Listening...')
                                voice = listener.listen(source)
                                info = listener.recognize_google(voice)
                                print(info)
                                return info.lower() if info else None
                        except Exception as e:
                            print(f"Error: {e}")
                            return None

                    def authenticate_gmail():
                        creds = None
                        if os.path.exists('token.pickle'):
                            with open('token.pickle', 'rb') as token:
                                creds = pickle.load(token)

                        if isinstance(creds, Credentials) and creds.valid:
                            service = build('gmail', 'v1', credentials=creds)
                            return service
                        else:
                            flow = InstalledAppFlow.from_client_secrets_file(
                            'aanchalstinge28@gmail.com.json', SCOPES)
                            creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
                            with open('token.pickle', 'wb') as token:
                                pickle.dump(creds, token)

                            service = build('gmail', 'v1', credentials=creds)
                            return service

                    def create_message(sender, to, subject, message_text):
                        """Create a message for an email."""
                        message = MIMEText(message_text)
                        message['to'] = to
                        message['from'] = sender
                        message['subject'] = subject
                        return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

                    def send_message(service, user_id, message):
                        """Send an email message."""
                        try:
                            sent_message = (service.users().messages().send(userId=user_id, body=message).execute())
                            print('Message Id: %s' % sent_message['id'])
                            return sent_message
                        except Exception as error:
                            print(f'An error occurred: {error}')
                            return None

                    email_list = {
                        'ananya': 'ananyasaumya16@gmail.com',
                        'aanchal': 'taanchal03@gmail.com',
                    }

                    def get_email_info():
                        talk('Hi Sir, I am your assistant for today. To whom do you want to send an email?')
                        name = get_info()
                        if name in email_list:
                            receiver = email_list[name]
                            print(receiver)
                            talk('What is the subject of your email?')
                            subject = get_info()
                            talk('Tell me the text in your email.')
                            message = get_info()
                        if subject and message:
                            service = authenticate_gmail()
                            email_message = create_message('aanchalstinge28@gmail.com', receiver, subject, message)
                            send_message(service, 'me', email_message)
                            talk('Thank you, Sir. Your email has been sent.')
                            talk('Do you want to send more emails?')
                            send_more = get_info()
                            if 'yes' in send_more:
                                get_email_info()
                            else:
                                talk("The subject or message was not recognized. Email not sent.")
                        else:
                            talk("I couldn't find the email address for that name. Please try again.")

                    if __name__ == "__main__":
                        get_email_info()

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()


              #  elif "change password" in query:
              #      speak("What's the new password")
               #     new_pw = input("Enter the new password\n")
               #     new_password = open("password.txt","w")
               #     new_password.write(new_pw)
               #     new_password.close()
                #    speak("Done sir")
               # speak(f"Your new password is{new_pw}")

                


                


               