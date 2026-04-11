# constants
COVERAGE = 350
COST_PER_GALLON = 42


def computeRectangleArea(length, width):
	return length * width


def computeSquareArea(side):
	return side * side


def computeWindowsDoorsArea():
	total_area = 0
	count = int(input("How many windows and doors does the room contain? \n"))

	for i in range(1, count + 1):
		length = float(input(f"Enter window/door length for window/door {i} in feet\n"))
		width = float(input(f"Enter window/door width for window/door {i} in feet\n"))
		total_area += computeRectangleArea(length, width)

	return total_area


def computeRectangleWallsArea():
	length = float(input("Enter the length of the room in feet:\n"))
	width = float(input("Enter the width of the room in feet:\n"))
	height = float(input("Enter the height of the room in feet:\n"))

	wall1 = computeRectangleArea(length, height)
	wall2 = computeRectangleArea(width, height)

	total = 2 * (wall1 + wall2)

	subtract = computeWindowsDoorsArea()

	return total - subtract


def computeSquareWallsArea():
	side = float(input("Enter the length of one side of the room: \n"))

	wall_area = computeRectangleArea(side, side)
	total = 4 * wall_area

	subtract = computeWindowsDoorsArea()

	return total - subtract


def computeCustomWallsArea():
	walls = int(input("How many walls are there in the room\n"))
	total = 0

	for i in range(1, walls + 1):
		height = float(input(f"Enter the height of wall {i} in feet\n"))
		length = float(input(f"Enter the length of wall {i} in feet\n"))
		total += computeRectangleArea(length, height)

	subtract = computeWindowsDoorsArea()

	return total - subtract


def computeGallons(area):
	return area / COVERAGE


def computePaintPrice(area):
	gallons = computeGallons(area)
	return gallons * COST_PER_GALLON


def computeRoomArea(room_num):
	print(f"Room: {room_num}")
	print("Select the shape of the room: ")
	print("1 - Rectangular")
	print("2 - Square")
	print("3 - Custom (more or less than 4 walls, all square or rectangles)")

	choice = int(input())

	if choice == 1:
		area = computeRectangleWallsArea()
	elif choice == 2:
		area = computeSquareWallsArea()
	elif choice == 3:
		area = computeCustomWallsArea()
	else:
		print("Invalid choice. Defaulting to 0.")
		area = 0

	gallons = computeGallons(area)
	cost = computePaintPrice(area)

	print(f"For Room: {room_num}, the area to be painted is {area:.1f} square ft and will require {gallons:.2f} gallons to paint. This will cost the customer ${cost:.2f}")

	return area, gallons, cost


def main():
	print("Welcome to Shiny Paint Company for indoor painting!")
	rooms = int(input("How many Rooms do you want to paint:\n"))
	print("Thank you!")

	total_area = 0
	total_gallons = 0
	total_cost = 0

	for i in range(1, rooms + 1):
		area, gallons, cost = computeRoomArea(i)
		total_area += area
		total_gallons += gallons
		total_cost += cost

	print(f"Area to be painted is {total_area:.2f} square ft and will require {total_gallons:.2f} gallons to paint. This will cost the customer ${total_cost:.2f}")


main()
