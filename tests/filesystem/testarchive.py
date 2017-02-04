
from scriptcore.testing.testcase import TestCase
from scriptcore.filesystem.archive import Archive
from scriptcore.filesystem.path import Path
import os.path


class TestArchive(TestCase):

    def test_zipping(self):
        """
        Test the zipping
        :return:    void
        """

        directory = self.tests_dir()
        archive = self.temp_file(only_path=True, suffix='.zip')
        target_directory = self.temp_dir(only_path=True)

        # Zip
        self.assert_false(os.path.isfile(archive))
        self.assert_true(Archive.zip(directory, archive))
        self.assert_true(os.path.isfile(archive))
        self.assert_greater_equal(Path.get_dir_size(directory), os.path.getsize(archive))

        # Unzip
        self.assert_false(os.path.isdir(target_directory))
        self.assert_true(Archive.unzip(archive, target_directory))
        self.assert_true(os.path.isdir(target_directory))
        self.assert_equal(Path.get_dir_size(directory), Path.get_dir_size(target_directory))
        self.assert_equal_deep(['tests'], os.listdir(target_directory))
        self.assert_equal_deep(os.listdir(directory), os.listdir(os.path.join(target_directory, 'tests')))
