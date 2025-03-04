import logging

import stenogotchi.ui.fonts as fonts
from stenogotchi.ui.hw.base import DisplayImpl


class WaveshareV4(DisplayImpl):
    def __init__(self, config):
        super(WaveshareV4, self).__init__(config, 'waveshare_4')
        self._display = None

    def layout(self):
        fonts.setup(10, 8, 10, 35, 25, 9)
        self._layout['width'] = 250
        self._layout['height'] = 122
        self._layout['face'] = (0, 40)
        self._layout['name'] = (5, 20)
        self._layout['ups'] = (0, 0)
        self._layout['wpm'] = {
            'pos': (50, 0),
            'max': 9
        }
        self._layout['strokes'] = {
            'pos': (128, 0),
            'max': 5
        }
        self._layout['uptime'] = (185, 0)
        self._layout['line1'] = [0, 14, 250, 14]
        self._layout['line2'] = [0, 108, 250, 108]
        self._layout['friend_face'] = (0, 92)
        self._layout['friend_name'] = (40, 94)
        self._layout['bthost'] = {
            'pos': (0, 109),
            'max': 15
        }
        self._layout['wifi'] = {
            'pos': (113, 109),
            'max': 12
        }
        self._layout['mode'] = (210, 109)
        self._layout['status'] = {
            'pos': (125, 20),
            'font': fonts.status_font(fonts.Medium),
            'max': 20
        }

        return self._layout
    
    def initialize(self):
        logging.info("initializing waveshare v4 display")
        from stenogotchi.ui.hw.libs.waveshare.v4.epd2in13_V4 import EPD
        self._display = EPD()
        self._display.init()
        self._display.Clear(0xFF)

    def render(self, canvas):
        buf = self._display.getbuffer(canvas)
        self._display.displayPartial(buf)

    def clear(self):
        #pass
        self._display.Clear(0xFF)
