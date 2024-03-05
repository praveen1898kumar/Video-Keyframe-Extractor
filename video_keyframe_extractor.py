import cv2
import os

# Function to extract keyframes and save them as images
def extract_keyframes(video_path, output_folder):
    # Open video capture object
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open video.")
        return

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Variables for frame count and keyframe count
    frame_count = 0
    keyframe_count = 0
    keyframe_interval = 30  # Change this value to adjust keyframe extraction frequency

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Increment frame count
        frame_count += 1

        # Extract keyframes
        if frame_count % keyframe_interval == 0:
            # Save keyframe as an image
            keyframe_filename = f"keyframe_{keyframe_count}.jpg"
            keyframe_path = os.path.join(output_folder, keyframe_filename)
            cv2.imwrite(keyframe_path, frame)
            print(f"Keyframe {keyframe_count} saved.")
            keyframe_count += 1

        # Increase the interval for next keyframe
        if frame_count % (keyframe_interval * 2) == 0:
            keyframe_interval += 1


    # Release video capture object
    cap.release()

if __name__ == "__main__":
    # Video source (0 for webcam, or provide the path to a video file)
    video_source = 1

    # Output folder for keyframe images
    output_folder = "/Users/praveen18kumar/Desktop/KeyFrame Exctraction"

    # Extract keyframes from live webcam feed
    extract_keyframes(video_source, output_folder)
