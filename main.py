from backend.api.endpoints.behavioral_cv import process_video, generate_transcript, generate_visual_score

video = process_video("behavorial_interview.mp4", "Rate this interview out 100, include 3 key details said")

print (generate_transcript(video))

