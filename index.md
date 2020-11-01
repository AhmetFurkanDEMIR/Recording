<p align="center">
  <img src="https://user-images.githubusercontent.com/54184905/97798487-91cf6800-1c37-11eb-91f1-50282f23a17f.gif" />
</p>


## What is a Recorder?

Recorder allows you to record your desktop screen at 30 or 60 FPS. If you wish, you can open your camera and include it in the video with a single click. Currently, video recording is performed in .mp4 format only.


## Recorder's features

* Screen recording at 30 or 60 FPS (.mp4).

* Combining Screen and Camera recording.

* Possibility to delay the start of recording up to 180 seconds.

* Instantly save the recording wherever you want.


## Shortcomings, Features planned to be added later

* Adding the sound of the computer and microphone to the screen recording.

* Display of the mouse cursor in the video.

* Adding other video codecs.

* Ability to record screens in different formats (.avi3, .mpeg, etc.).


## Technologies we use

This application was written in Python 3.7.

```python
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from time import sleep as sl
import numpy as np
import threading
import skvideo.io
import datetime
import mss
import sys
import cv2
```

| Python module |    Purpose of usage                              |
|---------------|--------------------------------------------------|
| PyQt5         | GUI programming                                  |
| time          | Time operations                                  |
| numpy         | Tensors, combining images                        |
| threading     | To be able to do all operations at the same time |
| skvideo       | Saving the created video                         |
| datetime      | Date transactions                                |
| mss           | Desktop screen recording                         |
| sys           | System arguments                                 |
| cv2           | Camera record                                    |
