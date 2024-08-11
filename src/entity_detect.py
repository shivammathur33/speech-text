import ollama
import re

PROMPT="""
TASK: Given an UTTERANCE, detect origin and destination address
OUTPUT FORMAT: 
<ORIGIN>address of the origin</ORIGIN>
<DESTINATION>address of the destination</DESTINATION>
(DO NOT OUTPUT ANYTHING EXTRA!)
UTTERANCE:"""

def entity_detect(utterance):
    print('Searching for origin and destination...')
    response=ollama.generate(model='mistral', 
                             prompt=PROMPT+utterance)['response']
    print(response)
    return post_process(response)

def post_process(generated_text):
    address_list=[]
    try:
        origin = r"<origin>(.*?)</origin>"
        destination = r"<destination>(.*?)</destination>"
        address_list.append(re.search(origin, generated_text.lower()).group(1))
        address_list.append(re.search(destination, generated_text.lower()).group(1))
    except Exception as e:
        print(e)
    return address_list

# Test generative call
# print(entity_detect("Hi, can you book me a cab from 2211 Edgewood St to 5480 7th Ave"))


