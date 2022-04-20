from inc.optimize_text import optimize_text_editing_distance, optimize_text_lcs
from inc.success_counter import success_counter


class Corrector:
    """Class storing corrupted and correct contents, alongside
    with dictionary, and running correcting functions."""

    def __init__(self, dict_file_name):
        with open(dict_file_name) as file:
            self.dict_string = file.read()

    def load_input_file(self, file_name, encoding=None):
        """Read corrupted file content"""

        with open(file_name, "r", encoding=encoding) as file:
            self.input_string = file.read()

    def load_correct_file(self, file_name, encoding=None):
        """Read correct file that we compare our
        repaired corrupted file against"""

        with open(file_name, "r", encoding=encoding) as file:
            self.correct_string = file.read()

    def run_correction(self, mode, output_file_name):
        """Run correction on loaded files with
        mode passed as string. Fixed content is written
        to file into output folder.

        Possible modes: lcs, ed
        """

        if mode == 'lcs':
            self.corrected_output = optimize_text_lcs(
                self.input_string, self.dict_string, output_file_name)
        elif mode == 'ed':
            self.corrected_output = optimize_text_editing_distance(
                self.input_string, self.dict_string, output_file_name)
        else:
            print('Unsupported correction mode')

    def print_success_rate(self):
        """Prints out success rate of repaired file
        against the correct file"""

        success_counter(self.corrected_output, self.correct_string)

    def load_corrected_from_file(self, file_name):
        """Load repaired content from file. Use this if you
        dont want to run correction again. Useful when content
        is too long and we want to calculate success rate from
        already repaired file"""

        with open(file_name) as file:
            self.corrected_output = file.read().split()
