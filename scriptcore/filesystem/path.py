
import os
from math import log10


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
            return '0'

        magnitude = int(log10(abs(size)))
        if magnitude > 13:
            format_str = '%i T'
            denominator_mag = 12
        else:
            float_fmt = '%2.1f ' if magnitude % 3 == 1 else '%1.2f '
            illion = (magnitude + 1) // 3
            format_str = float_fmt + ['B', 'K', 'M', 'G', 'T'][illion]
            denominator_mag = illion * 3

        return (format_str % (size * 1.0 / (10 ** denominator_mag))).lstrip('0')
