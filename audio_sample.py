#import pypdf
#import gtts

from gtts import gTTS
sample="hello everyone"
tts = gTTS(sample, lang='en')
tts.save('hello.mp3')