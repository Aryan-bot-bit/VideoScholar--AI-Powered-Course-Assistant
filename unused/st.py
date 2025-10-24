import whisper
import json
#v2 is a model 
model = whisper.load_model("medium")

result = model.transcribe(audio="audios/p6.mp4_62 #p6.mp4.mp3",
                          language="hi",
                          task="translate",
                          word_timestamps=False )


chunks = []
for segment in result["segments"]:
    chunks.append({"start": segment["start"], "end": segment["end"], "text": segment["text"]})

print(chunks)

with open("output.json", "w") as f:
    json.dump(chunks,f)
