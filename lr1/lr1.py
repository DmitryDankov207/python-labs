import random
import operator
import argparse
import sys


def get_text_from_file(file_name):
	with open(file_name, 'r') as f:
		result = f.read()
	return result


def get_words_statistics(file_name):
	text = get_text_from_file(file_name)
	words = count_words(text)

	print('count | word')
	for word, count in words.items():
		print(count, " | ", word)


def count_words(text):
	splitted_text = text.split()
	words = set({word for word in splitted_text})
	return {word:splitted_text.count(word) for word in words}


# Input: counts is dictionary like: {count mentions of the word : word}.
# Output: sentence consisting of 10 the most popular words.
def get_top_from_dict(counts):
	counter = 0
	result = ""
	keys = [k for k in counts.keys()]
	keys.reverse()

	for key in keys:
		result = result + " "+ " ".join(counts[key])
		counter += len(counts[key])
		if(counter >= 10):
			break

	return result[1:]


def print_top_words(file_name):
	text = get_text_from_file(file_name)
	words_dict = count_words(text)
	counts = {count:[] for count in set({n for n in words_dict.values()})}

	for k, v in words_dict.items():
		counts[v].append(k) 

	print(get_top_from_dict(counts))


def perform_quick_sort(nums):
	if len(nums) <= 1:
		return nums
	else:
		current = random.choice(nums)
		lower_nums = [num for num in nums if num < current]
		equal_nums = [current] * nums.count(current)
		bigger_nums = [num for num in nums if num > current]

	return perform_quick_sort(lower_nums) + \
			equal_nums + perform_quick_sort(bigger_nums)


def from_f_to_int_arr(file_name):
	text = get_text_from_file(file_name)
	return [int(num) for num in text.split()]


def quick_sort(file_name):
	numbers = from_f_to_int_arr(file_name)
	return perform_quick_sort(numbers)


def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def get_fibonacci(file_name):
	with open(file_name, 'r') as f:
		length = int(f.read())

	result = [1, 1]

	for i in range(2, length):
		result.append(result[i - 1] + result[i - 2])

	return result


def create_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('-qs', '--quicksort')
	parser.add_argument('-ms', '--mergesort')
	parser.add_argument('-ws', '--words_statistics')
	parser.add_argument('-tw', '--top_words')
	parser.add_argument('-f', '--fibonacci')
	return parser


if __name__ == '__main__':
	parser = create_parser()
	namespace = parser.parse_args(sys.argv[1:])

	if namespace.fibonacci:
		print(get_fibonacci(namespace.fibonacci))
	elif namespace.words_statistics:
		get_words_statistics(namespace.words_statistics)
	elif namespace.top_words:
		print_top_words(namespace.top_words)
	elif namespace.quicksort:
		print(quick_sort(namespace.quicksort))
	elif namespace.mergesort:
		print(merge_sort(from_f_to_int_arr(namespace.mergesort)))
	else:
		get_words_statistics(namespace.words_statistics)