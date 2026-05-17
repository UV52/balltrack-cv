import cv2
import os

video_folder = "data/raw_videos"
output_folder = "data/frames"

os.makedirs(output_folder, exist_ok=True)

frame_count = 0

for video_name in os.listdir(video_folder):

    video_path = os.path.join(video_folder, video_name)

    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_count % 5 == 0:
            filename = f"frame_{frame_count}.jpg"

            cv2.imwrite(
                os.path.join(output_folder, filename),
                frame
            )

        frame_count += 1

    cap.release()

print("Frames extracted successfully.")