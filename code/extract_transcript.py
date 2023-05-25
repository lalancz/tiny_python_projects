import json
import youtube_transcript_api

# tool to compile instances of a given word being said in youtube videos (eg making compilations of something being said)

# read txt files for video IDS
def get_IDs(filename):
	with open(filename, "r") as file:
		return file.readlines()

# find line of transcript containing given word
def find_word(transcript, id, word):
	for i in transcript:
		if word in i['text']:
			return (id, i['start'])
	return None
	
if __name__ == "__main__":
	base_video_url = "https://www.youtube.com/watch?v="

	with open("word.txt", "w") as output:
		IDs = get_IDs("urls.txt")

		for id in IDs:
			try:
				transcript = youtube_transcript_api.YouTubeTranscriptApi.get_transcript(id)
			except (youtube_transcript_api._errors.TranscriptsDisabled, youtube_transcript_api._errors.NoTranscriptFound):
				continue
			
			word_instance = find_word(transcript, id)

			if word_instance != None:
				output.write(f"{base_video_url + word_instance[0]}?t={round(word_instance[1])}\n\n")

	print("done")


