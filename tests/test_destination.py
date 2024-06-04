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
