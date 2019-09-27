from unittest import TestCase

from minesweeper.cell import*


class TestCell(TestCase):

	@classmethod
	def setUpClass(cls):
		cls.cell = Cell(5, 10)

	def test_init(self):
		self.assertEqual(self.cell.x, 5)
		self.assertEqual(self.cell.y, 10)

	def test_open_state_is_flagged(self):
		expected_state = "flagged"
		self.cell.state = expected_state
		self.cell.open()
		self.assertEqual(self.cell.state, expected_state)

	def test_open_state_is_opened(self):
		expected_state = "opened"
		self.cell.state = expected_state
		self.cell.open()
		self.assertEqual(self.cell.state, expected_state)

	def test_open_state_is_closed(self):
		primary_state = "closed"
		expected_state = "opened"
		self.cell.state = primary_state
		self.cell.open()
		self.assertEqual(self.cell.state, expected_state)

	def test_open_state_is_questioned(self):
		primary_state = "questioned"
		expected_state = "opened"
		self.cell.state = primary_state
		self.cell.open()
		self.assertEqual(self.cell.state, expected_state)

	def test_next_mark_state_is_opened(self):
		primary_state = "opened"
		self.cell.state = primary_state
		self.cell.next_mark()
		self.assertEqual(self.cell.state, primary_state)

	def test_next_mark_state_is_closed(self):
		primary_state = "closed"
		expected_state = "flagged"
		self.cell.state = primary_state
		self.cell.next_mark()
		self.assertEqual(self.cell.state, expected_state)

	def test_next_mark_state_is_questioned(self):
		primary_state = "questioned"
		expected_state = "closed"
		self.cell.state = primary_state
		self.cell.next_mark()
		self.assertEqual(self.cell.state, expected_state)
