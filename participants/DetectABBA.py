#!/usr/bin/env python
import sys, os, json, logging
sys.path.append(os.path.abspath("."))
import gevent
import msgflo

log = logging.getLogger(__name__)


class DetectABBA(msgflo.Participant):
  def __init__(self, role):
    d = {
      'component': 'c-flo/DetectABBA',
      'label': 'Detect if ABBA',
      'icon': 'toggle-on',
      'inports': [
        { 'id': 'current_song_in', 'type': 'object' },
      ],
      'outports': [
        { 'id': 'out', 'type': 'object' },
      ],
    }
    msgflo.Participant.__init__(self, d, role)

  def process(self, inport, msg):
    current_song = msg.data
    artist = current_song.get('artist', '')
    if artist.lower() == 'abba':
        self.send('out', True)
    else:
        self.send('out', False)
    self.ack(msg)


if __name__ == '__main__':
  msgflo.main(DetectABBA)
