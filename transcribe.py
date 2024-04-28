#!/usr/bin/python3
from dotenv import load_dotenv
from openai import OpenAI
import argparse
import os

# Create an argument parser
parser = argparse.ArgumentParser(description="Transcribe an audio file to text")

# Add the --file argument
parser.add_argument("--file", help="Name of the audiofile in the recordings directory", required=True)

# Parse the arguments
args = parser.parse_args()

# Load the .env file
load_dotenv()

# Read the OpenAI API key from the .env file
openai_api_key = os.getenv("OPENAI_API_KEY")

# Print the name of the file
print(f"Transcribing file: recordings/{args.file}")

# Create an OpenAI client
client = OpenAI(api_key=openai_api_key)

# Open the audio file
audio_file= open(f"recordings/{args.file}", "rb")

# Transcribe the audio file using OpenAI whisper-1 model
transcription = client.audio.transcriptions.create(
	model="whisper-1", 
	file=audio_file,
	language="en",
	prompt="Transcribe the following audio file to text. Make sure to include punctuation and capitalization. Where possible, distinguish between speakers."
)

# Save the transcription to a file
with open(f"transcriptions/{args.file}.txt", "w") as file:
	file.write(transcription.text)