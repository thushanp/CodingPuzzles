# Given a sorted array of strings that is interspersed with empty strings, write a
# method to find the location of a given string.

array = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", "eagle", ""]

find = "at"

def finder(array, find, tracker):
	mid = len(array)//2
	tracker = tracker + mid
	while array[mid] == "" and mid != len(array) - 1:
		mid = mid+1
		tracker = tracker + 1
	while array[mid] == "" and mid != 0:
		mid = mid-1
		tracker = tracker - 1
	if array[mid] == find:
		print("found")
		print(tracker)
	elif array[mid] > find:
		finder(array[:mid], find, tracker)
	elif array[mid] < find:
		finder(array[mid:], find, tracker)
	else:
		print("not found")

finder(array,find, 0)