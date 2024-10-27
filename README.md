<img width="297" alt="offer.ai logo" src="https://github.com/user-attachments/assets/5a6ea129-b7f6-4602-84ef-15287656b504">

# Offer.ai - Trained AI Interview Simulator


## 💡 **Inspiration**
- The tech industry can be challenging to break into, especially with the high demands of Software Engineering (SWE) interviews.
- Genuine interview practice is often limited and costly, creating barriers for aspiring tech professionals.
- **Offer.ai** provides an affordable, open-source solution for authentic interview experiences, helping candidates build confidence and improve their skills with AI-driven feedback.

## 👔 **What it Does**  
**Offer.ai** is an AI-powered interview simulator that provides real-time practice and feedback for SWE candidates by evaluating:

- **Technical Skills**: Assesses code quality and problem-solving approaches for technical questions. *(Score out of 600)*
- **Behavioral Responses**: Evaluates answers using the STAR method and principles from top tech companies. *(Score out of 400)*
- **Audio-Visual Communication**: Analyzes non-verbal cues, confidence, and tone through visual and audio responses using computer vision. *(Behavioral 400 = Video Score/100 + Audio Score/300)*

## 🛠️ **How We Built It**
We leveraged **Google Gemini 1.5 Flash LLM models**, each trained on vast datasets for specific interview types:

- **Technical Model**: Trained on thousands of coding challenges to assess problem-solving and coding proficiency.
- **Behavioral Computer Vision Model**: Uses STAR-based examples and principles from companies like Amazon to evaluate soft skills, emotional cues, and non-verbal responses.
- Developed with **Python**, **Google Cloud**, and **Streamlit** to create a streamlined, user-friendly interface for instant scoring.
- **Visual Studio Code** and **Mermaid** were essential for coding, visualization, and debugging.

## 🦺 **Challenges We Ran Into**
- Training and fine-tuning the AI models to provide consistent, real-world feedback was challenging.
- The **behavioral analysis model** required careful calibration for STAR-based responses.
- Integrating **computer vision** for emotion detection demanded complex adjustments to capture subtle communication cues effectively.
- **Streamlit optimization** was crucial for maintaining model performance and delivering a cohesive user experience.

## 🏆 **Accomplishments We’re Proud Of**
- Creating an accessible tool that offers candidates meaningful insights and an authentic interview experience.
- Fine-tuned models provide feedback that closely mirrors real tech interview expectations.
- Proud to offer **Offer.ai** as an open-source solution, breaking down financial and logistical barriers to career advancement.

## 📚 **What We Learned**
- Gained experience integrating **large language models** and **computer vision** into practical applications.
- Developed an understanding of training **LLMs** on specific interview types and optimizing **Streamlit** for a smooth user experience.
- Deepened insights into **model performance** and **feedback** in real-world interview simulations.

## 🚀 **What's Next for Offer.ai - Trained AI Interview Simulator**
- **Expand capabilities** by integrating more interview categories, including system design and advanced technical interviews, and more tech roles like data science and product management.
- **Refine computer vision model** to better analyze facial expressions and body language.
- Implement **community-driven improvements** for users to contribute questions, provide feedback, and share resources.
