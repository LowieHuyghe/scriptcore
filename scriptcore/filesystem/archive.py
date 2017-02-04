
from scriptcore.process.execute import Execute
import os.path


class Archive(object):

    @staticmethod
    def zip(directory, target):
        """
        Zip a directory
        :param directory:   The directory
        :param target:      The target
        :return:            The archive
        """

        execute = Execute()

        directory = os.path.abspath(directory)
        parent_directory = os.path.abspath(os.path.join(directory, '..'))
        directory_name = os.path.relpath(directory, parent_directory)

        out, err, exitcode = execute('cd "%s" && zip -FSr "%s" "./%s"' % (parent_directory, target, directory_name))

        return exitcode == 0

    @staticmethod
    def unzip(archive, directory):
        """
        Unzip a file
        :param archive:     The zip file
        :param directory:   The directory to unzip in
        :return:            Success
        """

        execute = Execute()

        out, err, exitcode = execute('unzip "%s" -d "%s"' % (archive, directory))

        return exitcode == 0
