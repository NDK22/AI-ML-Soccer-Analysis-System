# Soccer Analysis System

## Overview
The Soccer Analysis System is a cutting-edge project that combines machine learning, computer vision, and deep learning techniques to provide in-depth analysis of football games. By employing state-of-the-art technologies such as YOLOv8, this system detects players, referees, and footballs, and includes custom-trained models to enhance detection accuracy. The system also integrates various techniques to measure and analyze player movements, ball interactions, and more.

https://github.com/NDK22/AI-ML-Soccer-Analysis-System/blob/main/Untitled%20video%20-%20Made%20with%20Clipchamp%20(2).gif

![Soccer Analysis GIF]([assets/soccer_analysis.gif](https://github.com/NDK22/AI-ML-Soccer-Analysis-System/blob/main/Untitled%20video%20-%20Made%20with%20Clipchamp%20(2).gif))  


## Features
- **Object Detection and Tracking**: Utilizes YOLOv8 for detecting and tracking players, referees, and footballs across frames.
- **Custom YOLO Model**: Fine-tunes and trains a custom YOLO model for improved accuracy in detecting specific objects.
- **Player Color Assignment**: Uses KMeans clustering for pixel segmentation to accurately assign players to teams based on their t-shirt colors.
- **Camera Movement Estimation**: Measures camera movement between frames using optical flow techniques.
- **Perspective Transformation**: Applies the perspective transformation to convert measurements from pixels to meters, providing a realistic representation of scene depth and perspective.
- **Speed and Distance Calculation**: Computes the speed and distance covered by players throughout the game.

### Prerequisites
- Python 3.x
- Required Python libraries: `ultralytics`, `supervision`, `opencv-python`, `numpy`, `matplotlib`, `pandas`

## Datasets
- **[Kaggle Dataset](https://www.kaggle.com/competitions/dfl-bundesliga-data-shootout/data?select=clips)**: Contains football game data for training and evaluation.
- **[Roboflow Football Dataset](https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/dataset/1)**: Provides additional football game data for model enhancement and validation.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/NDK22/AI-ML-Soccer-Analysis-System.git

2. Change directory:
cd football-analysis-system

3. Install the prerequisites

## Usage
- Place your video files in the input_videos directory.
- Run the main script to start the analysis: python main.py
- The results will be saved in the output_videos directory.

## Code Structure
- main.py: The main script for running the analysis.
- speed_distance_estimator.py: Calculates speed and distance covered by players.
- object_detection.py: Implements YOLO object detection and tracking.
- color_assignment.py: Assigns players to teams based on t-shirt colors.
- camera_movement.py: Measures camera movement between frames.
- perspective_transformer.py: Applies perspective transformation.
- utils/: Contains utility functions and helper modules.

## Contributing
If you would like to contribute to this project, please fork the repository and create a pull request with your changes. Make sure to follow the coding style and include appropriate tests for your contributions.

## Acknowledgements
- YOLOv8 for object detection.
- OpenCV for computer vision techniques.
- KMeans for color segmentation.

## Contact
For any questions or issues, please open an issue on the GitHub repository.
