import argparse

# ---------------------------------------------------------------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------------------------------------------------------------
def sayHello(lang,genre):
  if lang == 'en':
    if genre == 'Homme':
      print('Hello Mister')
    else:
      print('Hello Miss')
  elif lang == 'es':
    if genre == 'Homme':
      print('Hola senor')
    else: 
      print('Hola Senorita')
  elif lang == 'fr':
    if genre == 'Homme':
      print('Bonjour Monsieur')
    else: 
      print('Bonjour Madame')


def sayWelcome(lang,genre):
  if lang == 'en':
    print('Welcome to our new nation')
  elif lang == 'es':
    print('espanol')
  else:
    print('Bienvenue dans notre nouvelle nation')


# ---------------------------------------------------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
  
  # Create parser
  parser = argparse.ArgumentParser()
  parser.add_argument('--version', action='version', version='%(prog)s v12.0')
  parser.add_argument('--lang', dest='lang', help='Language: en |fr | es')
  parser.add_argument('--genre', dest='genre', help='Genre : Homme | Femme')

  # Parse arguments
  args = parser.parse_args()
  if args.lang:
    lang = args.lang
    if args.genre:
      genre = args.genre
  else:
    parser.print_help()
    exit(1)


  sayHello(lang,genre)
  sayWelcome('en','Homme')
 
