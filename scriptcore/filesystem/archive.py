
from scriptcore.process.execute import Execute


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

        execute('zip -FSr "%s" "%s"' % (target, directory))

        return target
