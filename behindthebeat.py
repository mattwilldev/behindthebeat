"""behindthebeat

Usage:
    behindthebeat.py <artist>
    behindthebeat.py <artist> (--track=<track> | --album=<album>)
    behindthebeat.py (-h | --help)
    behindthebeat.py (-v | --version)

Options:
    -h --help               Show this screen.
    -v --version            Show version.
    -t --track=<track>      The song title (for use with --artist)
    -b --album=<album>      The album title (for use with --artist)
"""

from docopt import docopt
from apirequests.SearchRequest import SearchRequest
from apirequests.SongRequest import SongRequest
import os

def main():
    access_token = '65OqpfrfCyG6-X29enouHpqJbnf8lir_fyjxpyhH5i96VMbUVigq4Nf822dlevLm'
    arguments = docopt(__doc__, version="behindthebeat 1.0")

    if (arguments['<artist>'] and arguments['--track']):
        query = arguments['<artist>'] + " " + arguments['--track']

        search_request = SearchRequest(query, access_token)
        song_id = search_request.execute()

        song_request = SongRequest(song_id, access_token)
        track = song_request.execute()

        print ""
        print track
        print ""

    elif (arguments['<artist>'] and arguments['--album']):
        query = arguments['<artist>'] + " " + arguments['--album']
        print query

if __name__ == '__main__':
    main()
