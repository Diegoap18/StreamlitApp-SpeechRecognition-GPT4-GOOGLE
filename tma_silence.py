'''
This is script is to generate a TMA and Time silence for audio.
it can be used by anyone that is needing a help to identify the silence time.
Enjoy just give me the credits by creation and have fun!!!!!

Author Diego A Pereira.
'''
import audioread
from pydub import AudioSegment,silence
import numpy 
import warnings
warnings.filterwarnings('ignore')


def duration_detector(length):
   ''' This function is to detect the duration of audio TMA to 
   be more speficic  they will be useto convert the values 
   into times.'''
     
   hours = length // 3600  # calculate in hours
   length %= 3600
   mins = length // 60  # calculate in minutes
   length %= 60
   seconds = length  # calculate in seconds
  
   return hours, mins, seconds

def silence_calculation(audio_path):
    ''' This function is the calculate paremeters audio to find the silence time, using audio and getting
    the variations of parameters and converting into math to transform in hours minutes.'''
    
    from pydub import AudioSegment,silence
    ##Silence Calculation:
    myaudio = intro = AudioSegment.from_file(audio_path)
    dBFS=myaudio.dBFS
    silence = silence.detect_silence(myaudio, min_silence_len=1000, silence_thresh=dBFS-18)

    silence = [((start/1000),(stop/1000)) for start,stop in silence] #in sec
    #silence
    Silence_minutes = []
    for i in silence:
        valor1 = i[0]
        valor2 = i[1]
        Seconds = (valor2-valor1)
        minutes = Seconds
        Silence_minutes.append(minutes)
        
    Silence_minutes

    m_silence = numpy.sum(Silence_minutes)
    
    return m_silence
    
def calculation_tma_silence(audio_path, m_silence):
    ''' this function is the main of process basically get the others functions and
    generate the final calculation as TMA total and Silence Total and sent it back as 
    return'''
    with audioread.audio_open(audio_path) as f:
        # totalsec contains the length in float
        totalsec = f.duration
        hours, mins, seconds = duration_detector(int(totalsec))
        print('TMA: {}:{}'.format(mins, seconds))
        tma_total = '{}:{}'.format(mins, seconds)
        
        hours_s, mins_s, seconds_s = duration_detector(int(m_silence))
        print('Silence: {}:{}'.format(mins_s, seconds_s))
        silence_total = '{}:{}'.format(mins_s, seconds_s)
        
    return tma_total, silence_total
    
if __name__ == "__main__":
    m_silence = silence_calculation(audio_path)
    tma_total, silence_total = calculation_tma_silence(audio_path, m_silence) 