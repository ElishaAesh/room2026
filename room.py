"""Room model for hotel reservation testing."""


class Room:
	def __init__(self, room_number: int, room_type: str, price: float, guest_name: str = "") -> None:
		self._room_number = room_number
		self._room_type = room_type
		self._price = price
		self._guest_name = guest_name

	def get_room_number(self) -> int:
		return self._room_number

	def set_room_number(self, room_number: int) -> None:
		self._room_number = room_number

	def get_room_type(self) -> str:
		return self._room_type

	def set_room_type(self, room_type: str) -> None:
		self._room_type = room_type

	def get_price(self) -> float:
		return self._price

	def set_price(self, price: float) -> None:
		self._price = price

	def get_guest_name(self) -> str:
		return self._guest_name

	def set_guest_name(self, guest_name: str) -> None:
		self._guest_name = guest_name

	def is_available(self) -> bool:
		return self._guest_name.strip() == ""

	def check_in(self, guest_name: str) -> None:
		if not self.is_available():
			raise ValueError(f"Room {self._room_number} is already occupied")
		self._guest_name = guest_name

	def check_out(self) -> None:
		if self.is_available():
			raise ValueError(f"Room {self._room_number} is already available")
		self._guest_name = ""

	def __str__(self) -> str:
		status = "Available" if self.is_available() else f"Occupied by {self._guest_name}"
		return f"Room {self._room_number} | {self._room_type} | Price: {self._price} | {status}"
