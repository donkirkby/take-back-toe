import sys
from PyQt5 import QtCore, QtWidgets


class Pile(QtWidgets.QGraphicsEllipseItem):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)

        # set item's rectangle
        self.setRect(QtCore.QRectF(50, 50, 50, 50))


class MainForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        # noinspection PyArgumentList
        super().__init__(parent)

        scene = QtWidgets.QGraphicsScene(-50, -50, 600, 600)

        ellipse_item = Pile()
        scene.addItem(ellipse_item)

        view = QtWidgets.QGraphicsView()
        view.setScene(scene)
        view.setGeometry(QtCore.QRect(0, 0, 400, 200))
        self.setCentralWidget(view)


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainForm()
    form.show()
    exit(app.exec_())


if __name__ == '__main__':
    main()
