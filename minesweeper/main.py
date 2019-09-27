import sys

from PyQt5.QtWidgets import QApplication

from view import View


if __name__ == '__main__':
	application = QApplication(sys.argv)
	window = View()
	window.show()
	sys.exit(application.exec_())