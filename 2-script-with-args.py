import argparse

# ---------------------------------------------------------------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------------------------------------------------------------
def sayHello(lang):
  if lang == 'en':
    print('Hello')
  else:
    print('Bonjour')

def sayWelcome(lang):
  if lang == 'en':
    print('Welcome to our new nation')
  else:
    print('Bienvenue dans notre nouvelle nation')

# ---------------------------------------------------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
  
  # Create parser
  parser = argparse.ArgumentParser()
  parser.add_argument('--version', action='version', version='%(prog)s v1.0')
  parser.add_argument('--lang', dest='lang', help='Language: en|fr')

  # Parse arguments
  args = parser.parse_args()
  if args.lang:
    lang = args.lang
  else:
    parser.print_help()
    exit(1)

  sayHello(lang)
  sayWelcome(lang)
