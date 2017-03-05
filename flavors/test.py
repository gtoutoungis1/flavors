import unittest
import json
from parse_flavor_wheel import traverse, score

import datetime as dt


class Test(unittest.TestCase):
	def setUp(self):

		self.json_tree = {
			  "flavor": None,
			  "css_color": None,
			  "children": [
			    {
			      "flavor": "Roasted",
			      "css_color": "#c74a36",
			      "children": [
			        
			        {
			          "flavor": "Tobacco"
			        },
			        {
			          "flavor": "Burnt",
			          "children": [
			           
			            {
			              "flavor": "Smoky"
			            },
			            {
			              "flavor": "Brown, Roast"
			            }
			          ]
			        },
			        {
			          "flavor": "Cereal",
			          "children": [
			            {
			              "flavor": "Malt"
			            },
			            {
			              "flavor": "Grain"
			            }
			          ]
			        }
			      ]
			    },
			   ]
			  }

		self.tree_dict = {'Chamomile': 'Floral', 'Anise': 'Brown Spice', 'Petroleum': 'Chemical',
		 'Chemical': 'Other', 'Citric Acid': 'Sour', 'Blackberry': 'Berry', 'Brown Sugar': 'Sweet', 
		 'Grape': 'Other Fruit', 'Vegetative': 'Green/Vegetative', 'Isovaleric Acid': 'Sour',
		  'Papery': 'Paper/Musty', 'Other Fruit': 'Fruity', 'Animalic': 'Paper/Musty', 
		  'Musty/Earthy': 'Paper/Musty', 'Malic Acid': 'Sour', 'Pear': 'Other Fruit', 
		  'Herb-Like': 'Green/Vegetative', 'Chocolate': 'Cocoa', 'Beany': 'Green/Vegetative',
		   'Cherry': 'Other Fruit', 'Floral': 'None', 'Sweet Aromatics': 'Sweet', 'Burnt': 'Roasted',
		    'Prune': 'Dried Fruit', 'Overall Sweet': 'Sweet', 'Maple Syrup': 'Brown Sugar', 
		    'Vanilla': 'Sweet', 'Raisin': 'Dried Fruit', 'Coconut': 'Other Fruit', 
		    'Whiskey': 'Alcohol/Fermented', 'Ashy': 'Burnt', 'Cinnamon': 'Brown Spice', 
		    'Medicinal': 'Chemical', 'Stale': 'Paper/Musty', 'Spices': 'None', 'Acetic Acid': 'Sour',
		    'Rubber': 'Chemical', 'Meaty Brothy': 'Paper/Musty', 'Raspberry': 'Berry', 
		    'Skunky': 'Chemical', 'Nutty': 'Nutty/Cocoa', 'Vanillin': 'Sweet', 'Pepper': 'Spices', 
		    'Honey': 'Brown Sugar', 'Raw': 'Green/Vegetative', 'Other': 'None', 'Salty': 'Chemical', 
		    'Grain': 'Cereal', 'Lime': 'Citrus Fruit', 'Clove': 'Brown Spice', 'Lemon': 'Citrus Fruit', 
		    'Fermented': 'Alcohol/Fermented', 'Peach': 'Other Fruit', 'Musty/Dusty': 'Paper/Musty', 
		    'Rose': 'Floral', 'Peapod': 'Green/Vegetative', 'Grapefruit': 'Citrus Fruit', 
		    'Peanuts': 'Nutty', 'Orange': 'Citrus Fruit', 'Alcohol/Fermented': 'Sour/Fermented', 
		    'Bitter': 'Chemical', 'Under-Ripe': 'Green/Vegetative', 'Moldy/Damp': 'Paper/Musty', 
		    'Pipe Tobacco': 'Roasted', 'Carmelized': 'Brown Sugar', 'Tobacco': 'Roasted', 
		    'Pomegranate': 'Other Fruit', 'Jasmine': 'Floral', 'Winey': 'Alcohol/Fermented', 
		    'Blueberry': 'Berry', 'Molasses': 'Brown Sugar', 'Cereal': 'Roasted', 'Hazelnut': 'Nutty',
		     'Overripe': 'Alcohol/Fermented', 'Cardboard': 'Paper/Musty', 'Malt': 'Cereal', 
		     'Olive Oil': 'Green/Vegetative', 'Phenolic': 'Paper/Musty', 'None': 'None', 'Nutty/Cocoa': 'None', 
		     'Sour/Fermented': 'None', 'Pungent': 'Spices', 'Smoky': 'Burnt', 'Brown Spice': 'Spices', 
		     'Black Tea': 'Floral', 'Sour Aromatics': 'Sour', 'Strawberry': 'Berry', 'Sour': 'Sour/Fermented',
		      'Nutmeg': 'Brown Spice', 'Berry': 'Fruity', 'Pineapple': 'Other Fruit', 'Fresh': 'Green/Vegetative',
		       'Dark Chocolate': 'Cocoa', 'Fruity': 'None', 'Hay-Like': 'Green/Vegetative', 'Butyric Acid': 'Sour', 
		       'Apple': 'Other Fruit', 'Sweet': 'None', 'Almond': 'Nutty', 'Dried Fruit': 'Fruity', 'Cocoa': 'Nutty/Cocoa',
		        'Citrus Fruit': 'Fruity', 'Paper/Musty': 'Other', 'Roasted': 'None', 'Green/Vegetative': 'None',
		         'Woody': 'Paper/Musty', 'Brown, Roast': 'Burnt', 'Acrid': 'Burnt', 'Dark Green': 'Green/Vegetative'}

	def test_traverse(self):
		j = json.dumps(self.json_tree)
		result = [('None', 'None'), ('Roasted', 'None'), ('Tobacco', 'Roasted'), 
				('Burnt', 'Roasted'), ('Smoky', 'Burnt'), ('Brown, Roast', 'Burnt'), 
				('Cereal', 'Roasted'), ('Malt', 'Cereal'), ('Grain', 'Cereal')]
		self.tree_dict = dict(result)

		self.assertEqual(traverse(json.loads(j)), result)

	
	def test_score_with_equal_node_parent_name(self):
		text = "Balanced and elegant, crisp black tea, citrus, and silky dark chocolate flavors"
		result = [['Nutty/Cocoa', 'Cocoa', 'Dark Chocolate'], ['Green/Vegetative', 'Dark Green'], ['Fruity', 'Citrus Fruit']]
		print score(text, self.tree_dict)

		self.assertEqual(score(text, self.tree_dict), result)


	def test_score_with_notfoundscore(self):
		text = ''
		print score(text, self.tree_dict)
		result = []

		self.assertEqual(score(text, self.tree_dict), result)

	def test_score(self):
		text = "An excellent cup of coffee. Notes of stone fruit, cherry and plum. Long finish with hints of milk chocolate and brown sugar."
		result = [
			    ["Fruity", "Other Fruit", "Cherry"],
			    ["Sweet", "Brown Sugar"],
			    ["Nutty/Cocoa", "Cocoa", "Chocolate"]
			]

		self.assertItemsEqual(score(text, self.tree_dict), result)


if __name__ == '__main__':
    unittest.main()


