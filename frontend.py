import base64
import streamlit as st
import streamlit.components.v1 as components
import time
from backend.api.endpoints.behavioral_cv import get_behavioral_score
from backend.api.endpoints.behavioral_bq import generate_problem, evaluate_user_response
from backend.api.endpoints.technical import *


# Inject CSS for custom styling with background image
st.markdown("""
    <style>

    [data-testid="stAppViewContainer"] {
    background-image: url("https://i.imgur.com/lSjVYqD.jpeg");
    background-size: 100%;
    background-position: center;
    background-attachment: fixed;
    }

    .stApp {
        background-image: url("intro.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #39FF14 !important; /* Primary text color (neon green) */
    }

    /* Set primary text color */
    .css-18e3th9, .css-1d391kg, h1, h2, h3, h4, h5, h6, p {
        color: #000000 !important;
    }

    /* Set secondary color (lighter green) for subheaders */
    .css-1v0mbdj {
        color: #66ff66 !important;
    }

    /* Style for user input fields with white text */
    .stTextInput>div>div>input, .stTextArea>div>textarea, .stSelectbox>div>div>div>span {
        color: white !important;
        background-color: rgba(0, 0, 0, 0.7) !important; /* Slightly transparent black background */
        border: 1px solid #39FF14 !important;
    }

    /* Placeholder text */
    ::placeholder {
        color: #66ff66 !important;
    }

    /* Button styling */
    .stButton>button {
        color: white !important;
        background-color: #39FF14 !important;
        border: none;
        font-weight: bold;
        padding: 8px 20px;
    }
    </style>
""", unsafe_allow_html=True)


def intro_screen():
    st.title("Ready for your next job?")
    st.subheader("Select an interview type below to access a wide range of technical questions, track progress, and sharpen your skills. Find your offer with offer.ai.")
    
    # Interview type selection
    st.subheader("Select Interview Type")
    difficulties = ["1st/2nd Year Internship", "All Years Internship", "Entry-Level"]
    difficulty = st.selectbox("Choose Interview Difficulty", difficulties)
    
    if st.button("Proceed"):
        st.session_state['authenticated'] = True
        st.session_state['difficulty'] = difficulty
        st.success("Login successful!")
        st.session_state['interview_stage'] = 'behavioral'

#import streamlit as st
import streamlit.components.v1 as components
import base64

def behavioral_interview():
    st.title("Behavioral Interview")
    st.write(f"Position Level: {st.session_state['difficulty']}")
    st.write("**Instructions:** Please ensure your video and audio are turned on.")

    for i in range(6):
        interviewQuestion = generate_problem(question_number=i)
        st.write(interviewQuestion)

        # JavaScript for webcam recording with automatic save and upload
        video_recorder_html = f'''
            <div>
                <video id="video" width="640" height="480" autoplay></video>
                <button id="startRecord" onclick="startRecording()">Start Recording</button>
                <button id="stopRecord" onclick="stopRecording()" disabled>Stop Recording</button>
                <p id="status">Status: Not Recording</p>
                <br/>
                <video id="playback" width="320" height="240" controls></video>
            </div>
            <script>
                let mediaRecorder;
                let recordedChunks = [];
                
                async function startRecording() {{
                    let stream = await navigator.mediaDevices.getUserMedia({{ video: true }});
                    document.getElementById("video").srcObject = stream;
                    mediaRecorder = new MediaRecorder(stream, {{ mimeType: 'video/webm' }});
                    mediaRecorder.ondataavailable = event => {{
                        if (event.data.size > 0) recordedChunks.push(event.data);
                    }};
                    mediaRecorder.onstop = () => {{
                        const blob = new Blob(recordedChunks, {{ type: 'video/webm' }});
                        const reader = new FileReader();
                        reader.readAsDataURL(blob);
                        reader.onloadend = () => {{
                            const base64data = reader.result.split(',')[1];
                            window.parent.postMessage({{ 'videoData': base64data, 'index': {i} }}, "*");
                        }};
                        document.getElementById("status").innerHTML = "Status: Stopped Recording";
                        recordedChunks = [];
                    }};
                    mediaRecorder.start();
                    document.getElementById("status").innerHTML = "Status: Recording";
                    document.getElementById("startRecord").disabled = true;
                    document.getElementById("stopRecord").disabled = false;
                }}
                
                function stopRecording() {{
                    mediaRecorder.stop();
                    document.getElementById("video").srcObject.getTracks().forEach(track => track.stop());
                    document.getElementById("startRecord").disabled = false;
                    document.getElementById("stopRecord").disabled = true;
                }}

                window.addEventListener("message", (event) => {{
                    if (event.data.index === {i}) {{
                        document.getElementById("playback").src = "data:video/webm;base64," + event.data.videoData;
                    }}
                }});
            </script>
        '''

        # Embed the video recorder HTML in Streamlit
        components.html(video_recorder_html, height=500)

        # Receive video data from JavaScript and save it
        if f"video_data_{i}" in st.session_state:
            video_bytes = base64.b64decode(st.session_state[f"video_data_{i}"])
            video_path = f"behavioral_interview_{i}.mp4"
            with open(video_path, "wb") as f:
                f.write(video_bytes)
            st.success(f"Recording saved successfully for question {i}!")

            # Pass the saved video path to get_behavioral_score function
            uploaded_score = get_behavioral_score(video_path, interviewQuestion)
            st.write("Behavioral Score:", uploaded_score)

        st.write("\n")

    if st.button("Submit Response"):
        st.session_state['behavioral_analysis'] = "Placeholder behavioral analysis result."
        st.session_state['interview_stage'] = 'technical'


