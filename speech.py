import speech_recognition as sr
import emoji
EmojiD={}
Expressions = ['Laughing','Crying']
Laughing=['\U0001F600','\U0001F603','\U0001F604','\U0001F601','\U0001F606','\U0001F605','\U0001F923','\U0001F602','\U0001F642','\U0001F60A']
Crying=['\U0001F641','\U0001F60C','\U0001F614','\U0001F62A','\U0001F61F','\U0001F630','\U0001F625','\U0001F622','\U0001F62D','\U0001F61F','\U0001F629','\U0001F613','\U0001F62B']
Hands=['\U0001F448','\U0001F91A','\U0001F590','\U0001F596','\U0001F44C','\U0001F91F','\U0001F448','\U0001F449','\U0001F44F','\U0001F64F']
Trees=['\U0001F332','\U0001F333','\U0001F334','\U0001F33E',]
Fruits=['\U0001F347','\U0001F348','\U0001F349','\U0001F34A','\U0001F34B','\U0001F34C','\U0001F34D','\U0001F34E','\U0001F34F','\U0001F352','\U0001F353']
Cars=['\U0001F697']
Traffic=['\U0001F6A6']
Ice=['\U0001F368']

EmojiD={'laughing': Laughing,'crying': Crying,'wave':Hands,'fruits':Fruits,'trees':Trees,'fruit':Fruits,'and':Hands,'car':Cars,'traffic':Traffic,'icecream':Ice}

r = sr.Recognizer()
with sr.Microphone() as source:
    print("May i know which emoji you want: ")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        emotion_input=text
    except:
        print("Sorry could not recognize what you said")

for i in EmojiD[emotion_input]:
    print(i,end='     ')
print()
