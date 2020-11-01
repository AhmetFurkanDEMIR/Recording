<p align="center">
  <img src="https://user-images.githubusercontent.com/54184905/97798487-91cf6800-1c37-11eb-91f1-50282f23a17f.gif" />
</p>


## What is a Recording?

Recording allows you to record your desktop screen at 30 or 60 FPS. If you wish, you can open your camera and include it in the video with a single click. Currently, video recording is performed in .mp4 format only.


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

* Providing less CPU and RAM usage by distributing across different threads instead of doing all the operations on the same thread.


## Supported systems

* A linux operating system from the Debian distribution.

* Screen with a resolution of 1366 X 768 (15.6 inch).


## Technologies we use

<p align="center">
  <img src="https://user-images.githubusercontent.com/54184905/97799114-fccf6d80-1c3c-11eb-92bf-358971809f8d.png" />
</p>

This application was written in Python 3.7. In order for the application to run, you must have Python and the necessary Python modules installed on your device. 

Python downloads : [https://www.python.org/downloads/](https://www.python.org/downloads/)

In order to install the necessary Python modules, run the following code while in the same directory as the file named requirements.txt.

```linux
pip3 install -r requirements.txt
```

**Python modules and their purposes.**

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


## In app images

**Camera and video recording are turned off.**

![not_viode_not_camera](https://user-images.githubusercontent.com/54184905/97799430-520c7e80-1c3f-11eb-87c2-c0472f364ee7.png)

**Record off, camera on.**

![not_video_yes_camera](https://user-images.githubusercontent.com/54184905/97799428-5173e800-1c3f-11eb-9220-6e1a0a8b3fb0.png)

**Settings.**

![Settings](https://user-images.githubusercontent.com/54184905/97799425-5042bb00-1c3f-11eb-8e5a-ca0469caa1b1.png)

**Setting the start time of recording**

![Screenshot_2020-11-01_12-38-16](https://user-images.githubusercontent.com/54184905/97799427-50db5180-1c3f-11eb-89d3-e239e943f6ab.png)

**A frame from the test recording with the camera on.**

![untitled-f002803](https://user-images.githubusercontent.com/54184905/97799518-cc3d0300-1c3f-11eb-93ab-f2dd4fd4e833.png)


## Open source codes of the application

[GitHub Link : https://github.com/AhmetFurkanDEMIR/Recorder](https://github.com/AhmetFurkanDEMIR/Recorder)

