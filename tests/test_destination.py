import pytest

from character_copier_kata.destination import ListDestination


class TestListDestination:

    @pytest.mark.parametrize(
        "input_char, expected_char",
        [
            ("a", "a"),
            ("b", "b"),
            ("c", "c"),
        ]
    )
    def test_can_write_single_char_into_list(self, input_char, expected_char):
        destination = ListDestination()

        destination.set_char(input_char)

        assert destination._chars == [expected_char]

    @pytest.mark.parametrize(
        "input_chars, expected_chars",
        [
            (["a", "b", "c"], ["a", "b", "c"]),
            (["d", "e", "f"], ["d", "e", "f"]),
            (["g", "h", "i"], ["g", "h", "i"]),
        ]
    )
    def test_can_write_multiple_chars_into_list(self, input_chars, expected_chars):
        destination = ListDestination()

        for char in input_chars:
            destination.set_char(char)

        assert destination._chars == expected_chars
