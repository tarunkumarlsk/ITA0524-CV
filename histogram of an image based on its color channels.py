
import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_color_histogram(image_path):
    # Read the image in color
    image = cv2.imread(image_path)

    # Check if the image is loaded correctly
    if image is None:
        print(f"Error: Unable to load image from {image_path}")
        return

    # Split the image into its Blue, Green, and Red channels
    channels = cv2.split(image)
    colors = ('b', 'g', 'r')
    channel_names = ('Blue', 'Green', 'Red')

    # Plot the histogram for each color channel
    plt.figure(figsize=(10, 6))
    plt.title('Color Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Number of Pixels')

    for channel, color, name in zip(channels, colors, channel_names):
        # Calculate the histogram for the current channel
        histogram = cv2.calcHist([channel], [0], None, [256], [0, 256])
        
        # Plot the histogram
        plt.plot(histogram, color=color, label=f'{name} Channel')
        plt.xlim([0, 256])  # Set the limits for x-axis

    # Add a legend to the plot
    plt.legend()

    # Show the plot
    plt.show()

# Example usage
plot_color_histogram("C:/Users/kumar/Desktop/rl/sample.jpg")
