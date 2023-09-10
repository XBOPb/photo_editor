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
        self.ui.undo.clicked.connect(self.undo)
        self.ui.redo.clicked.connect(self.redo)
        
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
        self.current_image = pix

    def set_main_pixmap(self, image):
        qt_conversion = ImageQt(image).copy()
        pix = QPixmap.fromImage(qt_conversion)
        self.ui.image_label.setPixmap(pix)
        self.ui.effect_slider.hide()
        self.current_image = pix

    def undo(self):
        self.next_image = Image.fromqpixmap(self.current_image)
        self.set_main_pixmap(self.previous_image)
    
    def redo(self):
        self.previous_image = Image.fromqpixmap(self.current_image)
        self.set_main_pixmap(self.next_image)

    def blur_image(self):
        self.previous_image = Image.fromqpixmap(self.current_image)
        blurred = self.previous_image.filter(ImageFilter.BLUR)
        self.set_main_pixmap(blurred)

    def black_white_image(self):
        self.previous_image = Image.fromqpixmap(self.current_image)
        black_white = self.previous_image.convert('L')
        self.set_main_pixmap(black_white)

    def enhance_image(self):
        self.previous_image = Image.fromqpixmap(self.current_image)
        enhanced = ImageEnhance.Contrast(self.previous_image).enhance(1.3)
        self.set_main_pixmap(enhanced)
        self.ui.effect_slider.show()
    
    def sharpen_image(self):
        self.previous_image = Image.fromqpixmap(self.current_image)
        sharp = self.previous_image.filter(ImageFilter.SHARPEN)
        self.set_main_pixmap(sharp)
    
    def smoothen_image(self):
        self.previous_image = Image.fromqpixmap(self.current_image)
        smooth = self.previous_image.filter(ImageFilter.SMOOTH)
        self.set_main_pixmap(smooth)

    def emboss(self):
        self.previous_image = Image.fromqpixmap(self.current_image)
        embossed = self.previous_image.filter(ImageFilter.EMBOSS)
        self.set_main_pixmap(embossed)

    def edge_enhance(self):
        self.previous_image = Image.fromqpixmap(self.current_image)
        edge_enhanced = self.previous_image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        self.set_main_pixmap(edge_enhanced)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = PhotoEditor()
    ui.show()
    app.exec()