import argparse

# ---------------------------------------------------------------------------------------------------------------------
# CONSTANTS
# ---------------------------------------------------------------------------------------------------------------------
SCRIPT_VERSION = '1.0'

# ---------------------------------------------------------------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------------------------------------------------------------
lang = None

# ---------------------------------------------------------------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------------------------------------------------------------
def parseArgs():
  global lang
  parser = argparse.ArgumentParser()
  parser.add_argument('--version', action='version', version='%(prog)s v1.0')
  parser.add_argument('--lang', dest='lang', help='Language: en|fr')

  args = parser.parse_args()
  if args.lang:
    lang = args.lang
  else:
    parser.print_help()
    exit(1)

def validateLang():
  if lang != 'en' and lang != 'fr':
    print(lang + ' n\'est pas une langue supportee')
    exit(2)

def sayHello():
  if lang == 'en':
    print('Hello')
  else:
    print('Bonjour')

def sayWelcome():
  if lang == 'en':
    print('Welcome to our new nation')
  else:
    print('Bienvenue dans notre nouvelle nation')

# ---------------------------------------------------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
  
  parseArgs()
  validateLang()
  sayHello()
  sayWelcome()
