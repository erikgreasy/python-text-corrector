from inc.Corrector import Corrector


def main():
    """Main program code"""

    o = Corrector('dictionary.txt')

    mode = 'ed'  # possible options: lcs, ed
    file = 'pirates'
    input_file = f'./inputs/{file}.txt'
    correct_file = f'./inputs/{file}_correct.txt'
    output_file = f'./outputs/{file}_{mode}.txt'

    o.load_input_file(input_file)
    o.load_correct_file(correct_file)
    o.run_correction(mode, output_file)
    # o.load_corrected_from_file(output_file)
    o.print_success_rate()


if __name__ == '__main__':
    main()
