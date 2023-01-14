import sys
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication


class VideoStream(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.player = QMediaPlayer()
        self.resize(QSize(1280, 720))

        self.video_widget = QVideoWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.video_widget)
        self.setLayout(self.layout)

        self.player.setMedia(QMediaContent(QUrl("gst-pipeline: rtspsrc location={ip/location of video} ! videoconvert ! videoscale  ! autovideosink sync=false drop=true max_buffers=1")))

        self.player.setVideoOutput(self.video_widget)
        self.player.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VideoStream()
    player.raise_()
    player.show()
    app.exec_()
