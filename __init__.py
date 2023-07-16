from tidal import *
from app import App

DISPLAY_WIDTH = 135
DISPLAY_HEIGHT = 240

CROSS_WIDTH = 27

HORIZONTAL = 1
VERTICAL = 2

DARKGREEN = color565(0, 122, 51)

class Flags2App(App):
    currentFlag = 0

    def draw_cross(self, bgColor, crossColor):
        print("draw_cross")
        display.fill(bgColor)
        display.fill_rect(int(DISPLAY_WIDTH/2 - CROSS_WIDTH/2), 0, CROSS_WIDTH, DISPLAY_HEIGHT, crossColor)
        display.fill_rect(0, int(DISPLAY_HEIGHT/2 - CROSS_WIDTH/2 + CROSS_WIDTH), DISPLAY_WIDTH, CROSS_WIDTH, crossColor)
    
    def draw_double_cross(self, bgColor, outerCrossColor, innerCrossColor):
        print("draw_double_cross")
        display.fill(bgColor)

        # Outer cross
        outerCrossWidth = int(CROSS_WIDTH + CROSS_WIDTH * 0.75)
        display.fill_rect(int(DISPLAY_WIDTH/2 - outerCrossWidth/2), 0, outerCrossWidth, DISPLAY_HEIGHT, outerCrossColor)
        display.fill_rect(0, int(DISPLAY_HEIGHT/2 - outerCrossWidth/2 + CROSS_WIDTH), DISPLAY_WIDTH, outerCrossWidth, outerCrossColor)

        # Inner cross
        innerCrossWidth = int(CROSS_WIDTH - CROSS_WIDTH * 0.25)
        display.fill_rect(int(DISPLAY_WIDTH/2 - innerCrossWidth/2), 0, innerCrossWidth, DISPLAY_HEIGHT, innerCrossColor)
        display.fill_rect(0, int(DISPLAY_HEIGHT/2 - innerCrossWidth/2 + CROSS_WIDTH), DISPLAY_WIDTH, innerCrossWidth, innerCrossColor)

    # Draw a striped flag with <n> fields, with horizontal or vertical orientation
    def draw_striped_generic(self, orientation, listOfColors):
        print("draw_striped_generic")

        count = len(listOfColors)
        stripeWidth = DISPLAY_WIDTH // count
        stripeHeight = DISPLAY_HEIGHT // count
        wpos = 0
        hpos = 0
        endh = 0
        endw = 0

        if orientation == VERTICAL:
            endw = DISPLAY_WIDTH
            endh = stripeHeight
        elif orientation == HORIZONTAL:
            endw = stripeWidth
            endh = DISPLAY_HEIGHT

        for color in listOfColors:
            #print(f"wpos: {wpos}, hpos: {hpos}, endw: {endw}, endh: {endh}, color: {color}")
            display.fill_rect(wpos, hpos, endw, endh, color)
            if orientation == VERTICAL:
                hpos += stripeHeight
            elif orientation == HORIZONTAL:
                wpos += stripeWidth


    def draw_sweden(self):
        print("draw_sweden")
        self.draw_cross(BLUE, YELLOW)

    def draw_denmark(self):
        print("draw_denmark")
        self.draw_cross(RED, WHITE)

    def draw_finland(self):
        print("draw_finland")
        self.draw_cross(WHITE, BLUE)

    def draw_norway(self):
        print("draw_norway")
        self.draw_double_cross(RED, WHITE, BLUE)

    def draw_iceland(self):
        print("draw_iceland")
        self.draw_double_cross(BLUE, WHITE, RED)

    def draw_japan(self):
        print("draw_japan")
        display.fill(WHITE)
        display.fill_circle(int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2), int(DISPLAY_WIDTH/3), RED)

    def draw_france(self):
        print("draw_france")
        self.draw_striped_generic(VERTICAL, [BLUE, WHITE, RED])

    def draw_italy(self):
        print("draw_italy")
        self.draw_striped_generic(VERTICAL, [DARKGREEN, WHITE, RED])

    def draw_ukraine(self):
        print("draw_ukraine")
        self.draw_striped_generic(HORIZONTAL, [BLUE, YELLOW])

    def draw_hungary(self):
        print("draw_hungary")
        colors = [RED, WHITE, DARKGREEN]
        self.draw_striped_generic(HORIZONTAL, colors)

    def draw_rainbow(self):
        colors = [color565(255, 153, 0), YELLOW, GREEN, BLUE, color565(204, 0, 255)]
        self.draw_striped_generic(HORIZONTAL, colors)

    flagFuncs = [
        draw_sweden,
        draw_denmark,
        draw_finland,
        draw_norway, 
        draw_iceland,
        draw_rainbow,
        draw_japan,
        draw_france,
        draw_italy,
        draw_ukraine,
        draw_hungary
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
