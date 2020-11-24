input = open("input.txt").read()

passphrases = input.splitlines()

def isValid(passphrase):
	lis = passphrase.split()
	s = set(lis)

	return (len(s) == len(lis))

total = [isValid(passphrase) for passphrase in passphrases]

print(sum(total))
