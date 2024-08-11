from entity_detect import entity_detect
from transcription import transcribe

def main():
    # Hi, can you book me a cab from 2211 Edgewood St to 5480 7th Ave
    # Hi, can you book me a cab from Park Lane to Northpark Mall
    # I need to go to Northpark Mall, I am at DFW Airport
    utterance=transcribe()
    print("Speech-Text:",utterance)
    address=entity_detect(utterance)
    print("Origin:",address[0])
    print("Destination:",address[1])


if __name__ == "__main__":
    main()