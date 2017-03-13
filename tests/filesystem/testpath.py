
from scriptcore.testing.testcase import TestCase
from scriptcore.filesystem.path import Path
import os.path


class TestPath(TestCase):

    def test_dir_size(self):
        """
        Test the dir size
        :return:    void
        """

        directory = self.directory()

        exp_size = 0
        for dirpath, direnames, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                exp_size += os.path.getsize(file_path)

        self.assert_equal(exp_size, Path.get_dir_size(directory))

    def test_readable_size(self):
        """
        Test readable size
        :return:    void
        """

        sizes = {
            0:          '0 B',
            1024**1:    '1.0 KB',
            1024**2:    '1.0 MB',
            1024**3:    '1.0 GB',
            1024**4:    '1.0 TB',
            1024**5:    '1.0 PB',
            1024**6:    '1.0 EB',
            1024**7:    '1.0 ZB',
            1024**8:    '1.0 YB',

            9:          '9.0 B',
            324:        '324.0 B',
            1983:       '1.94 KB',
            1239471:    '1.18 MB',
            848020462:  '808.74 MB',
            2089334920: '1.95 GB',
        }

        for size in sizes:
            self.assert_equal(sizes[size], Path.readable_size(size))
