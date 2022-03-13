#!/usr/bin/env python

import time
from pygame import mixer

mixer.init()
mixer.music.load("bell.mp3")
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(1)

