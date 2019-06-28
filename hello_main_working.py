import platform

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))
    print('Line 2')
    if False:
        print('Line 3')
    else:
        print('not true')

if __name__ == '__main__':
    main()
