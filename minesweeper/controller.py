class Controller:
	"""Controller class for the connection between
	   Model and View."""

	def __init__(self, model):
		self.model = model
		self.model.set_contoller(self)

	def setView(self, view):
		self.view = view

	def left_click(self, x, y):
		self.model.open_cell(x, y)
		status = self.get_status()
		if status == "Win":
			self.view.top_box.top_panel.start_btn.set_won()
		elif status =="Lose":
			self.view.top_box.top_panel.start_btn.set_lost()

	def right_click(self, x, y):
		self.model.next_mark(x, y)
		self.set_mines_board(self.model.MINES_MAX - self.model.flagged_cells)

	def create_timer(self):
		self.view.top_box.top_panel.run_timer()

	def stop_timer(self):
		try:
			self.view.top_box.top_panel.stop_timer()
		except:
			pass

	def clear_timer(self):
		try:
			self.view.top_box.top_panel.clear_timer()
		except:
			pass

	def set_start_button(self):
		try:
			self.view.top_box.top_panel.start_btn.set_start()
		except:
			pass

	def set_mines_board(self, mines):
		self.view.top_box.top_panel.board.set(mines)
		self.view.update()

	def get_status(self):
		return self.model.game_status()

	def start_new_game(self):
		self.model.new_game(game_level=1)
		self.view.update()

	def start_new_game_smile(self):
		self.model.new_game(game_level=0)
		self.view.update()

	def start_new_game_junior(self):
		self.model.new_game(game_level=1)
		self.model.last_level = 1
		self.set_fixed_size()
		self.view.update()

	def start_new_game_middle(self):
		self.model.new_game(game_level=2)
		self.model.last_level = 2
		self.set_fixed_size()
		self.view.update()

	def start_new_game_senior(self):
		self.model.new_game(game_level=3)
		self.model.last_level = 3
		self.set_fixed_size()
		self.view.update()

	def set_fixed_size(self):
		self.view.top_box.field.setFixedWidth(32 * self.model.FIELD_WIDTH)
		self.view.top_box.field.setFixedHeight(32 * self.model.FIELD_HEIGHT)
		self.view.setFixedWidth(32 * self.model.FIELD_WIDTH + 20)
		self.view.setFixedHeight(32 * self.model.FIELD_HEIGHT + 90)
