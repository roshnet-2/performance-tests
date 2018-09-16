# code to compare time differences in simultaneous function calls
# and inline-code.

from time import time

N = 1000000  ## larger N, more visible difference

def func():
	x = 5

def main():

	mark = time()
	for _ in range(N):
		x = 5
	mark = time() - mark
	print('Inline code took {} ms'.format(mark * 1000))

	mark = time()
	for _ in range(N):
		func()
	mark = time() - mark
	print('Function call took {} ms '.format(mark * 1000))


if __name__ == '__main__':
	main()




