import time
import bubble_sort
import counting_sort
import input_data
import statistics


def timepassed(func):
    def inside_f(len_list):
        start = time.perf_counter()
        func(len_list)
        stop = time.perf_counter()
        print(f"Time needed: {stop - start} seconds")
        return stop - start
    return inside_f


@timepassed
def speed_test_bubble(len_list):
    print(f'bubble_sort 5 lists with {len_list} elements ')
    for x in range(5):
        bubble_sort.bubble_sort(input_data.auto_random(len_list))


@timepassed
def speed_test_counting(len_list):
    print(f'counting sort 5 lists with {len_list} elements ')
    for x in range(5):
        counting_sort.counting_sort(input_data.auto_random(len_list))


def main():
    lists_tests_len = [10, 20, 50]
    results_bubble = []
    results_counting = []

    for tests_len in lists_tests_len:
        results_bubble.append(speed_test_bubble(tests_len))
        results_counting.append(speed_test_counting(tests_len))

    print("\nComparison")
    print(f'Average bubble {statistics.mean(results_bubble)}')
    print(f'Average counting {statistics.mean(results_counting)}')


if __name__ == '__main__':
    main()
