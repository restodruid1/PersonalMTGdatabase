import requests
import json



loop = True
#file = open("Personal_MTG_Database.txt", "a")
while loop:
	cardName = input("Enter Card Name(Enter q to quit): ")
	if cardName == "q":
		print("Exiting Program")
		break
	#url = "https://api.scryfall.com/cards/named?fuzzy=aust+com&format=image"  #If want image
	url = "https://api.scryfall.com/cards/autocomplete?q={}".format(cardName)

	headers = {
		"User-Agent" : "testAPI.py/1.0"
		#"Accept" : "*/*"
	}
	response = requests.get(url,headers)

	# API Request to Search for Card with AutoComplete is Valid
	if response.status_code == 200:
		try:
			# Turn response into dictionary
			jsonStr = response.content.decode('utf-8')
			data = json.loads(jsonStr)
			print("Cards with {}:".format(cardName))
			for number, card in enumerate(data["data"],start=1):
				print("{}) {}".format(number, card))
			
			num = int(input("Enter the number for the card you want: "))
			chosenCard = ""
			for number, card in enumerate(data["data"], start=1):
				if number == num:
					print("You  Selected: ", card)
					chosenCard = card
					break
			#print(chosenCard)
			emptyFile = True
			size = 0
			
			with open("MTG_Database.txt", "r") as infile:
				try:
					lines = infile.readlines()
					size = len(lines)
					
					if size == 0:
						lines = ["{}$ 1\n".format(chosenCard)]
						#print(lines)
						
					else:
						found = False
						for index, card in enumerate(lines):
							#print(index, card)
							line = card.split("$")
							cardNameTmp = line[0]
							count = int(line[1]) + 1
							if cardNameTmp == chosenCard:					
								lines[index] = "{}$ {}\n".format(cardNameTmp, count)
								found = True
								break
						if not found:   		
							lines.append("{}$ 1\n".format(chosenCard))
							lines.sort()
				except:
					print("card database not working")

			with open("MTG_Database.txt", "w") as outfile:			
					for card in lines:
						outfile.write(card)	
						
			continue	
				
		except:
			print("Error? ")
		
	    
	else:
	    print(f"Error: {response.status_code}")