# From Speech to Locational Entities
Extract origin and destination from spoken utterences

Input: [Voice]  Hi, can you book me a cab from 2211 Edgewood St to 5480 7th Ave

Output: Origin: 2211 edgewood street, Destination: 5480 7th avenue
```
Listening...
Speech-Text: hi can you book me a cab from 2211 Edgewood Street to 5480 7th Avenue
Searching for origin and destination...
 <ORIGIN>2211 Edgewood Street</ORIGIN>
<DESTINATION>5480 7th Avenue</DESTINATION>
Origin: 2211 edgewood street
Destination: 5480 7th avenue
```

#### Initial Setup
1) Create a venv
```
conda create --name venv-speech python=3.11
```
2) Activate
```
conda activate venv-speech
```
3) Install portaudio
```
brew install portaudio
```
4) Install all requirements
```
pip install -r requirements.txt
```

#### Running the full pipeline
1) Navigate to ```speech-text/src```

2) Run the pipeline: ```python pipeline.py```

3) You may see a prompt asking you to allow access to your microphone.

4) When you see the prompt "Listening", start speaking.
```
Listening...
```

5) Takes a few seconds to transcribe your voice into text.
```
Listening...
Speech-Text: hi can you book me a cab from 2211 Edgewood Street to 5480 7th Avenue
```

6) Will take another few seconds to extract the origin and destination entities.
```
Searching for origin and destination...
```

7) Final output:
```
 <ORIGIN>2211 Edgewood Street</ORIGIN>
<DESTINATION>5480 7th Avenue</DESTINATION>
Origin: 2211 edgewood street
Destination: 5480 7th avenue
```
