
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
string1:
string2: string2
int1: 0
int2: 1
float1: 0.0
float2: 1.1
boolean1: false
boolean2: true

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
            self.assert_equal_deep(8, len(config('%ssection1' % namespace_prefix)))
            self.assert_equal_deep('', config('%ssection1.string1' % namespace_prefix))
            self.assert_equal_deep('string2', config('%ssection1.string2' % namespace_prefix))
            self.assert_equal_deep(0, config('%ssection1.int1' % namespace_prefix))
            self.assert_equal_deep(1, config('%ssection1.int2' % namespace_prefix))
            self.assert_equal_deep(0.0, config('%ssection1.float1' % namespace_prefix))
            self.assert_equal_deep(1.1, config('%ssection1.float2' % namespace_prefix))
            self.assert_equal_deep(False, config('%ssection1.boolean1' % namespace_prefix))
            self.assert_equal_deep(True, config('%ssection1.boolean2' % namespace_prefix))

            # Test section 2
            self.assert_equal_deep(4, len(config('%ssection2' % namespace_prefix)))
            self.assert_equal_deep('string2', config('%ssection2.string2' % namespace_prefix))
            self.assert_equal_deep(2, config('%ssection2.int2' % namespace_prefix))
            self.assert_equal_deep(2.2, config('%ssection2.float2' % namespace_prefix))
            self.assert_equal_deep(False, config('%ssection2.boolean2' % namespace_prefix))

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
        "string1": "",
        "string2": "string2",
        "int1": 0,
        "int2": 1,
        "float1": 0.0,
        "float2": 1.1,
        "boolean1": false,
        "boolean2": true
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
            self.assert_equal_deep(8, len(config('%ssection1' % namespace_prefix)))
            self.assert_equal_deep('', config('%ssection1.string1' % namespace_prefix))
            self.assert_equal_deep('string2', config('%ssection1.string2' % namespace_prefix))
            self.assert_equal_deep(0, config('%ssection1.int1' % namespace_prefix))
            self.assert_equal_deep(1, config('%ssection1.int2' % namespace_prefix))
            self.assert_equal_deep(0.0, config('%ssection1.float1' % namespace_prefix))
            self.assert_equal_deep(1.1, config('%ssection1.float2' % namespace_prefix))
            self.assert_equal_deep(False, config('%ssection1.boolean1' % namespace_prefix))
            self.assert_equal_deep(True, config('%ssection1.boolean2' % namespace_prefix))

            # Test section 2
            self.assert_equal_deep(4, len(config('%ssection2' % namespace_prefix)))
            self.assert_equal_deep('string2', config('%ssection2.string2' % namespace_prefix))
            self.assert_equal_deep(2, config('%ssection2.int2' % namespace_prefix))
            self.assert_equal_deep(2.2, config('%ssection2.float2' % namespace_prefix))
            self.assert_equal_deep(False, config('%ssection2.boolean2' % namespace_prefix))

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
    string1:
    string2: string2
    int1: 0
    int2: 1
    float1: 0.0
    float2: 1.1
    boolean1: false
    boolean2: true
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
            self.assert_equal_deep(9, len(config('%ssection1' % namespace_prefix)))
            self.assert_equal_deep(None, config('%ssection1.string1' % namespace_prefix))
            self.assert_equal_deep('string2', config('%ssection1.string2' % namespace_prefix))
            self.assert_equal_deep(0, config('%ssection1.int1' % namespace_prefix))
            self.assert_equal_deep(1, config('%ssection1.int2' % namespace_prefix))
            self.assert_equal_deep(0.0, config('%ssection1.float1' % namespace_prefix))
            self.assert_equal_deep(1.1, config('%ssection1.float2' % namespace_prefix))
            self.assert_equal_deep(False, config('%ssection1.boolean1' % namespace_prefix))
            self.assert_equal_deep(True, config('%ssection1.boolean2' % namespace_prefix))
            self.assert_equal_deep(['list1item1', 'list1item2'], config('%ssection1.list1' % namespace_prefix))

            # Test section 2
            self.assert_equal_deep(5, len(config('%ssection2' % namespace_prefix)))
            self.assert_equal_deep('string2', config('%ssection2.string2' % namespace_prefix))
            self.assert_equal_deep(2, config('%ssection2.int2' % namespace_prefix))
            self.assert_equal_deep(2.2, config('%ssection2.float2' % namespace_prefix))
            self.assert_equal_deep(False, config('%ssection2.boolean2' % namespace_prefix))
            self.assert_equal_deep(['list2item1'], config('%ssection2.list2' % namespace_prefix))

            # Test section 3
            self.assert_equal(None, config('%ssection3' % namespace_prefix))
