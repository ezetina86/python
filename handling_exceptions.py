import sys


def main():
    try:
        x =  5/0
    except ValueError:
        print('I caugth a ValueError!')
    except ZeroDivisionError:
        print('Don\'t divide by zero')
    except:
        print('Unknown Error: {sys.exc_info()[1]}')
    else:
        print('Good job')
        print(x)

if __name__ == '__main__':
    main()
