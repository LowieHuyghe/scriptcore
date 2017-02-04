
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
        config = Config()
        config.load_from_ini(path)

        # Test section 1
        self.assert_is_instance(config('section1'), dict)
        self.assert_equal(4, len(config('section1')))
        self.assert_is_instance(config('section1.string1'), str)
        self.assert_equal('string1', config('section1.string1'))
        self.assert_is_instance(config('section1.int1'), int)
        self.assert_equal(1, config('section1.int1'))
        self.assert_is_instance(config('section1.float1'), float)
        self.assert_equal(1.1, config('section1.float1'))
        self.assert_is_instance(config('section1.boolean1'), bool)
        self.assert_equal(True, config('section1.boolean1'))

        # Test section 2
        self.assert_is_instance(config('section2'), dict)
        self.assert_equal(4, len(config('section2')))
        self.assert_is_instance(config('section2.string2'), str)
        self.assert_equal('string2', config('section2.string2'))
        self.assert_is_instance(config('section2.int2'), int)
        self.assert_equal(2, config('section2.int2'))
        self.assert_is_instance(config('section2.float2'), float)
        self.assert_equal(2.2, config('section2.float2'))
        self.assert_is_instance(config('section2.boolean2'), bool)
        self.assert_equal(False, config('section2.boolean2'))

        # Test section 3
        self.assert_equal(None, config('section3'))

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
        config = Config()
        config.load_from_json(path)

        # Test section 1
        self.assert_is_instance(config('section1'), dict)
        self.assert_equal(4, len(config('section1')))
        self.assert_is_instance(config('section1.string1'), str)
        self.assert_equal('string1', config('section1.string1'))
        self.assert_is_instance(config('section1.int1'), int)
        self.assert_equal(1, config('section1.int1'))
        self.assert_is_instance(config('section1.float1'), float)
        self.assert_equal(1.1, config('section1.float1'))
        self.assert_is_instance(config('section1.boolean1'), bool)
        self.assert_equal(True, config('section1.boolean1'))

        # Test section 2
        self.assert_is_instance(config('section2'), dict)
        self.assert_equal(4, len(config('section2')))
        self.assert_is_instance(config('section2.string2'), str)
        self.assert_equal('string2', config('section2.string2'))
        self.assert_is_instance(config('section2.int2'), int)
        self.assert_equal(2, config('section2.int2'))
        self.assert_is_instance(config('section2.float2'), float)
        self.assert_equal(2.2, config('section2.float2'))
        self.assert_is_instance(config('section2.boolean2'), bool)
        self.assert_equal(False, config('section2.boolean2'))

        # Test section 3
        self.assert_equal(None, config('section3'))
