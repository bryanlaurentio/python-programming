#alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u', 'v', 'w','x','y','z']

#i = 2

word = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

#word_array = list(word)


#for i in range(203):
#	if word_array[i] == ' ':
#		print(" ", end = '')
#	elif word_array[i] == '.':
#		print(".", end = " ")
#	elif word_array[i] == 'x':
#		print('z', end = '')
#	elif word_array[i] == 'y':
#		print('a', end = '')
#		print('b', end = '')
#	elif word_array[i] == '(':
#		print('(', end = '')
#	elif word_array[i] == ')':
#		print(')', end = '')
#	if word_array[i] not in alphabet:
#		print(word_array[i])
#	else:
#		for j in range(len(alphabet)-2):
#			if alphabet[j] == word_array[i]:
#				print(alphabet[j+2], end = "")
#
#	for j in range(len(alphabet)-2):
#		if alphabet[j] == new_world:
#			exact_word = alphabet[j+2]
#			print(exact_word, end = '')

#using maketrans()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

new_alphabet = 'cdefghijklmnopqrstuvwxyzab'

new_word = str.maketrans(alphabet, new_alphabet)

print(word.translate(new_word))

url = 'map'

print()
print(url.translate(new_word))

#http://www.pythonchallenge.com/pc/def/ocr.html