from parser import Parser

def main():
    print('Calculator v0.0.1\nWelcome! Type any expression below then press ENTER to evaluate.\n'
        'Press ENTER on empty input to exit.')
    _input = '';
    while True:
        _input = input('>> ')
        if _input == '':
            break
        parser = Parser(_input)
        print(parser.parse())

if __name__ == '__main__':
    main()
