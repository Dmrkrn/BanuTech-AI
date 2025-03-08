import cv2
import os
import time

video_path = "videolar/2024.mp4"
output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

video = cv2.VideoCapture(video_path)
fps = video.get(cv2.CAP_PROP_FPS)

count = 0
target_fps = 30
frame_time = 1 / target_fps 
prev_time = time.time() 

 

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    
    current_time = time.time()
    
    if current_time - prev_time >= frame_time:
        frame_output = os.path.join(output_folder, f"frame_{count}.jpg")  # Daha fazla sıralama için 3 basamak kullanabiliriz
        cv2.imwrite(frame_output, frame)
        count += 1
        prev_time = current_time  

video.release()
print(f"Toplam {count} frame kaydedildi.")
