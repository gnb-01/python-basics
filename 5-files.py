import os
import argparse

# ---------------------------------------------------------------------------------------------------------------------
# TO KNOW
# ---------------------------------------------------------------------------------------------------------------------
# A file can be opened in four different modes:
# 'r' - Read - Default value. Opens a file for reading, error if the file does not exist
# 'w' - Write - Opens a file for writing, creates the file if it does not exist
# 'a' - Append - Opens a file for appending, creates the file if it does not exist
# 'x' - Create - Creates the specified file, returns an error if the file exists

# ---------------------------------------------------------------------------------------------------------------------
# GLOBALS
# ---------------------------------------------------------------------------------------------------------------------
inputFile = None
copyFile = None

# ---------------------------------------------------------------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------------------------------------------------------------
def parseArgs():
  global inputFile
  global copyFile
  parser = argparse.ArgumentParser()
  parser.add_argument('--version', action='version', version='%(prog)s v1.0')
  parser.add_argument('--input', dest='input', help='Config file')

  args = parser.parse_args()
  if args.input:
    inputFile = args.input
    copyFile = inputFile + '.copy'
  else:
    parser.print_help()
    exit(1)

def readFile():
  with open(inputFile) as fd:  # Opens the file in read mode: open(inputFile) >> open(inputFile, 'r')
    for line in fd.readlines():
      print(line)

def writeFile():
  with open(copyFile, 'w') as copy:
    with open(inputFile) as fd:
      for line in fd.readlines():
        copy.writelines(line)

def deleteFile():
  shouldClean = input('Delete created file? Y|n ')
  if shouldClean != 'n':
    print('Deleting ', copyFile)
    try:
      if os.path.exists(copyFile):
        os.remove(copyFile)
    except Exception as e:
      print('Failed to delete: ', copyFile)

# ---------------------------------------------------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
  
  parseArgs()
  readFile()
  writeFile()
  
  # TODO: append copied file with the content of this file.

  deleteFile()
