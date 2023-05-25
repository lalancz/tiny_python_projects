import os
import json
from datetime import date

# simple commandline journal
# best to automate the launching through OS (eg windows task scheduler)

class Journal():
	filename = os.path.dirname(__file__) + "\\diary.json"

	def writeEntry(self):
		with open(self.filename, "r") as file:
			data = json.load(file)

			today = date.today()
			print(f"Journal Friend - Date: {today}")

			meal = str(input("Enter the meal you ate today: "))
			mood = str(input("Enter your mood today: "))
			summary = str(input("Enter a summary of your day: "))

			dataDict = {
				'meal' : meal,
				'mood' : mood,
				'summary' : summary
			}

			data[str(today)] = dataDict

		with open(self.filename, "w") as file:
			json.dump(data, file)


if __name__ == "__main__":
	journal = Journal()
	journal.writeEntry()