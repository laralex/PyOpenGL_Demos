from ..all_demos import Demo
from OpenGL.GL import *
import math

class Lecture01_ColorDemo(Demo):
    def __init__(self):
        super().__init__(ui_defaults=None)

    def load(self, window):
        self.is_loaded = True

    def render_frame(self, width, height, global_time_sec, delta_time_sec):
        red   = 0.5*math.sin(global_time_sec) + 0.5
        green = 0.5*math.cos(global_time_sec*1.3) + 0.5
        blue  = 0.5
        glClearColor(red,green,blue,1)
        glClear(GL_COLOR_BUFFER_BIT)

