import os
from queue import Queue
from threading import Thread

def tts(lmao = 'lmao'):
    from gtts import gTTS; from playsound import playsound
    if lmao == '': lmao = 'lmao'
    tts = gTTS(text = lmao, lang = 'en'); tts.save("TTS.mp3"); playsound("TTS.mp3"); os.remove("TTS.mp3")
def yanderesim():
    import random as cock, time as dio
    x = ['sixty nine','four twenty','666','cum','tiddies lol','please','weed','Creep by','by LMFAO','verb noun','bro','gayve strider dick rider','society','gamer','m i n o r i t i e s','Cum Univeristy'] #cum haha
    z = cock.randint(0,len(x)-1);p = cock.randint(0,len(x)-1); newstring = x[z]+' '+x[p];
    return newstring

tts(yanderesim())
# A thread that produces data
def producer(out_q):
    while True:
        # Produce some data
        data = yanderesim()
        out_q.put(data)
        print('thread[1]:', data)

# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        tts(data)

# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target = consumer, args =(q, ))
t2 = Thread(target = producer, args =(q, ))
t1.start()
t2.start()
