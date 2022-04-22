import input_data


def counting_sort(data_list):
    histogram_base = list(range(min(data_list), max(data_list)))
    len_histogram = len(histogram_base)
    histogram = [0] * len_histogram
    index = 0
    for base_num in histogram_base:
        for el in data_list:
            if base_num == el:
                histogram[index] += 1
        index += 1
    data_sorted = []
    for x in range(0, len_histogram):
        if histogram[len_histogram - x-1] > 0:
            data_sorted.append(histogram_base[len_histogram - x-1])
    return data_sorted


def main():
    print(counting_sort(input_data.auto_random()))


if __name__ == '__main__':
    main()