import google.generativeai as genai
from bigback import load_creds


creds = load_creds()
genai.configure(credentials=creds)
model = genai.GenerativeModel('tunedModels/avbehavorialapi-rh48ho8em5cf')
response = model.generate_content("Positive Cues in AUDIO response to interview questions voice/speech patterns: 25/25 - Clear and Concise Communication25/25 - Professionalism in Speaking20/25 - Engaging & Enthusiastic25/25 - Confidence in KnowledgeNegative Cues in AUDIO response to interview questions (voice/speech patterns):Minus 5 Points - HesitationMinus 0 Points - NervousnessMinus 0 Points - Uncertainty")
print(response.text)
