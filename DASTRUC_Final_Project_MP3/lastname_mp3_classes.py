# lastname_mp3_classes.py

import os

#DO NOT EDIT
class ChildProfile:
	first_name: str
	last_name: str
	gender: str
	age: int
	goodDeeds: int
	badDeeds: int
	gift: str
#DO NOT EDIT

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ChildProfileList:
	children = []
	head = None
    
	def build_list_from_file(self):
		# Get the directory of the lastname_main.py file
		dir_path = os.path.dirname(os.path.realpath(__file__))
		# Construct the path to the INPUT.TXT file
		input_file_path = os.path.join(dir_path, "INPUT.TXT")
		with open(input_file_path, "r") as file:
			lines = file.readlines()
			for line in lines:
				first_name, last_name, gender, age, goodDeeds, badDeeds = line.strip().split()
				child = ChildProfile()
				child.first_name = first_name
				child.last_name = last_name
				child.gender = gender
				try:
					child.age = int(age)
					child.goodDeeds = int(goodDeeds)
					child.badDeeds = int(badDeeds)
				except ValueError:
					print("ValueError: Invalid data in INPUT.TXT file")
					exit(1)
				new_node = Node(child)
				if self.head is None:
					self.head = new_node
				else:
					current = self.head
					while current.next is not None:
						current = current.next
					current.next = new_node


	def swap(self, node_1, node_2):
		temp = node_1.data
		node_1.data = node_2.data
		node_2.data = temp
  
	def sort_list(self):
		if self.head is None:
			return
		swapped = True
		while swapped:
			swapped = False
			current = self.head
			while current.next is not None:
				if current.data.last_name > current.next.data.last_name or (current.data.last_name == current.next.data.last_name and current.data.first_name > current.next.data.first_name):
					self.swap(current, current.next)
					swapped = True
				current = current.next


  
	def determine_gift(self):
		current = self.head
		while current is not None:
			if current.data.age <= 5:
				if current.data.gender == 'M':
					if current.data.age == 1:
						current.data.gift = 'Blue_Pacifier'
					elif current.data.age == 2:
						current.data.gift = 'Colored_Shapes'
					elif current.data.age == 3:
						current.data.gift = 'Choo_Choo_Train'
					elif current.data.age == 4:
						current.data.gift = 'Wooden_Horse'
					else:
						current.data.gift = 'Remote_Controlled_Car'
				else:
					if current.data.age == 1:
						current.data.gift = 'Pink_Pacifier'
					elif current.data.age == 2:
						current.data.gift = 'Colored_Shapes'
					elif current.data.age == 3:
						current.data.gift = 'Teddy_Bear'
					elif current.data.age == 4:
						current.data.gift = 'Doll'
					else:
						current.data.gift = 'Pair_of_Shoes'
			elif 6 <= current.data.age <= 12:
				deeds = current.data.goodDeeds - current.data.badDeeds
				if deeds <= 0:
					current.data.gift = 'Good_Manners_and_Right_Conduct_Book'
				else:
					if 6 <= current.data.age <= 8:
						if current.data.gender == 'M':
							current.data.gift = 'Chess_Set'
						else:
							current.data.gift = 'Disney_Puzzle'
					else:
						if current.data.gender == 'M':
							current.data.gift = 'Soccer_Ball'
						else:
							current.data.gift = 'Blouse_Pants'
			else:
				current.data.gift = 'E_Christmas_Card'

			current = current.next

  
	def write_gift_file(self):
		# Get the directory of the lastname_main.py file
		dir_path = os.path.dirname(os.path.realpath(__file__))
		# Construct the path to the OUTPUT.TXT file
		output_file_path = os.path.join(dir_path, "OUTPUT.TXT")
		with open(output_file_path, "w") as file:
			current = self.head
			while current is not None:
				file.write(f"{current.data.last_name} {current.data.first_name} {current.data.gender} {current.data.gift}\n")
				current = current.next

		print("Output file written, check OUTPUT.TXT")