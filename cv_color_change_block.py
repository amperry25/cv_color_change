import numpy
import cv2

from nio import Block
from nio.properties import Property, VersionProperty


class CvColorChange(Block):

    version = VersionProperty('0.1.0')
    input_array = Property(title='Array to Convert', default='{{ $image }}')

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            signal.image = cv2.cvtColor(self.input_array(signal), cv2.COLOR_BGR2RGB)
        self.notify_signals(signals)
