# TicketParser
Small application for analysing emails with sentiment analysis, using spacy (en_core_web_sm) for NER and TextBlob for sentiment analysis.

# How to run

- Clone the code! Make sure to install all necessary python packages (Best Practice: Use an own environment)
- Open a new terminal (CLI)
- Make sure to switch to the correct directory of your project
- Execute “app.py” in your terminal (CLI) using the following command: python app.py
- This command will run the python file and start a FLASK server 
- Open http://127.0.0.1:5000 in your Webbrowser
- If everything went well, you will see the following start screen:

  
<img width="873" alt="Start" src="https://github.com/user-attachments/assets/f1dccf2c-487f-4dd1-85c0-7358e898e8a7"><br>
- In the attachments you will find three sample emails. One email is friendly. Click the upload file button and load the "friendly" email <b>(email_friendly.txt)</b>.
- The sentiment analysis classifies the email as friendly and a green light symbol appears.


<img width="871" alt="Good" src="https://github.com/user-attachments/assets/5713cc53-580e-4fab-ae69-67c213ec5cc6"><br>
- Click the upload file button and load the "sad" email <b>(email_sad.txt)</b>.
- The sentiment analysis classifies the email as sad and a blue light symbol appears.


<img width="867" alt="Sad" src="https://github.com/user-attachments/assets/d27414ee-4c98-4e4c-87da-e2fa7b096560"><br>
- Click the upload file button and load the "angry" email <b>(email_angry.txt)</b>.
- The sentiment analysis classifies the email as angry and a red light symbol appears.


<img width="873" alt="Bad" src="https://github.com/user-attachments/assets/6eaa2680-58df-41f5-be1a-dd567424825f"><br>
- Of course, you can also simply enter any text in the text field and click the analyze text button!

# Author

David Bistron
