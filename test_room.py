#
# test_room - This program tests the majority of the methods in the Room class
#
# Author:
# Version/Date:
#
from repo import room as rm

def main():
    # Create a list of 5 rooms with different types
    room_list = []
    
    # Add rooms with different configurations
    room_list.append(rm.Room(101, "Single", 5000.0, "John Smith"))
    room_list.append(rm.Room(102, "Double", 8000.0, "Maria Garcia"))
    room_list.append(rm.Room(103, "Double", 8000.0, ""))  # Available room
    room_list.append(rm.Room(104, "Suite", 12000.0, "Robert Johnson"))
    room_list.append(rm.Room(105, "Single", 5500.0, ""))  # Available room

    # Test getters
    print("Testing getters:")
    current_room = room_list[0]
    print(f"Room Number: {current_room.get_room_number()}")
    print(f"Room Type: {current_room.get_room_type()}")
    print(f"Price: {current_room.get_price()}")
    print(f"Guest Name: {current_room.get_guest_name()}")
    print()

    # Test is_available() method
    print("Testing is_available():")
    for i in range(len(room_list)):
        if room_list[i].is_available():
            print(f"Room {room_list[i].get_room_number()} is available")
        else:
            print(f"Room {room_list[i].get_room_number()} is occupied by {room_list[i].get_guest_name()}")
    print()

    # Test check_in() method on an available room
    print("Testing check_in():")
    # Find an available room
    found = False
    index = 0
    while index < len(room_list) and not found:
        if room_list[index].is_available():
            found = True
            print(f"Found available room: {room_list[index].get_room_number()}")
            # Check in a guest
            room_list[index].check_in("Alice Wonderland")
            print(f"After check-in: {room_list[index].get_guest_name()}")
        index += 1
    if not found:
        print("No available room found for check-in test")
    print()

    # Test check_out() method on an occupied room
    print("Testing check_out():")
    # Find an occupied room (not the one we just checked in)
    found = False
    index = 0
    while index < len(room_list) and not found:
        if not room_list[index].is_available() and room_list[index].get_guest_name() != "Alice Wonderland":
            found = True
            print(f"Found occupied room: {room_list[index].get_room_number()} occupied by {room_list[index].get_guest_name()}")
            # Check out the guest
            room_list[index].check_out()
            print(f"After check-out, room available: {room_list[index].is_available()}")
        index += 1
    if not found:
        print("No occupied room found for check-out test (excluding the one we just checked in)")
    print()

    # Test setters
    print("Testing setters:")
    current_room = room_list[1]  # Room 102
    print(f"Before - Room: {current_room.get_room_number()}, Type: {current_room.get_room_type()}, Price: {current_room.get_price()}")
    current_room.set_room_number(202)
    current_room.set_room_type("Suite")
    current_room.set_price(15000.0)
    current_room.set_guest_name("New Guest")
    print(f"After - Room: {current_room.get_room_number()}, Type: {current_room.get_room_type()}, Price: {current_room.get_price()}, Guest: {current_room.get_guest_name()}")
    print()

    # Print all rooms using __str__ method
    print("All rooms (using __str__ method):")
    print("-" * 50)
    for room in room_list:
        print(room)
    print("-" * 50)
    
    # Summary statistics
    available_count = 0
    for room in room_list:
        if room.is_available():
            available_count += 1
    
    print(f"\nSummary:")
    print(f"Total rooms: {len(room_list)}")
    print(f"Available: {available_count}")
    print(f"Occupied: {len(room_list) - available_count}")

if __name__ == "__main__":
    main()