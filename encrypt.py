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

def encrypt(phrase, number, lr):
	encrypted = ""

	for letter in phrase:
		if letter.lower() in alphabet:
			if lr == "left":
				if letter.isupper():
					encrypted = encrypted + reversed_alphabet[get_proper_index(reversed_alphabet.index(letter.lower()) + number)].upper()
				else:
					encrypted = encrypted + reversed_alphabet[get_proper_index(reversed_alphabet.index(letter.lower()) + number)]
			elif lr == "right":
				if letter.isupper():
					encrypted = encrypted + alphabet[get_proper_index(alphabet.index(letter.lower()) + number)].upper()
				else:
					encrypted = encrypted + alphabet[get_proper_index(alphabet.index(letter.lower()) + number)]
		else:
			encrypted = encrypted + letter

	return encrypted

if __name__ == "__main__":
	if len(sys.argv) > 1:
		phrase = str(sys.argv[1])
		number = int(sys.argv[2])
		direction = str(sys.argv[3]).lower()

		if direction.lower() != "left" and direction.lower() != "right":
			direction = "left"

		encryption = encrypt(phrase, number, direction.lower())

		print("\nEncrypted Caesar Cipher: " + encryption)

		clipboard_choice = input("\nCopy to clipboard?:\n(y/n): ")

		if clipboard_choice.lower() == "y" or clipboard_choice.lower() == "yes":
			clipboard(encryption)

		sys.exit()

	print("Caesar Cipher Encrypter\n")

	phrase = input("Enter Plaintext: ")
	number = int(input("Enter the number: "))
	direction = input("(Left/Right): ")

	if direction.lower() != "left" and direction.lower() != "right":
		direction = "left"

	encryption = encrypt(phrase, number, direction.lower())

	print("\nEncrypted Caesar Cipher: " + encryption)

	clipboard_choice = input("\nCopy to clipboard?:\n(y/n): ")

	if clipboard_choice.lower() == "y" or clipboard_choice.lower() == "yes":
		clipboard(encryption)

	sys.exit()
