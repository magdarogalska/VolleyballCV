import cv2
import os


def video_to_frames(video_path, frames_dir):
    # Make sure the folder exists, if not, create it
    if not os.path.exists(frames_dir):
        os.makedirs(frames_dir)

    # Load the video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    frame_count = 0
    while True:
        # Read frame by frame
        ret, frame = cap.read()

        # If frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Construct the filename of the frame
        frame_filename = os.path.join(frames_dir, f"frame_{frame_count:04d}.png")

        # Write the frame image to the directory
        cv2.imwrite(frame_filename, frame)
        print(f"Saved {frame_filename}")

        frame_count += 1

    # Release the VideoCapture object
    cap.release()


# Usage
video_path = 'C:\\Users\\kathr\\Desktop\\Frames\\mp4\\bgframe.mp4'
frames_dir = 'C:\\Users\\kathr\\Desktop\\Frames\\bg_frames'
video_to_frames(video_path, frames_dir)
