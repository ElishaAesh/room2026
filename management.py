import room as rm

DATA_FILE = "rooms.txt"

def load_rooms(file_path=DATA_FILE):
	rooms = []
	try:
		with open(file_path, 'r') as file:
			for line in file:
				parts = line.strip().split(',')
				if len(parts) < 3:
					continue # skip invalid lines
				room_num = int(parts[0])
				room_type = parts[1]
				room_price = float(parts[2])
				guest_name = parts[3] if len(parts) > 3 else ""

				# create room object and add to list
				rooms.append(rm.Room(room_num, room_type, room_price, guest_name))
	except FileNotFoundError:
		print(f"file {file_path} not found. Starting with an empty room list.")
	return rooms


def save_rooms(file_path, room_list):
	with open(file_path, 'w') as file:
		for r in room_list:
			file.write(f"{r.get_room_number()},{r.get_room_type()},{r.get_room_price()},{r.get_guest_name()}\n")


def find_room_index(room_list, room_number):
	for index, room in enumerate(room_list):
		if room.get_room_number() == room_number:
			return index
	return -1


def add_room(room_list):
	room_number_input = input("Enter room number: \033[1m\033[4m").strip()
	# Input validation using a condition, avoiding 'while True' or boolean flags
	if not room_number_input.isdigit():
		print("Invalid rooom number.\n")
		return room_list

	room_number = int(room_number_input)
	index = find_room_index(room_list, room_number)

	if index != -1:
		print("Room already exists.\n")
		return room_list

	valid_types = ["Single", "Double", "Suite"]

	room_type = input("Enter room type: \033[1m\033[4m").strip().title()
	print("\033[0m", end="")
	
	if room_type not in valid_types:
		print("Room type must be one of these values ['Single', 'Double', 'Suite']\n")
		return room_list
	
	price_input = input("Enter room price: \033[1m\033[4m").strip()
	print("\033[0m", end="")
	
	try:
		room_price = float(price_input)
		if room_price <= 0:
			print("Price should be > 0.\n")
			return room_list
	except ValueError:
		print("Price must be a number.\n")
		return room_list
	
	new_room = rm.Room(room_number, room_type, room_price, "")
	room_list.append(new_room)
	print(f"Room added.\n")
	return room_list

def remove_room(room_list):
	room_number_input = input("Enter room number to remove: \033[1m\033[4m").strip()
	print("\033[0m", end="")
	
	if not room_number_input.isdigit():
		print("Invalid room number.\n")
		return room_list

	room_number = int(room_number_input)
	index = find_room_index(room_list, room_number)

	if index == -1:
		print("Room not found.\n")
		return room_list
	
	room = room_list[index]

	if not room.is_available():
		print("Room is already occupied.\n")
		return room_list

	room_list.pop(index)
	print(f"Room removed.\n")
	return room_list

def check_in_guest(room_list):

	room_number_input = input("Enter room number to check in: \033[1m\033[4m").strip()
	print("\033[0m", end="")
	guest_name = input ("Enter guest name: \033[1m\033[4m").strip()
	print("\033[0m", end="")

	if not room_number_input.isdigit():
		print("Invalid data - Enter valid values for room or guest name.\n")
		return room_list
	
	room_number = int(room_number_input)
	index = find_room_index(room_list, room_number)
	if index == -1:
		print("Room not found.\n")
		return room_list
	
	room = room_list[index]
	room.set_guest_name(guest_name)
	print(f"Guest checked in.\n")
	return room_list

def check_out_guest(room_list):

	room_number_input = input("Enter room number: \033[1m\033[4m").strip()
	print("\033[0m", end="")
	if not room_number_input.isdigit():
		print("Invalid room number.\n")
		return room_list
	
	room_number = int(room_number_input)
	index = find_room_index(room_list, room_number)
	if index == -1:
		print("Room not found.\n")
		return room_list
	
	room = room_list[index]

	if room.is_available():
		print("Room is already available.\n")
		return room_list
	room.set_guest_name("")
	print(f"Guest checked out.\n")
	return room_list

def view_all_rooms(room_list):
	print("\nAll Rooms")

	available_count = 0
	occupied_count = 0

	for room in room_list:
		room_number = room.get_room_number()
		room_type = room.get_room_type()
		room_price = room.get_room_price()

		if room.is_available():
			status = "Available"
			print(f"Room {room_number} - {room_type} | price: {room_price} - {status}")
			available_count += 1
		else:
			guest = room.get_guest_name()
			status = "Occupied"
			print(f"Room {room_number} - {room_type} | price: {room_price} - {status}")
			occupied_count += 1

	print("=" * 16)
	print("    SUMMARY    ")
	print("=" * 16)
	print(f"Total Rooms: {len(room_list)}")
	print(f"Available rooms: {available_count}")
	print(f"Occupied rooms: {occupied_count}\n")
	print("-" * 40)

def main():
	room_list = load_rooms(DATA_FILE)

	print("*" * 40)
	print("      Welcome to YYC Hotel System      ")
	print("*" * 40)
	print(f"{len(room_list)} rooms have been loaded\n")

	while True:

		print("1) Add Room")
		print("2) Remove Room")
		print("3) Check In Guest")
		print("4) Check Out Guest")
		print("5) View All Rooms")
		print("6) Exit")

		option = input("Select an option: \033[1m\033[4m").strip()
		print("\033[0m", end="")

		if not option.isdigit():
			print("Invalid option.\n")
			continue

		option = int(option)

		if option == 1:
			room_list = add_room(room_list)
			
		elif option == 2:
			room_list = remove_room(room_list)

		elif option == 3:
			room_list = check_in_guest(room_list)

		elif option == 4:
			room_list = check_out_guest(room_list)

		elif option == 5:
			view_all_rooms(room_list)

		elif option == 6:
			save_rooms(DATA_FILE, room_list)
			print("Saved. Goodbye.")
			break

		else:
			print("Invalid option.")


if __name__ == "__main__":
	main()
