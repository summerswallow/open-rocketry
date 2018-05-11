import os

import solid

from utils import to_inch


class EnglishThread(solid.IncludedOpenSCADObject):
    """ Hacky Connector for threads.scad library.
        "use" doesn't survive imports welll"""

    """ This requires the thread library found at http://dkprojects.net/openscad-threads/ """

    def __init__(self, diameter=None, threads_per_inch=None, length=None, internal=None, n_starts=None,
                 thread_size=None, groove=None, square=None, rectangle=None, angle=None, taper=None, leadin=None,
                 **kwargs):
        super(EnglishThread, self).__init__('english_thread',
                                            {'diameter': diameter, 'threads_per_inch': threads_per_inch,
                                             'length': length, 'internal': internal, 'n_starts': n_starts,
                                             'thread_size': thread_size, 'groove': groove, 'square': square,
                                             'rectangle': rectangle, 'angle': angle, 'taper': taper,
                                             'leadin': leadin, },
                                            include_file_path=os.path.join(os.environ.get("OPENSCAD_LIBRARY", "."),
                                                                           "threads.scad"),
                                            use_not_include=True, **kwargs)


class Threaded(object):
    """ You can refactor this to use a different thread library"""

    def threaded_male_column(self, length, diameter, threads_per_inch):
        return EnglishThread(length=to_inch(length), diameter=to_inch(diameter), threads_per_inch=threads_per_inch)

    def threaded_female_column(self, length, diameter, threads_per_inch):
        return EnglishThread(length=to_inch(length), diameter=to_inch(diameter),
                             threads_per_inch=threads_per_inch, internal=True)
