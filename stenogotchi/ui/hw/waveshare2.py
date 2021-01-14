import logging

import stenogotchi.ui.fonts as fonts
from stenogotchi.ui.hw.base import DisplayImpl


class WaveshareV2(DisplayImpl):
    def __init__(self, config):
        super(WaveshareV2, self).__init__(config, 'waveshare_2')
        self._display = None

    def layout(self):
        if self.config['color'] == 'black':
            fonts.setup(10, 9, 10, 35, 25, 9)
            self._layout['width'] = 250
            self._layout['height'] = 122
            self._layout['face'] = (0, 40)
            self._layout['name'] = (5, 20)
            self._layout['ups'] = (0, 0)
            self._layout['aps'] = (46, 0)
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
        else:    # these are not correctly configured based on different width and height of color display
            fonts.setup(10, 8, 10, 25, 25, 9)
            self._layout['width'] = 212
            self._layout['height'] = 104
            self._layout['face'] = (0, 26)
            self._layout['name'] = (5, 15)
            self._layout['ups'] = (0, 0)
            self._layout['aps'] = (46, 0)
            self._layout['status'] = (91, 15)
            self._layout['uptime'] = (147, 0)
            self._layout['line1'] = [0, 12, 212, 12]
            self._layout['line2'] = [0, 92, 212, 92]
            self._layout['friend_face'] = (0, 76)
            self._layout['friend_name'] = (40, 78)
            self._layout['bthost'] = {
                'pos': (0, 93),
                'max': 15
            }
            self._layout['wifi'] = {
                'pos': (113, 109),
                'max': 12
            }
            self._layout['mode'] = (187, 93)
            self._layout['status'] = {
                'pos': (125, 20),
                'font': fonts.status_font(fonts.Medium),
                'max': 14
            }
        return self._layout

    def initialize(self):
        logging.info("initializing waveshare v2 display")
        from stenogotchi.ui.hw.libs.waveshare.v2.epd2in13_V2 import EPD
        self._display = EPD()
        self._display.init(self._display.FULL_UPDATE)
        self._display.Clear(0xff)
        self._display.init(self._display.PART_UPDATE)

    def render(self, canvas):
        buf = self._display.getbuffer(canvas)
        self._display.displayPartial(buf)

    def clear(self):
        self._display.Clear(0xff)

    def shutdown(self):
        self._display.Dev_exit()
