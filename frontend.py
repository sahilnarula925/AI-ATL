import streamlit as st
import streamlit.components.v1 as components
import time
from backend.api.endpoints.behavioral_cv import get_behavioral_score
from backend.api.endpoints.behavioral_bq import generate_problem, evaluate_user_response
from backend.api.endpoints.technical import generate_user, evaluate


# Inject CSS for custom styling with background image
st.markdown("""
    <style>
    /* Set the background image */
    .reportview-container, .main {
        background-image: url("intro.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #39FF14 !important; /* Primary text color (neon green) */
    }

    /* Set primary text color */
    .css-18e3th9, .css-1d391kg, h1, h2, h3, h4, h5, h6, p {
        color: #39FF14 !important;
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

# Placeholder functions (not integrated with actual backend)
def placeholder_function():
    return "This is a placeholder for backend functionality."

# Intro Screen: Mock Login Screen
def intro_screen():
    st.title("Offer.ai")
    st.subheader("Login with your credentials")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Mock authentication success
        st.session_state['authenticated'] = True
        st.success("Login successful!")
        

# Choose Interview Type Screen
def choose_interview_type():
    st.title("Select Interview Type")
    difficulties = ["1st/2nd Year Internship", "All Years Internship", "Entry-Level"]
    difficulty = st.selectbox("Choose Interview Difficulty", difficulties)
    if st.button("Proceed"):
        st.session_state['difficulty'] = difficulty
        st.session_state['interview_stage'] = 'behavioral'
        

# Behavioral Interview Screen with webcam recording
def behavioral_interview():
    st.title(" Behavioral Interview")
    st.write(f"Position Level: {st.session_state['difficulty']}")
    st.write("**Instructions:** Please ensure your video and audio are turned on.")

    for i in range (0, 6):
        # Display mock behavioral question
        interviewQuestion = generate_problem(question_number= i)
        st.write(interviewQuestion)
        
        # HTML and JavaScript for webcam recording
        # HTML and JavaScript for webcam recording

        video_recorder_html = '''
            <div>
                <video id="video" width="320" height="240" autoplay></video>
                <button id="startRecord" onclick="startRecording()">Start Recording</button>
                <button id="stopRecord" onclick="stopRecording()" disabled>Stop Recording</button>
                <p id="status">Status: Not Recording</p>
                <br/>
                <video id="playback" width="320" height="240" controls></video>
                <a id="downloadLink" style="display: none;">Download Video</a>
            </div>
            <script>
                let mediaRecorder;
                let recordedChunks = [];
                async function startRecording() {
                    let stream = await navigator.mediaDevices.getUserMedia({ video: true });
                    document.getElementById("video").srcObject = stream;
                    mediaRecorder = new MediaRecorder(stream, { mimeType: 'video/webm' });
                    mediaRecorder.ondataavailable = event => {
                        if (event.data.size > 0) recordedChunks.push(event.data);
                    };
                    mediaRecorder.onstop = () => {
                        const blob = new Blob(recordedChunks, { type: 'video/mp4' });
                        const url = URL.createObjectURL(blob);
                        document.getElementById("playback").src = url;
                        const downloadLink = document.getElementById("downloadLink");
                        downloadLink.href = url;
                        downloadLink.download = "behavioral_interview.mp4";
                        downloadLink.style.display = "block";
                        downloadLink.textContent = "Download Your Recording";
                        recordedChunks = [];
                    };
                    mediaRecorder.start();
                    document.getElementById("status").innerHTML = "Status: Recording";
                    document.getElementById("startRecord").disabled = true;
                    document.getElementById("stopRecord").disabled = false;
                }
                function stopRecording() {
                    mediaRecorder.stop();
                    document.getElementById("video").srcObject.getTracks().forEach(track => track.stop());
                    document.getElementById("status").innerHTML = "Status: Stopped Recording";
                    document.getElementById("startRecord").disabled = false;
                    document.getElementById("stopRecord").disabled = true;
                }
            </script>
        '''


        # Embed the video recorder HTML in Streamlit
        components.html(video_recorder_html, height=500)
    # Add a Streamlit file uploader to accept video file for saving
        st.write("Upload your recording here after recording stops:")
        uploaded_video = st.file_uploader("Choose a video file", type=["mp4"])

        if uploaded_video is not None:
            with open("behavioral_interview.mp4", "wb") as f:
                f.write(uploaded_video.read())
            get_behavioral_score("behavioral_interview.mp4", interviewQuestion)
            st.success("Recording saved successfully!")
        

        # Placeholder for submitting response
        if st.button("Submit Response"):
            
            st.session_state['behavioral_analysis'] = "Placeholder behavioral analysis result."
            st.session_state['interview_stage'] = 'technical'
        

# Technical Coding Interview Screen
def technical_interview():
    st.title("Technical Interview")
    st.write(f"Difficulty Level: {st.session_state['difficulty']}")
    st.write("You have 40 minutes to complete the following question.")

    # Display mock technical question
    difficulty_level = {
        "1st/2nd Year Internship": "Easy",
        "All Years Internship": "Medium",
        "Entry-Level": "Hard"
    }
   
    technicalQuestion = generate_user(difficulty_level)
    st.write("**Question:** " + "problem['question']")
    
    # Placeholder for code entry and hint
    st.text_area("Write your code here:")
    if st.button("Hint"):
        st.info("problem['hints']")

    # Placeholder for submitting code
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
    
    if not st.session_state['authenticated']:
        intro_screen()
    else:
        if st.session_state['interview_stage'] == 'intro':
            choose_interview_type()
        elif st.session_state['interview_stage'] == 'behavioral':
            behavioral_interview()
        elif st.session_state['interview_stage'] == 'technical':
            technical_interview()
        elif st.session_state['interview_stage'] == 'loading':
            loading_screen()
        elif st.session_state['interview_stage'] == 'feedback':
            feedback_screen()

if __name__ == "__main__":
    main()
