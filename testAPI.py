import requests
import json



loop = True
#file = open("Personal_MTG_Database.txt", "a")
while loop:
	cardName = input("Enter Card Name: ")
	#url = "https://api.scryfall.com/cards/named?fuzzy=aust+com&format=image"  #If want image
	url = "https://api.scryfall.com/cards/autocomplete?q={}".format(cardName)

	headers = {
		"User-Agent" : "testAPI.py/1.0"
		#"Accept" : "*/*"
	}
	response = requests.get(url,headers)

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
					print("yes", card)
					chosenCard = card
					break
			#print(chosenCard)
			
			with open("MTG_Database.txt", "a+") as file:
				
				
				#file.write("{}, 0\n".format(chosenCard))
				try:
					file.seek(0)
					for line in file:
						
						print(line)
						line = line.split(",")
						print(line)
						word = line[0]
						count = int(line[1])
						if word == chosenCard:
							count += 1
							file.write("{}, {}\n".format(chosenCard, count))
							break
			#FIND EFFICIENT WAY TO OVERWRITE A CARD VALUE THAT ALREADY EXISTS	
						print(word, count)
						#line = list(line)
						#word = line[0:-1]
						#count = line[-1]
					file.write("{}, 1\n".format(chosenCard))
				except:
					print("File is empty")
					file.write("placeholder", 0)
					#for line in file:
						#print(line)
						#if line[0] == chosenCard:
							#line[1] += 1
							#break
					#file.write(chosenCard, 1)	
	    		
			continue	
		except:
			print("Error? ")
		else:
			print("Error? No card matches")
	    
	else:
	    print(f"Error: {response.status_code}")