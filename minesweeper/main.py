import sys

from PyQt5.QtWidgets import QApplication

from view import View
from controller import Controller
from model import Model


if __name__ == '__main__':
	application = QApplication(sys.argv)

	model = Model()
	controller = Controller(model)
	window = View(controller, model)

	window.show()
	sys.exit(application.exec_())