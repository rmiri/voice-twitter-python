import speech_recognition
import postTweet

recognizer = speech_recognition.Recognizer()

def checkMessage(msg):
    if msg:
        with speech_recognition.Microphone() as source:
            print('Are you sure you want to tweet: ' + msg + '   yes/no/cancel')
            audio = recognizer.listen(source)
            try: 
                response = recognizer.recognize_google(audio)
                if response == 'yes':
                    postTweet.postStatus(msg)
                elif response == 'no':
                    message()
                elif response == 'cancel':
                    print('goodbye')
                else:
                    print('no answer')
            except:
                print("An exception occurred")
            

def message():
    with speech_recognition.Microphone() as source:
        print("What do you want to tweet about?")
        audio = recognizer.listen(source)
        try:
            response = recognizer.recognize_google(audio)
            checkMessage(response)
        except speech_recognition.UnknownValueError:
            print("I CAN'T HEAR YOU")
        except speech_recognition.RequestError:
            print("too busy, talk to you later")

message()