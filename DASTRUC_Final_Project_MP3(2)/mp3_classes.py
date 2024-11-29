#mp3_classes
import os

class ChildProfile:
    fstName: str
    lstName: str
    gender: str
    age: int
    goodDeeds: int
    badDeeds: int
    gift: str

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
                fstName, lstName, gender, age, goodDeeds, badDeeds = line.strip().split()
                child = ChildProfile()
                child.fstName = fstName
                child.lstName = lstName
                child.gender = gender
                try:
                    child.age = int(age)
                    child.goodDeeds = int(goodDeeds)
                    child.badDeeds = int(badDeeds)
                except ValueError:
                    print("INVALID: data is not right in INPUT.TXT")
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
                if (
                    current.data.lstName > current.next.data.lstName
                    or (
                        current.data.lstName == current.next.data.lstName
                        and current.data.fstName > current.next.data.fstName
                    )
                ):
                    self.swap(current, current.next)
                    swapped = True
                current = current.next

    def determine_gift(self):
        current = self.head
        while current is not None:
            if current.data.age <= 5:
                if current.data.gender == "M":
                    if current.data.age == 1:
                        current.data.gift = "Blue_Pacifier"
                    elif current.data.age == 2:
                        current.data.gift = "Colored_Shapes"
                    elif current.data.age == 3:
                        current.data.gift = "Choo_Choo_Train"
                    elif current.data.age == 4:
                        current.data.gift = "Wooden_Horse"
                    else:
                        current.data.gift = "Remote_Controlled_Car"
                else:
                    if current.data.age == 1:
                        current.data.gift = "Pink_Pacifier"
                    elif current.data.age == 2:
                        current.data.gift = "Colored_Shapes"
                    elif current.data.age == 3:
                        current.data.gift = "Teddy_Bear"
                    elif current.data.age == 4:
                        current.data.gift = "Doll"
                    else:
                        current.data.gift = "Pair_of_Shoes"
            elif 6 <= current.data.age <= 12:
                deeds = current.data.goodDeeds - current.data.badDeeds
                if deeds <= 0:
                    current.data.gift = "Good_Manners_and_Right_Conduct_Book"
                else:
                    if 6 <= current.data.age <= 8:
                        if current.data.gender == "M":
                            current.data.gift = "Chess_Set"
                        else:
                            current.data.gift = "Disney_Puzzle"
                    else:
                        if current.data.gender == "M":
                            current.data.gift = "Soccer_Ball"
                        else:
                            current.data.gift = "Blouse_Pants"
            else:
                current.data.gift = "E_Christmas_Card"

            current = current.next

    def write_gift_file(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        output_file_path = os.path.join(dir_path, "OUTPUT.TXT")
        with open(output_file_path, "w") as file:
            current = self.head
            while current is not None:
                file.write(
                    f"{current.data.lstName} {current.data.fstName} {current.data.gender} {current.data.gift}\n"
                )
                current = current.next
