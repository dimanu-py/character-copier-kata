import pytest

from character_copier_kata.source import StringReader


class TestStringReader:

    @pytest.mark.parametrize(
        ["input_string", "expected_char"],
        [("a", "a"), ("b", "b"), ("c", "c")],
    )
    def test_given_single_char_should_return_char(self, input_string, expected_char):
        reader = StringReader(string_to_read=input_string)

        read_char = reader.get_char()

        assert read_char == expected_char
