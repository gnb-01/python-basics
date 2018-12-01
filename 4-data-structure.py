import argparse

# ---------------------------------------------------------------------------------------------------------------------
# CONSTANTS
# ---------------------------------------------------------------------------------------------------------------------
SCRIPT_VERSION = '1.0'

# ---------------------------------------------------------------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------------------------------------------------------------
lang = None
supportedLanguageList = ['en', 'fr']
messageDictionary = {
  'en': '--- Messages will be displayed in English ---',
  'fr': '--- Les messages seront affiches en francais ---'
}

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
  if lang not in supportedLanguageList:
    print(lang + ' n\'est pas une langue supportee')

    # Print possible options by direct access to element
    print('[direct access] - Les options permises sont:')
    print('1: ' + supportedLanguageList[0])
    print('2: ' + supportedLanguageList[1])
    
    # Print possible options by iterating through the list
    print('[list iteration] - Les options permises sont:')
    for langague in supportedLanguageList:
      print('-' + langague)

    exit(2)

def printSelectedLanguage():
  print(messageDictionary[lang])

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
  printSelectedLanguage()
  sayHello()
  sayWelcome()
