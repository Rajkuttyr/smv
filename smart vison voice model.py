import pyaudio
import wave
import os
import google.generativeai as genai
import PIL.Image
import os
import cv2
from gtts import gTTS

# Set recording parameters
CHUNK = 1024  # Record in chunks of 1024 samples
FORMAT = pyaudio.paInt16  # 16-bit resolution
CHANNELS = 1  # Mono audio
RATE = 44100  # Sample rate (Hz)
RECORD_SECONDS = 5  # Duration of recording in seconds
WAVE_OUTPUT_FILENAME = "sample.mp3"  # Output file name

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open microphone stream
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK,
)
genai.configure(api_key="AIzaSyCZcvBAVsPDc4307AXJE3_FgPJHhCv1KGY")
print("Recording...")
    
# Record audio
frames = []
for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording.")

# Close the stream and terminate PyAudio
stream.stop_stream()
stream.close()
p.terminate()

# Save the recording to a WAV file
wf = wave.open(WAVE_OUTPUT_FILENAME, "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b"".join(frames))
wf.close()

print(f"Audio saved to {WAVE_OUTPUT_FILENAME}")
os.system(WAVE_OUTPUT_FILENAME)
# Upload the file.
audio_file = genai.upload_file(path='sample.mp3')
# Initialize a Gemini model appropriate for your use case.
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Create the prompt.
prompt = "find answer to question"

# Pass the prompt and the audio file to Gemini.
response = model.generate_content([prompt, audio_file])

# Print the response.
print(response.text)
text = response.text
language = 'en'

# Create gTTS object
myobj = gTTS(text=text, lang=language, slow=False)

        # Save the audio as a file
myobj.save("output.mp3")


        
        # for playing note.wav file
os.system("output.mp3")