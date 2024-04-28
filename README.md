# OpenAI-transcribe
This is a simple Python script that utilises the OpenAI API to transcribe audio files using their whisper-1 model (powered by the open source Whisper V2 model). All audio recordings should be in the `recordings` directory, and the text output will be saved to the `transcriptions` directory (name of the file will be the same as the audio file, but with a `.txt` extension).  
To make this script work, you need to have an OpenAI API key saved in the .env file (example is in [env](env) file).  
Example use:
```bash
python3 transcribe.py --file my_audio.mp3
```