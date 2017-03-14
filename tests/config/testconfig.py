
from scriptcore.testing.testcase import TestCase
from scriptcore.config.config import Config


class TestConfig(TestCase):

    def test_get(self):
        """
        Test get
        :return:    void
        """

        # Make ini-file
        path = self.write_temp_file("""
[section1]
string1: string1
""")
        config = Config()
        config.load_from_ini(path)

        # Test get
        self.assert_is_instance(config.get('section1'), dict)
        self.assert_is_instance(config('section1'), dict)
        self.assert_is_instance(config.get('section1.string1'), str)
        self.assert_is_instance(config('section1.string1'), str)

    def test_config_from_ini(self):
        """
        Test config from ini
        :return:    void
        """

        # Make ini-file
        path = self.write_temp_file("""
[section1]
string1: string1
int1: 1
float1: 1.1
boolean1: true

[section2]
string2: string2
int2: 2
float2: 2.2
boolean2: false
""")

        for namespace in [None, 'namespace']:
            config = Config()
            config.load_from_ini(path, namespace=namespace)

            namespace_prefix = '%s.' % namespace if namespace is not None else ''

            # Test section 1
            self.assert_is_instance(config('%ssection1' % namespace_prefix), dict)
            self.assert_equal(4, len(config('%ssection1' % namespace_prefix)))
            self.assert_is_instance(config('%ssection1.string1' % namespace_prefix), str)
            self.assert_equal('string1', config('%ssection1.string1' % namespace_prefix))
            self.assert_is_instance(config('%ssection1.int1' % namespace_prefix), int)
            self.assert_equal(1, config('%ssection1.int1' % namespace_prefix))
            self.assert_is_instance(config('%ssection1.float1' % namespace_prefix), float)
            self.assert_equal(1.1, config('%ssection1.float1' % namespace_prefix))
            self.assert_is_instance(config('%ssection1.boolean1' % namespace_prefix), bool)
            self.assert_equal(True, config('%ssection1.boolean1' % namespace_prefix))

            # Test section 2
            self.assert_is_instance(config('%ssection2' % namespace_prefix), dict)
            self.assert_equal(4, len(config('%ssection2' % namespace_prefix)))
            self.assert_is_instance(config('%ssection2.string2' % namespace_prefix), str)
            self.assert_equal('string2', config('%ssection2.string2' % namespace_prefix))
            self.assert_is_instance(config('%ssection2.int2' % namespace_prefix), int)
            self.assert_equal(2, config('%ssection2.int2' % namespace_prefix))
            self.assert_is_instance(config('%ssection2.float2' % namespace_prefix), float)
            self.assert_equal(2.2, config('%ssection2.float2' % namespace_prefix))
            self.assert_is_instance(config('%ssection2.boolean2' % namespace_prefix), bool)
            self.assert_equal(False, config('%ssection2.boolean2' % namespace_prefix))

            # Test section 3
            self.assert_equal(None, config('%ssection3' % namespace_prefix))

    def test_config_from_json(self):
        """
        Test config from json
        :return:    void
        """

        # Make json-file
        path = self.write_temp_file("""
{
    "section1": {
        "string1": "string1",
        "int1": 1,
        "float1": 1.1,
        "boolean1": true
    },
    "section2": {
        "string2": "string2",
        "int2": 2,
        "float2": 2.2,
        "boolean2": false
    }
}
""")

        for namespace in [None, 'namespace']:
            config = Config()
            config.load_from_json(path, namespace=namespace)

            namespace_prefix = '%s.' % namespace if namespace is not None else ''

            # Test section 1
            self.assert_is_instance(config('%ssection1' % namespace_prefix), dict)
            self.assert_equal(4, len(config('%ssection1' % namespace_prefix)))
            self.assert_is_instance(config('%ssection1.string1' % namespace_prefix), str)
            self.assert_equal('string1', config('%ssection1.string1' % namespace_prefix))
            self.assert_is_instance(config('%ssection1.int1' % namespace_prefix), int)
            self.assert_equal(1, config('%ssection1.int1' % namespace_prefix))
            self.assert_is_instance(config('%ssection1.float1' % namespace_prefix), float)
            self.assert_equal(1.1, config('%ssection1.float1' % namespace_prefix))
            self.assert_is_instance(config('%ssection1.boolean1' % namespace_prefix), bool)
            self.assert_equal(True, config('%ssection1.boolean1' % namespace_prefix))

            # Test section 2
            self.assert_is_instance(config('%ssection2' % namespace_prefix), dict)
            self.assert_equal(4, len(config('%ssection2' % namespace_prefix)))
            self.assert_is_instance(config('%ssection2.string2' % namespace_prefix), str)
            self.assert_equal('string2', config('%ssection2.string2' % namespace_prefix))
            self.assert_is_instance(config('%ssection2.int2' % namespace_prefix), int)
            self.assert_equal(2, config('%ssection2.int2' % namespace_prefix))
            self.assert_is_instance(config('%ssection2.float2' % namespace_prefix), float)
            self.assert_equal(2.2, config('%ssection2.float2' % namespace_prefix))
            self.assert_is_instance(config('%ssection2.boolean2' % namespace_prefix), bool)
            self.assert_equal(False, config('%ssection2.boolean2' % namespace_prefix))

            # Test section 3
            self.assert_equal(None, config('%ssection3' % namespace_prefix))

    def test_config_from_yaml(self):
        """
        Test config from yaml
        :return:    void
        """

        # Make yaml-file
        path = self.write_temp_file("""
section1:
    string1: string1
    int1: 1
    float1: 1.1
    boolean1: true
    list1:
        - list1item1
        - list1item2
section2:
    string2: string2
    int2: 2
    float2: 2.2
    boolean2: false
    list2:
        - list2item1
""")

        for namespace in [None, 'namespace']:
            config = Config()
            config.load_from_yaml(path, namespace=namespace)

            namespace_prefix = '%s.' % namespace if namespace is not None else ''

            # Test section 1
            self.assert_is_instance(config('%ssection1' % namespace_prefix), dict)
            self.assert_equal(5, len(config('%ssection1' % namespace_prefix)))
            self.assert_is_instance(config('%ssection1.string1' % namespace_prefix), str)
            self.assert_equal('string1', config('%ssection1.string1' % namespace_prefix))
            self.assert_is_instance(config('%ssection1.int1' % namespace_prefix), int)
            self.assert_equal(1, config('%ssection1.int1' % namespace_prefix))
            self.assert_is_instance(config('%ssection1.float1' % namespace_prefix), float)
            self.assert_equal(1.1, config('%ssection1.float1' % namespace_prefix))
            self.assert_is_instance(config('%ssection1.boolean1' % namespace_prefix), bool)
            self.assert_equal(True, config('%ssection1.boolean1' % namespace_prefix))
            self.assert_is_instance(config('%ssection1.list1' % namespace_prefix), list)
            self.assert_equal(2, len(config('%ssection1.list1' % namespace_prefix)))
            self.assert_equal('list1item1', config('%ssection1.list1' % namespace_prefix)[0])
            self.assert_equal('list1item2', config('%ssection1.list1' % namespace_prefix)[1])

            # Test section 2
            self.assert_is_instance(config('%ssection2' % namespace_prefix), dict)
            self.assert_equal(5, len(config('%ssection2' % namespace_prefix)))
            self.assert_is_instance(config('%ssection2.string2' % namespace_prefix), str)
            self.assert_equal('string2', config('%ssection2.string2' % namespace_prefix))
            self.assert_is_instance(config('%ssection2.int2' % namespace_prefix), int)
            self.assert_equal(2, config('%ssection2.int2' % namespace_prefix))
            self.assert_is_instance(config('%ssection2.float2' % namespace_prefix), float)
            self.assert_equal(2.2, config('%ssection2.float2' % namespace_prefix))
            self.assert_is_instance(config('%ssection2.boolean2' % namespace_prefix), bool)
            self.assert_equal(False, config('%ssection2.boolean2' % namespace_prefix))
            self.assert_is_instance(config('%ssection2.list2' % namespace_prefix), list)
            self.assert_equal(1, len(config('%ssection2.list2' % namespace_prefix)))
            self.assert_equal('list2item1', config('%ssection2.list2' % namespace_prefix)[0])

            # Test section 3
            self.assert_equal(None, config('%ssection3' % namespace_prefix))