def technical_interview1():
    st.title("Technical Interview Question 1")
    st.write(f"Difficulty Level: {st.session_state['difficulty']}")
    st.write("You have 40 minutes to complete the following question.")

    problems = generate_user(st.session_state['difficulty'])   
    st.write("**Question:** " + problems[0]['question'])
        
        
    st.text_area("Write your code here:")

    if st.button("Submit Code"):
        st.session_state['technical_analysis'] = "Placeholder technical analysis result."
        st.session_state['interview_stage'] = 'technical2'

def technical_interview2():
    st.title("Technical Interview Question 2")
    st.write(f"Difficulty Level: {st.session_state['difficulty']}")
    st.write("You have 40 minutes to complete the following question.")

    problems = generate_user(st.session_state['difficulty'])  
     
    st.write("**Question:** " + problems[1]['question'])
        
        
    st.text_area("Write your code here:")

    if st.button("Submit Code"):
        st.session_state['technical_analysis'] = "Placeholder technical analysis result."
        st.session_state['interview_stage'] = 'loading'

# Loading Screen
def loading_screen():
    st.title("Analyzing Your Responses")
    with st.spinner('Processing...'):
        time.sleep(3)  # Simulate processing time
    st.session_state['interview_stage'] = 'feedback'
    

# Feedback Screen
def feedback_screen():
    st.title("Interview Feedback")
    name = st.text_input("Enter Your Name")
    if name:
        score = 850  # Placeholder score out of 1000
        st.write(f"**Score:** {score}/1000")
        st.write("**Behavioral Analysis:**")
        st.write(st.session_state.get('behavioral_analysis', 'No behavioral analysis available.'))
        st.write("**Technical Analysis:**")
        st.write(st.session_state.get('technical_analysis', 'No technical analysis available.'))
        st.write("""
        **Resources to Improve:**
        - [Cracking the Coding Interview](https://www.crackingthecodinginterview.com/)
        - [LeetCode](https://leetcode.com/)
        - [System Design Primer](https://github.com/donnemartin/system-design-primer)
        """)
        if st.button("Take Another Interview"):
            st.session_state.clear()
         

# Main function to control app flow
def main():
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False
    if 'interview_stage' not in st.session_state:
        st.session_state['interview_stage'] = 'intro'
    if 'difficulty' not in st.session_state:
        st.session_state['difficulty'] = None
    
    if not st.session_state['authenticated']:
        intro_screen()
    else:
        if st.session_state['interview_stage'] == 'intro':
            intro_screen()
        elif st.session_state['interview_stage'] == 'behavioral':
            behavioral_interview()
        elif st.session_state['interview_stage'] == 'technical':
            technical_interview1()
        elif st.session_state['interview_stage'] == 'technical2':
            technical_interview2()
        elif st.session_state['interview_stage'] == 'loading':
            loading_screen()
        elif st.session_state['interview_stage'] == 'feedback':
            feedback_screen()

if __name__ == "__main__":
    main()
