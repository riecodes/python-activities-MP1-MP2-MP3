# lastname_main.py

from lastname_mp3_classes import ChildProfileList

if __name__ == '__main__':
	child_list = ChildProfileList()
	child_list.build_list_from_file()
	child_list.sort_list()
	child_list.determine_gift()
	child_list.write_gift_file()
	