import sys
from interface import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt6.QtGui import QPixmap
from PIL import Image, ImageFilter 
from PIL.ImageQt import ImageQt

class PhotoEditor(QMainWindow):
    def __init__(self):
        super(PhotoEditor, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.photo_choice_button.clicked.connect(self.get_image)
        self.ui.blur.clicked.connect(self.blur_image)
        self.ui.black_white.clicked.connect(self.black_white_image)

    def get_image(self):
        file_dialog = QFileDialog()
        filter = "*.png *.jpeg *.jpg *.ppm *.gif *.tiff *.bmp"
        self.image_path = QFileDialog.getOpenFileName(file_dialog, filter=filter)[0]
        self.set_image(self.image_path)

    def set_image(self, image_path):
        pix = QPixmap(image_path)
        self.ui.image_label.setPixmap(pix)

    def set_main_pixmap(self, image):
        qt_conversion = ImageQt(image).copy()
        pix = QPixmap.fromImage(qt_conversion)
        self.ui.image_label.setPixmap(pix)

    def blur_image(self):
        image = Image.open(self.image_path)
        blurred = image.filter(ImageFilter.BLUR)
        self.set_main_pixmap(blurred)

    def black_white_image(self):
        image = Image.open(self.image_path)
        black_white = image.convert('L')
        self.set_main_pixmap(black_white)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = PhotoEditor()
    ui.show()
    app.exec()