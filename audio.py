import pygame
import os
import random

# Set the path of the directory containing the audio files
audio_path = '/home/ram/Downloads/audios'

# Get a list of all the audio files in the directory
audio_files = os.listdir(audio_path)

# Shuffle the list of audio files
random.shuffle(audio_files)

# Initialize Pygame mixer
pygame.mixer.init()

# Loop through the shuffled list of audio files
for audio_file in audio_files:
    # Load the audio file
    audio = pygame.mixer.Sound(os.path.join(audio_path, audio_file))

    # Play the audio file
    audio.play()

    # Wait until the audio has finished playing
    while pygame.mixer.get_busy():
        pass

