import pytest

from character_copier_kata.copier import Copier
from character_copier_kata.destination import IDestination, ListDestination
from character_copier_kata.source import ISource, StringReader


class TestCopier:

    def test_given_single_char_should_copy_char(self, mocker):
        source = mocker.Mock(spec=ISource)
        destination = mocker.Mock(spec=IDestination)
        source.get_char.side_effect = ["a", "\n"]
        copier = Copier(source, destination)

        copier.copy_character()

        assert source.get_char.call_count == 2
        assert destination.set_char.call_count == 1
        destination.set_char.assert_called_once_with("a")

    @pytest.mark.parametrize(
        "input_characters, expected_write_calls, expected_read_calls",
        [
            (["a", "b", "\n"], ["a", "b"], 2),  # Regular case
            (["\n", "a", "b"], [], 0),  # Newline at the start
            (["a", "b", "c", "\n", "d", "e"], ["a", "b", "c"], 3),  # Newline in middle
        ]
    )
    def test_multiple_chars_are_copied_until_new_line_is_found(self, mocker, input_characters, expected_write_calls, expected_read_calls):
        source = mocker.Mock(spec=ISource)
        destination = mocker.Mock(spec=IDestination)
        source.get_char.side_effect = input_characters
        copier = Copier(source, destination)

        copier.copy_character()

        assert source.get_char.call_count == len(expected_write_calls) + 1
        assert destination.set_char.call_count == expected_read_calls
        expected_calls = [mocker.call(char) for char in expected_write_calls]
        destination.set_char.assert_has_calls(expected_calls)

    @pytest.mark.integration
    @pytest.mark.parametrize(
        "input_string, expected_chars",
        [("abc", ["a", "b", "c"]), ("def\nghi", ["d", "e", "f"])],
    )
    def test_copies_characters_from_string_reader_and_writes_to_list(self, input_string, expected_chars):
        source = StringReader(input_string)
        destination = ListDestination()
        copier = Copier(source, destination)

        copier.copy_character()

        assert destination._chars == expected_chars
