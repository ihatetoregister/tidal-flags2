from tidal import *
from app import App

DISPLAY_WIDTH = 135
DISPLAY_HEIGH = 240

CROSS_WIDTH = 27

class Flags2App(App):
    currentFlag = 0

    def draw_cross(self, bgColor, crossColor):
        print("draw_cross")
        display.fill(bgColor)
        display.fill_rect(int(DISPLAY_WIDTH/2 - CROSS_WIDTH/2), 0, CROSS_WIDTH, DISPLAY_HEIGH, crossColor)
        display.fill_rect(0, int(DISPLAY_HEIGH/2 - CROSS_WIDTH/2 - CROSS_WIDTH), DISPLAY_WIDTH, CROSS_WIDTH, crossColor)

    def draw_sweden(self):
        print("draw_sweden")
        self.draw_cross(BLUE, YELLOW)

    def draw_denmark(self):
        print("draw_denmark")
        self.draw_cross(RED, WHITE)

    def draw_finland(self):
        print("draw_finland")
        self.draw_cross(WHITE, BLUE)

    def draw_rainbow(self):
        display.fill(RED)
        display.fill_rect(22, 0, 23, 240, color565(255, 153, 0))
        display.fill_rect(45, 0, 22, 240, YELLOW)
        display.fill_rect(67, 0, 23, 240, GREEN)
        display.fill_rect(90, 0, 22, 240, BLUE)
        display.fill_rect(112, 0, 23, 240, color565(204, 0, 255))

    flagFuncs = [
        draw_sweden, 
        draw_denmark, 
        draw_finland, 
        draw_rainbow
    ]

    def updateFlag(self):
        print("updateFlag")
        self.flagFuncs[self.currentFlag](self)

    def nextFlag(self):
        print("nextFlag")
        self.currentFlag = self.currentFlag + 1
        if(self.currentFlag >= len(self.flagFuncs)):
            self.currentFlag = 0
        print(f"currentflag: {self.currentFlag}")
        self.updateFlag()

    def prevFlag(self):
        print("prevFlag")
        self.currentFlag = self.currentFlag - 1
        if(self.currentFlag < 0):
            self.currentFlag = len(self.flagFuncs) - 1
        print(f"currentflag: {self.currentFlag}")
        self.updateFlag()

    def on_start(self):
        super().on_start()
        print("on_start")
        self.currentFlag = 0

    def on_activate(self):
        super().on_activate()
        print("on_activate")
        self.buttons.on_press(JOY_LEFT, self.nextFlag)
        self.buttons.on_press(JOY_RIGHT, self.prevFlag)
        self.updateFlag()


print("Flags2App")

main = Flags2App
