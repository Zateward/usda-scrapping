import requests

query = input('Type the aliment you want to search for: ')
response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?', params={'query': query, 'api_key': 'Qh1IiGUEYxSICDvd2VQ60CHlbfsy9Vbp3BcGiKca'})
data = response.json()

for item in data['foods']:
	name = item.get('description', 'N/A')
	category = item.get('foodCategory', 'N/A')

	nutrients = item.get('foodNutrients', [])
	fats = next((nutrient['value'] for nutrient in nutrients if nutrient['nutrientName'] == 'Total lipid (fat)'), 0)
	carbohydrates = next((nutrient['value'] for nutrient in nutrients if nutrient['nutrientName'] == 'Carbohydrate, by difference'), 0)
	proteins = next((nutrient['value'] for nutrient in nutrients if nutrient['nutrientName'] == 'Protein'), 0)

	print(f"- {name}, {category}, {fats}, {carbohydrates}, {proteins}")

print(fats+carbohydrates+proteins)