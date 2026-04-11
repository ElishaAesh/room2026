import room as rm


def load_rooms(file_path):
	room_list = []
	try:
		with open(file_path, 'r') as file:
			for line in file:
				line = line.strip()
				# Skip empty lines
				if not line:
					continue
				parts = line.split(',')
				# Ensure we have all 4 properties (even if guest is empty)
				if len(parts) >= 4:
					r_num = int(parts[0])
					r_type = parts[1]
					r_price = float(parts[2])
					g_name = parts[3]
					room_list.append(rm.Room(r_num, r_type, r_price, g_name))
	except FileNotFoundError:
		print("Data file not found. Starting with an empty room list.")
	return room_list


def save_rooms(file_path, room_list):
	with open(file_path, 'w') as file:
		file.write("room_number,room_type,price,guest_name\n")
		for room in room_list:
			file.write(f"{room.get_room_number()},{room.get_room_type()},{room.get_price()},{room.get_guest_name()}\n")


def find_room_index(room_list, room_number):
	for i in range(len(room_list)):
		if int(room_list[i].get_room_number()) == int(room_number):
			return i
	return -1


def add_room(room_list):
	room_number_str = input("Enter room number: ")
	# Input validation using a condition, avoiding 'while True' or boolean flags
	while not room_number_str.isdigit():
		print("Error: Room number must be numeric.")
		room_number_str = input("Enter room number: ")

	room_number = int(room_number_str)
	index = find_room_index(room_list, room_number)

	if index != -1:
		print("Error: Room already exists.")
	else:
		room_type = input("Enter room type (Single/Double/Suite): ")
		price_str = input("Enter price per night: ")
		# Assuming valid price input for simplicity, as per course constraints
		room_list.append(rm.Room(room_number, room_type, float(price_str), ""))
		print("Room added successfully.")

	return room_list


def remove_room(room_list):
	room_number_str = input("Enter room number to remove: ")
	while not room_number_str.isdigit():
		print("Error: Room number must be numeric.")
		room_number_str = input("Enter room number to remove: ")

	room_number = int(room_number_str)
	index = find_room_index(room_list, room_number)

	if index == -1:
		print("Error: Room not found.")
	else:
		if room_list[index].is_available():
			room_list.pop(index)
			print("Room removed successfully.")
		else:
			print("Error: Cannot remove an occupied room.")

	return room_list


def check_in_guest(room_list):
	room_number_str = input("Enter room number: ")
	while not room_number_str.isdigit():
		print("Error: Room number must be numeric.")
		room_number_str = input("Enter room number: ")

	room_number = int(room_number_str)
	index = find_room_index(room_list, room_number)

	if index == -1:
		print("Error: Room not found.")
	else:
		guest_name = input("Enter guest name: ")
		while guest_name.strip() == "":
			print("Error: Guest name cannot be empty.")
			guest_name = input("Enter guest name: ")

		if room_list[index].is_available():
			room_list[index].check_in(guest_name)
			print("Check-in successful.")
		else:
			print("Room is already occupied.")

	return room_list


def check_out_guest(room_list):
	room_number_str = input("Enter room number: ")
	while not room_number_str.isdigit():
		print("Error: Room number must be numeric.")
		room_number_str = input("Enter room number: ")

	room_number = int(room_number_str)
	index = find_room_index(room_list, room_number)

	if index == -1:
		print("Error: Room not found.")
	else:
		if not room_list[index].is_available():
			room_list[index].check_out()
			print("Check-out successful.")
		else:
			print("Error: Room is already available.")

	return room_list


def view_all_rooms(room_list):
	if len(room_list) == 0:
		print("No rooms available.")
	else:
		occupied = 0
		for room in room_list:
			print(room)
			if not room.is_available():
				occupied += 1

		print("\n--- Summary Statistics ---")
		print(f"Total rooms: {len(room_list)}")
		print(f"Available: {len(room_list) - occupied}")
		print(f"Occupied: {occupied}")


def main():
	room_list = load_rooms("rooms.txt")

	# Initialize choice with a value that ensures the loop runs
	choice = "0"

	while choice != "6":
		print("\n--- YYC Hotel Room Management System ---")
		print("1. Add Room")
		print("2. Remove Room")
		print("3. Check In Guest")
		print("4. Check Out Guest")
		print("5. View All Rooms")
		print("6. Exit")

		choice = input("Enter your choice (1-6): ")

		if choice == "1":
			room_list = add_room(room_list)
		elif choice == "2":
			room_list = remove_room(room_list)
		elif choice == "3":
			room_list = check_in_guest(room_list)
		elif choice == "4":
			room_list = check_out_guest(room_list)
		elif choice == "5":
			view_all_rooms(room_list)
		elif choice == "6":
			save_rooms("bookings.csv", room_list)
			print("Data saved. Exiting program.")
		else:
			print("Invalid choice. Please try again.")


if __name__ == "__main__":
	main()
