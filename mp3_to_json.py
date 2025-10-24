
import whisper
import json
import os
#v2 is a model 
model = whisper.load_model("medium")

audios = os.listdir("audios")

#Add this line to create folder if not exists
os.makedirs("jsons", exist_ok=True)

for audio in audios: 
    # print(audio)
    if("_" in audio):
        number = audio.split("_")[0]
        title = audio.split("_")[1][:-4]
        print(number, title)
        result = model.transcribe(audio = f"audios/{audio}", 
        # result = model.transcribe(audio = f"audios/p6.mp4_62 #p6.mp4.mp3", 
                              language="hi",
                              task="translate",
                              word_timestamps=False )
        
        chunks = []
        for segment in result["segments"]:
            chunks.append({"number": number, "title":title, "start": segment["start"], "end": segment["end"], "text": segment["text"]})
        
        chunks_with_metadata = {"chunks": chunks, "text": result["text"]}

        with open(f"jsons/{audio}.json", "w") as f:
            json.dump(chunks_with_metadata,f)
