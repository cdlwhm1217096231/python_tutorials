import logging
import logging_lib


def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    logging_lib.do_something()
    logging.info('Finished')


if __name__ == '__main__':
    main()

