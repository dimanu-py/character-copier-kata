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

    @pytest.mark.parametrize(
        ["input_string", "expected_chars"],
        [("abc", ["a", "b", "c", "\n"]), ("defghi", ["d", "e", "f", "g", "h", "i", "\n"])]
    )
    def test_given_a_word_should_return_separated_chars(self, input_string, expected_chars):
        reader = StringReader(string_to_read=input_string)
        iterations = len(input_string) + 1

        read_chars = [reader.get_char() for _ in range(iterations)]

        assert read_chars == expected_chars
