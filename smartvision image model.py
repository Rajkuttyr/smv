import google.generativeai as genai
import PIL.Image
import os
import cv2
from gtts import gTTS

# Initialize the webcam
camera = cv2.VideoCapture(0)  # 0 for default camera, 1, 2, etc. for others

# Check if the webcam is opened successfully
if not camera.isOpened():
    raise IOError("Cannot open webcam")
genai.configure(api_key="AIzaSyCZcvBAVsPDc4307AXJE3_FgPJHhCv1KGY")
while True:
    # Read a frame from the webcam
    ret, frame = camera.read()

    # Check if the frame is valid
    if not ret:
        break

    # Display the frame in a window
    cv2.imshow('Webcam Capture', frame)
    

    # Capture image when 's' key is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'): 
        cv2.imwrite('captured_image.jpg', frame)
        print("Image captured!")




        img = PIL.Image.open(r'captured_image.jpg')

        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(["What is in this photo?", img])
        print(response.text)
        text = response.text
        language = 'en'

        # Create gTTS object
        myobj = gTTS(text=text, lang=language, slow=False)

        # Save the audio as a file
        myobj.save("output.mp3")


        
        # for playing note.wav file
        os.system("output.mp3")