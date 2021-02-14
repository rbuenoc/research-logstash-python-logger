from common.tools.logs import log_info
from time import sleep


def process_data():
    i = 0
    while True:
        _process_number(i)
        i += 1
        if i == 15:
            raise Exception('Something goes wrong')


def _process_number(n):
    data = { 'number': n }
    log_info(f'{__name__}._process_number', data)
    sleep(1)
