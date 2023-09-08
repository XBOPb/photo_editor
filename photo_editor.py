import sys
from interface import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt6.QtGui import QPixmap
from PIL import Image, ImageFilter 
from PIL.ImageQt import ImageQt
from PIL import ImageEnhance

class PhotoEditor(QMainWindow):
    def __init__(self):
        super(PhotoEditor, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.effect_slider.hide()
        self.ui.photo_choice_button.clicked.connect(self.get_image)
        self.ui.blur.clicked.connect(self.blur_image)
        self.ui.black_white.clicked.connect(self.black_white_image)
        self.ui.enhance.clicked.connect(self.enhance_image)
        self.ui.sharpen.clicked.connect(self.sharpen_image)
        self.ui.smooth.clicked.connect(self.smoothen_image)
        self.ui.emboss.clicked.connect(self.emboss)
        self.ui.edge_enhance.clicked.connect(self.edge_enhance)
        
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
        self.ui.effect_slider.hide()

    def blur_image(self):
        image = Image.open(self.image_path)
        blurred = image.filter(ImageFilter.BLUR)
        self.set_main_pixmap(blurred)

    def black_white_image(self):
        image = Image.open(self.image_path)
        black_white = image.convert('L')
        self.set_main_pixmap(black_white)

    def enhance_image(self):
        image = Image.open(self.image_path)
        enhanced = ImageEnhance.Contrast(image).enhance(1.3)
        self.set_main_pixmap(enhanced)
        self.ui.effect_slider.show()
    
    def sharpen_image(self):
        image = Image.open(self.image_path)
        sharp = image.filter(ImageFilter.SHARPEN)
        self.set_main_pixmap(sharp)
    
    def smoothen_image(self):
        image = Image.open(self.image_path)
        smooth = image.filter(ImageFilter.SMOOTH)
        self.set_main_pixmap(smooth)

    def emboss(self):
        image = Image.open(self.image_path)
        embossed = image.filter(ImageFilter.EMBOSS)
        self.set_main_pixmap(embossed)

    def edge_enhance(self):
        image = Image.open(self.image_path)
        edge_enhanced = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        self.set_main_pixmap(edge_enhanced)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = PhotoEditor()
    ui.show()
    app.exec()