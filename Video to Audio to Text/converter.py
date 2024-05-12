# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

# create a speech recognition object
r = sr.Recognizer()
prnt=lambda st: print(st, flush=True)
# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)
    #print(dir(sound))
    prnt("sound loaded")
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 1000,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    prnt("sound splitted")

    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened, language="ru-RU")
            except sr.UnknownValueError as e:
                 pass
#                print("Error:", str(e))
            else:
                proc_print(i, len(chunks))
                whole_text += text
    return whole_text


def proc_print(i, value):
 print('\r', end="")
 width=os.get_terminal_size()[0]
 for x in range(width-5):
  if x==0 or x==width-6: print("|",end="")
  elif x>width//2-1 and x<width//2+1:
   if int(i/value*100)<10: print(" ",end="")
   print(" ", int(i/value*100),"% ",sep="",end="")
  else:
   if x<i/value*(width-3): print("#",end="")
   else: print(" ",end="")  
  print(end="", flush=True)


dirAudio="audio/"
dirVideo="video/"
dirText ="text/"



def extractAudioFVideo(video):
    os.system('ffmpeg -i {} -acodec pcm_s16le -ar 16000 {}.wav'.format(dirVideo+video, dirAudio+video[:-4]))
    file=open(dirText+vid[:-4]+".txt", "w", encoding="utf-8")
    file.write(get_large_audio_transcription(dirAudio+video[:-4]+".wav"))
    file.close()

for vid in os.listdir(dirVideo):
 print(vid)
 extractAudioFVideo(vid)
 print("File written!!!")