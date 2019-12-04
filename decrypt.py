import pyperclip
import sys

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
reversed_alphabet = list(reversed(alphabet))

def clipboard(text):
	pyperclip.copy(text)
	pyperclip.paste()

def get_proper_index(amount):
	index = 0

	while amount > 0:
		index += 1
		amount -= 1

		if index >= len(alphabet):
			index = 0

	return index

def decrypt(phrase, number, lr):
	decrypted = ""

	for letter in phrase:
		if letter.lower() in alphabet:
			if lr == "left":
				if letter.isupper():
					decrypted = decrypted + reversed_alphabet[get_proper_index(reversed_alphabet.index(letter.lower()) + number)].upper()
				else:
					decrypted = decrypted + reversed_alphabet[get_proper_index(reversed_alphabet.index(letter.lower()) + number)]
			elif lr == "right":
				if letter.isupper():
					decrypted = decrypted + alphabet[get_proper_index(alphabet.index(letter.lower()) + number)].upper()
				else:
					decrypted = decrypted + alphabet[get_proper_index(alphabet.index(letter.lower()) + number)]
		else:
			decrypted = decrypted + letter

	return decrypted

def bruteforce(cipher):
	print("\n")
	print("-"*30 + "BRUTEFORCE" + "-"*30)
	print("\nLeft Direction:\n")
	for amount in range(1, 27):
		print("{}) {}".format(amount, decrypt(cipher, amount, "left")))

	print("\n")
	print("-"*70)

	print("\nRight Direction:\n")
	for amount in range(1, 27):
		print("{}) {}".format(amount, decrypt(cipher, amount, "right")))

	sys.exit()

while True:
	if len(sys.argv) > 1:
		phrase = str(sys.argv[1])
		number = int(sys.argv[2])
		direction = str(sys.argv[3]).lower()

		if direction.lower() != "left" and direction.lower() != "right" and direction.lower() != "bruteforce":
			direction = "left"

		if direction.lower() == "bruteforce":
			bruteforce(phrase)

		decryption = decrypt(phrase, number, direction.lower())

		print("\nDecrypted Caesar Cipher: " + decryption)

		clipboard_choice = input("\nCopy to clipboard?:\n(y/n): ")

		if clipboard_choice.lower() == "y" or clipboard_choice.lower() == "yes":
			clipboard(decryption)

		break

	print("Caesar Cipher Encrypter\n\nUse \"bruteforce\" in \"(Left/Right)\" to bruteforce.\n")

	phrase = input("Enter Caesar Cipher Text: ")
	number = int(input("Enter the number: "))
	direction = input("(Left/Right): ")

	if direction.lower() != "left" and direction.lower() != "right" and direction.lower() != "bruteforce":
		direction = "left"

	if direction.lower() == "bruteforce":
		bruteforce(phrase)

	decryption = decrypt(phrase, number, direction.lower())

	print("\nDecrypted Caesar Cipher: " + decryption)

	clipboard_choice = input("\nCopy to clipboard?:\n(y/n): ")

	if clipboard_choice.lower() == "y" or clipboard_choice.lower() == "yes":
		clipboard(decryption)

	break

"""
The funny thing is. That this script is actually the encrypt script. Because Caesar Cipher just
moves letter around the alphabet for all I know. So yeah whatever both scripts are the same XD.
"""
