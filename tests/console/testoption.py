
from scriptcore.testing.testcase import TestCase
from scriptcore.console.option import Option


class TestOption(TestCase):

    def test_constructor(self):
        """
        Test constructor
        :return:    void
        """

        prop_short = 's'
        prop_description = 'this is a description'
        prop_default = 'default'
        prop_long = 'long'
        prop_type = None

        option = Option(prop_short, prop_description, prop_default, prop_long, prop_type)

        self.assert_equal(prop_short, option.short)
        self.assert_equal(prop_description, option.description)
        self.assert_equal(prop_default, option.default)
        self.assert_equal(prop_long, option.long)
        self.assert_equal(prop_type, option.type)

    def test_properties(self):
        """
        Test properties
        :return:    void
        """

        prop_short = 's'
        prop_description = 'this is a description'
        prop_default = 'default'
        prop_long = 'long'
        prop_type = None
        prop_value = 'value'
        prop_given = True

        option = Option(None, None, None, None, None)
        option.short = prop_short
        option.description = prop_description
        option.default = prop_default
        option.long = prop_long
        option.type = prop_type
        option.value = prop_value
        option.given = prop_given

        self.assert_equal(prop_short, option.short)
        self.assert_equal(prop_description, option.description)
        self.assert_equal(prop_default, option.default)
        self.assert_equal(prop_long, option.long)
        self.assert_equal(prop_type, option.type)
        self.assert_equal(prop_value, option.value)
        self.assert_equal(prop_given, option.given)

    def test_reset(self):
        """
        Test properties
        :return:    void
        """

        prop_short = 's'
        prop_description = 'this is a description'
        prop_value = 'value'
        prop_given = True

        option = Option(prop_short, prop_description)
        option.value = prop_value
        option.given = prop_given

        self.assert_equal(prop_value, option.value)
        self.assert_equal(prop_given, option.given)

        option.reset()

        self.assert_equal(None, option.value)
        self.assert_equal(False, option.given)

    def test_value_given_default(self):
        """
        Test value, given and default logic
        :return:    void
        """

        prop_short = 's'
        prop_description = 'this is a description'
        prop_default = 'default'
        prop_value = 'value'

        option = Option(prop_short, prop_description)

        # Standard
        self.assert_is_none(option.value)
        self.assert_false(option.given)

        # Value given
        option.value = prop_value
        self.assert_equal(prop_value, option.value)
        self.assert_true(option.given)

        # Set given to false
        option.given = False
        self.assert_is_none(option.value)
        self.assert_false(option.given)

        # Give a default value
        option.default = prop_default
        self.assert_equal(prop_default, option.value)
        self.assert_false(option.given)

        # Value given
        option.value = prop_value
        self.assert_equal(prop_value, option.value)
        self.assert_true(option.given)

        # Set given to false
        option.given = False
        self.assert_equal(prop_default, option.value)
        self.assert_false(option.given)

    def test_add_value_and_types(self):
        """
        Test add value and types
        :return:    void
        """

        prop_short = 's'
        prop_description = 'this is a description'
        prop_value = 'value'
        prop_value2 = 'value2'

        option = Option(prop_short, prop_description)

        # Standard
        self.assert_is_none(option.value)
        self.assert_false(option.given)

        # Add value
        option.add_value(prop_value)
        self.assert_equal(prop_value, option.value)
        self.assert_true(option.given)

        # Add value2
        option.add_value(prop_value2)
        self.assert_equal(prop_value2, option.value)
        self.assert_true(option.given)

        # Make list
        option.type = Option.type_list
        option.reset()

        # Standard
        self.assert_equal_deep([], option.value)
        self.assert_false(option.given)

        # Add value
        option.add_value(prop_value)
        self.assert_equal([prop_value], option.value)
        self.assert_true(option.given)

        # Add value2
        option.add_value(prop_value2)
        self.assert_equal([prop_value, prop_value2], option.value)
        self.assert_true(option.given)
