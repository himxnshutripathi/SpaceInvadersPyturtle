import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser  # inbuilt - to acces the web browser
import os  # inbuilt - to acces the installed applications in your pc
import random  # inbuit
import pyautogui
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)


def speak(audio):  # is function se ye bolega with a parameter audio
    engine.say(audio)
    engine.runAndWait()


def wishkr():
    hour = int(datetime.datetime.now().hour)  # 0-24 tak ka ghanta mil gaayega
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am stark, Sir Please tell me")


def commandlo():
    # ye user se microphone input leta hai aur output string k taur p deta hai
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening . . .")
        r.pause_threshold = 0.5
        # control daba ke pause_threshold p click kr aur saare try kr
        # yaha control kr skte hain ki kitna tez bolo by increasing energy_threshold
        audio = r.listen(source)

        try:
            # print("Ruk bhai recognize kr rha hu . . . .")
            # speak("recognizing")
            bola = r.recognize_google(audio, language='en-in')
            print("U said : {} \n".format(bola))

        except Exception as e:
            print(e)
            speak("please say again")
            return "None"
        return bola


if __name__ == "__main__":
    wishkr()
    while True:
        bola = commandlo().lower()
    # ab yaha se chalu hai main logics jo bhi input doge uske hisaab se ye kaam krega
        if "wikipedia" in bola:
            speak("wait . . . searching wikipedia ")
            bola = bola.replace("wikipedia", "")
            results = wikipedia.summary(bola, sentences=2)
            # sentences = n *n numbers of senteces will be printed by the wikipedia
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open facebook" in bola:
            speak("opening boss")
            pyautogui.hotkey('win', "1")
            time.sleep(1)
            pyautogui.click(206, 62)
            pyautogui.hotkey("ctrl", 't')
            pyautogui.typewrite("facebook.com")
            pyautogui.press("enter")

        elif "open youtube" in bola:
            speak("okay boss ! opening youtube")
            pyautogui.hotkey('win', "1")
            time.sleep(2)
            pyautogui.click(206, 62)
            pyautogui.hotkey("ctrl", 't')
            pyautogui.typewrite("youtube.com")
            pyautogui.press("enter")
            pyautogui.moveTo(576, 160, duration=1.5)
            pyautogui.click()
            speak("okay! boss what should i search for you on youtube")
            prro = sr.Recognizer()
            with sr.Microphone() as soorc:
                print("Listening . . .")
                prro.pause_threshold = 1
                gopaudio = prro.listen(soorc)

                try:
                    gopbola = prro.recognize_google(gopaudio, language='en-in')

                except Exception as e:
                    speak("please say again")

                pyautogui.typewrite(gopbola)
                pyautogui.press("enter")

        elif "open google" in bola:
            speak("okay boss ! redirecting google")
            pyautogui.hotkey('win', "1")
            time.sleep(1)
            pyautogui.click(206, 62)
            pyautogui.hotkey("ctrl", 't')
            pyautogui.typewrite("google.com")
            pyautogui.press("enter")
            pyautogui.moveTo(679, 499, duration=0.5)
            pyautogui.click()
            speak("okay! boss what should i search for you")
            prro = sr.Recognizer()
            with sr.Microphone() as soorc:
                print("Listening . . .")
                prro.pause_threshold = 1
                gopaudio = prro.listen(soorc)

                try:
                    gopbola = prro.recognize_google(gopaudio, language='en-in')

                except Exception as e:
                    speak("please say again")

                pyautogui.typewrite(gopbola)
                pyautogui.press("enter")

        elif "open stack overflow" in bola:
            speak("okay boss ! initializing stackoverflow")
            pyautogui.hotkey('win', "1")
            time.sleep(1)
            pyautogui.click(206, 62)
            pyautogui.hotkey("ctrl", 't')
            pyautogui.typewrite("stackoverflow.com")
            pyautogui.press("enter")

        elif "open music" in bola:
            speak("okay boss ! getting some refreshing hits for you")
            music_dir = "D:\\songs"
            songs = os.listdir(music_dir)
            # to generate random number isi k liye random library import kiya tha
            k = random.randint(0, 638)
            os.startfile(os.path.join(music_dir, songs[k]))

        elif "play songs" in bola:
            speak("okay boss ! getting some refreshing hits for you")
            musicdir = "D:\\Songs"
            sng = os.listdir(musicdir)
            # to generate random number isi k liye random library import kiya tha
            k = random.randint(0, 6)
            os.startfile(os.path.join(musicdir, sng[k]))
            pyautogui.moveTo(1798, 10, duration=0.2)
            pyautogui.click()

        elif "the time" in bola:
            tm = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"boss ! the time is {tm}")

        # aise path copy kr ke you can open many programs in your pc
        elif "open code" in bola:
            speak("okay boss ! initializing visual studio code")
            cpath = 'C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(cpath)

        elif "open command" in bola:
            speak("okay boss ! initializing command prompt")
            cpath = "C:\\Users\\Dell\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
            os.startfile(cpath)

        elif "open file" in bola:
            speak("okay boss ! initializing my pc")
            pyautogui.hotkey('win', 'e')

        elif "open settings" in bola:
            speak("okay boss ! you are setting up")
            pyautogui.hotkey('win', 'i')

        elif "open control panel" in bola:
            speak("okay boss ! initializing control panel")
            cpath = "C:\\Users\\Dell\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk"
            os.startfile(cpath)

        elif "take screenshot" in bola:
            speak("okay boss ! snapping ")
            pyautogui.hotkey('win', 'w')

        elif "open chrome" in bola:
            speak("okay boss ! initializing google chrome")
            cpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
            os.startfile(cpath)
            pyautogui.moveTo(192, 64, duration=1)
            pyautogui.click()
            speak("Boss, what should i search for?")
            rrr = sr.Recognizer()
            with sr.Microphone() as srco:
                print("Listening . . .")
                rrr.pause_threshold = 1
                gcsearch = rrr.listen(srco)

                try:
                    gcbola = rrr.recognize_google(gcsearch, language='en-in')

                except Exception as e:
                    speak("please say again")

                pyautogui.typewrite(gcbola)
                pyautogui.press("enter")

        elif "open firefox" in bola:
            speak("okay boss ! initializing mozzila firefox")
            cpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Firefox.lnk"
            os.startfile(cpath)

        elif "open anydesk" in bola:
            speak("okay boss ! initializing anydesk")
            cpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\AnyDesk\\AnyDesk.lnk"
            os.startfile(cpath)

        elif "open downloads" in bola:
            speak("okay boss ! opening downloads")
            cpath = "C:\\Users\\Dell\\Downloads"
            os.startfile(cpath)

        elif "open start" in bola:
            pyautogui.press('win')

        elif "open recents" in bola:
            pyautogui.hotkey('win', 'tab')

        elif "open run" in bola:
            pyautogui.hotkey('win', 'r')

        elif "play music" in bola:
            speak("revising some hits for you")
            speak("boss from starting or just random")

            rr = sr.Recognizer()
            with sr.Microphone() as src:
                print("Listening . . .")
                rr.pause_threshold = 1
                musicaudio = rr.listen(src)

                try:
                    mbola = rr.recognize_google(musicaudio, language='en-in')

                except Exception as e:
                    speak("please say again")

            if "random" in mbola:
                pyautogui.press('win')
                pyautogui.moveTo(1734, 714, duration=0.5)
                pyautogui.click(1734, 714)
                pyautogui.moveTo(448, 173, duration=1.0)
                pyautogui.click(448, 173)
                pyautogui.moveTo(1798, 10, duration=0.2)
                pyautogui.click()
            elif "starting" in mbola:
                pyautogui.press('win')
                pyautogui.moveTo(1734, 714, duration=0.5)
                pyautogui.click(1734, 714)
                pyautogui.moveTo(621, 227, duration=1.5)
                pyautogui.click(621, 227)
                pyautogui.moveTo(1798, 10, duration=0.2)
                pyautogui.click()

        elif "pause music" in bola:
            pyautogui.press('win')
            pyautogui.moveTo(1734, 714, duration=0.5)
            pyautogui.click(1734, 714)
            pyautogui.moveTo(959, 1015, duration=1)
            pyautogui.click(959, 1015)
            pyautogui.moveTo(1798, 10, duration=0.2)
            pyautogui.click()

        elif "next music" in bola:
            pyautogui.press('win')
            pyautogui.moveTo(1734, 714, duration=0.5)
            pyautogui.click(1734, 714)
            pyautogui.moveTo(1014, 1012, duration=1)
            pyautogui.click(1014, 1012)
            pyautogui.moveTo(1798, 10, duration=0.2)
            pyautogui.click()

        elif "last music" in bola:
            pyautogui.press('win')
            pyautogui.moveTo(1734, 714, duration=0.5)
            pyautogui.click(1734, 714)
            pyautogui.moveTo(906, 1016, duration=1)
            pyautogui.click(906, 1016)
            pyautogui.moveTo(1798, 10, duration=0.2)
            for i in range(2):
                pyautogui.click()

        elif "open notifications" in bola:
            pyautogui.hotkey('win', 'a')

        elif "minimise all" in bola:
            pyautogui.hotkey('win', "d")

        elif "how are you" in bola:
            speak("Im fine as always, what about you boss.")

        elif "you have girlfriend" in bola:
            speak("no no no no bro im single, ha ha ha ")

        elif "refresh" in bola:
            pyautogui.hotkey('win', 'd')
            for i in range(4):
                pyautogui.rightClick()
                pyautogui.move(10, 60)
                pyautogui.click()

        elif "close" in bola:
            pyautogui.hotkey("alt", "F4")

        elif "open twitter" in bola:
            pyautogui.hotkey('win', "1")
            time.sleep(1)
            pyautogui.click(206, 62)
            pyautogui.hotkey("ctrl", 't')
            pyautogui.typewrite("twitter.com")
            pyautogui.press("enter")

        elif "open paint" in bola:
            pyautogui.press('win')
            time.sleep(1)
            r = pyautogui.locateOnScreen(
                "F:\\python coursera\\images to locate\\Untitled.png")
            pyautogui.click(r)

        elif "open new tab" in bola:
            pyautogui.hotkey('ctrl', 't')

        elif "open whatsapp" in bola:
            pyautogui.hotkey('win', '2')
            time.sleep(2)
            speak(
                "open whats app in your phone and scan the whats app web provided on the screen")
            time.sleep(3)
            speak("tell me now what to do next")
            wrr = sr.Recognizer()
            with sr.Microphone() as srwco:
                print("Listening . . .")
                wrr.pause_threshold = 1
                ws = wrr.listen(srwco)

                try:
                    wbola = wrr.recognize_google(ws, language='en-in')

                except Exception as e:
                    speak("please say again")

                if "show status" in wbola:
                    speak("opening status")
                    r = pyautogui.locateOnScreen(
                        "F:\\python coursera\\images to locate\\status.png")
                    pyautogui.click(r)

                elif "logout WhatsApp" in wbola:
                    r = pyautogui.locateOnScreen(
                        "F:\\python coursera\\images to locate\\optionwhats.png")
                    pyautogui.click(r)
                    time.sleep(0.5)
                    r = pyautogui.locateOnScreen(
                        "F:\\python coursera\\images to locate\\logout whats.png")
                    pyautogui.click(r)
                    speak("logging out of the whatsapp")

        elif "shutdown" in bola:
            speak("okay! boss im logging out")
            quit()