
import os
import math


class Path(object):

    @staticmethod
    def get_dir_size(directory):
        """
        Get size of a directory
        :param directory:   The directory
        :return:            The size
        """

        size = 0

        for dirpath, direnames, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                size += os.path.getsize(file_path)

        return size

    @staticmethod
    def readable_size(size):
        """
        Get readable size
        :param size:    The size in bytes
        :return:        The readable size
        """

        if size == 0:
            return '0 B'

        size_name = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')

        i = int(math.floor(math.log(size, 1024)))
        p = math.pow(1024, i)
        s = round(size/p, 2)

        return '%s %s' % (s, size_name[i])

