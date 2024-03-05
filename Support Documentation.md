# Video Keyframe Extractor

This Python script extracts keyframes from a video source, such as a webcam feed or a video file, and saves them as images. Users can customize the keyframe extraction frequency to adjust the number of keyframes extracted per unit of time.

## Usage

1. **Setup Environment**:
   - Ensure you have Python installed on your system.
   - Install OpenCV library using `pip install opencv-python`.

2. **Run the Script**:
   - Execute the script `video_keyframe_extractor.py`.
   - Provide the video source (0 for webcam or the path to a video file).
   - Specify the output folder where keyframe images will be saved.

3. **Customization**:
   - Adjust the `keyframe_interval` variable to change the frequency of keyframe extraction.
   - Modify the `output_folder` variable to specify a different folder for saving keyframe images.

## Functionality

- **Extract Keyframes**: The script reads frames from the video source and saves keyframes based on the specified interval.
- **Save as Images**: Keyframes are saved as individual images in the specified output folder.
- **Dynamic Interval Adjustment**: The interval between keyframe extraction increases progressively, allowing for a more varied selection of keyframes.

## Code Explanation

- **Imports**: The script imports the necessary modules `cv2` for video processing and `os` for file system operations.

- **`extract_keyframes` Function**: This function takes the video source path and output folder path as input. It reads frames from the video source, extracts keyframes at regular intervals, and saves them as images in the output folder.

- **Main Function**: The `if __name__ == "__main__":` block is the entry point of the script. It specifies the video source (0 for webcam) and the output folder for keyframe images. The `extract_keyframes` function is called with these parameters to initiate the keyframe extraction process.

- **Customization Options**: Users can customize the video source and output folder paths based on their requirements. Additionally, the keyframe extraction frequency can be adjusted by modifying the `keyframe_interval` variable.

This documentation provides an overview of how to use the script, its functionality, and insights into the code structure and customization options available.
