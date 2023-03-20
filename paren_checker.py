from stack import Stack

open_chars = ['(', '{', '[']
close_chars = [')', '}', ']']

def is_open(char):
	return char in open_chars

def is_close(char):
	return char in close_chars

def match(open_char, close_char):
	if open_char == '(' and close_char == ')':
		return True
	if open_char == '{' and close_char == '}':
		return True
	if open_char == '[' and close_char == ']':
		return True
	return False

def check(paren_string):
	parens = Stack(10)

	for close_char in paren_string:	
		if is_open(close_char):
			parens.push(close_char)
		elif is_close(close_char):
			if parens.size() == 0:
				return False
			open_char = parens.pop()
			# print(f'popped char: {open_char}')
			if not match(open_char, close_char):
				return False			
		# print('current stack:')
		# parens.debug()
		# print(f'close_char: {close_char}')
		# print()

	
	# print('finished!')
	# parens.debug()
	if parens.size() > 0:
		return False
	return True



# paren_string = '(()())'
# result = check(paren_string)
# print(result, paren_string)
