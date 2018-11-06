import sys
from query import process
from prodigy import train

def main(argv):
	string = argv[1]
	# process.init()
	process.get_ents(string)


if __name__ == "__main__":
	main(sys.argv)
