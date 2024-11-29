#main
from mp3_classes import ChildProfileList

if __name__ == '__main__':
    children_list = ChildProfileList() 
    children_list.build_list_from_file() 
    children_list.sort_list() 
    children_list.determine_gift() 
    children_list.write_gift_file()