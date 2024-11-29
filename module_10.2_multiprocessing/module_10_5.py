from time import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for n, line in enumerate(file, 1):
            line = line.rstrip('\n')
            all_data.append(line)

if __name__ == '__main__':
    files = [f'file {number}.txt' for number in range(1,5)]

    start_at = time()

    for i in files:
        read_info(i)

    end_at = time()
    print(f'Время выполнения линейно - {round((end_at - start_at), 4)} сек.')

    start_at = time()

    with multiprocessing.Pool() as pool:
        pool.map(read_info, files)

    end_at = time()
    print(f'Время выполнения многопроцессно - {round((end_at - start_at), 4)} сек.')