import requests
import json

# ---------------------------------------------------------------------------------------------------------------------
# TO KNOW
# ---------------------------------------------------------------------------------------------------------------------
# requests is an additional lib that requires install:
# pip install requests
# ---------------------------------------------------------------------------------------------------------------------
# For this topic, we'll be using JSONPlaceholder (https://jsonplaceholder.typicode.com),
# a Fake Online REST API for Testing and Prototyping 
# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
# CONSTANTS
# ---------------------------------------------------------------------------------------------------------------------
JSON_PLACE_HOLDER_URL = 'https://jsonplaceholder.typicode.com'
POSTS_PATH = '/posts'

HEADER = {
  'Content-Type': 'application/json; charset=UTF-8'
}

HTTP_STATUS_OK = 200
HTTP_STATUS_CREATED = 201

# ---------------------------------------------------------------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------------------------------------------------------------
def getAllPosts():
  print('Retrieving all posts from server...')

  url = JSON_PLACE_HOLDER_URL + POSTS_PATH
  
  try:
    response = requests.get(url, headers=HEADER)

    if response.status_code == HTTP_STATUS_OK:
      parseResponse(response)
    else:
      print('Non success response returned')
      print('Status: ' + str(response.status_code), ' ', response.reason)
  except Exception as e:
    print('Oops! Looks like something went wrong!')
    printException(e)
    exit(1)

def createPost():
  print('Posting a post (^_^)')

  url = JSON_PLACE_HOLDER_URL + POSTS_PATH

  try:
    response = requests.post(url, data=payload(), headers=HEADER)

    if response.status_code == HTTP_STATUS_CREATED:
      post = response.json()
      printPost(post)
    else:
      print('Non success response returned')
      print('Status: ' + str(response.status_code), ' ', response.reason)
  except Exception as e:
    print('Oops! Looks like something went wrong!')
    printException(e)
    exit(1)

def parseResponse(response):
  print('Total posts: ', len(response.json())) # response.json() is an array of dictionnaries
  for post in response.json():
    printPost(post)
  print('')

def printPost(post):
  print('# ----------------------------------------------------------------------------------------------------------')
  print('# POST: ', post['id'])
  print('# ----------------------------------------------------------------------------------------------------------')
  print('userId: ', post['userId'])
  print('title: ', post['title'])
  print('content: ', post['body'])

def payload():
  payload = {
      'userId': 200,
      'title': 'Why I Droped The \"Ne\"',
      'body': 'C\'était un lundi, au quatrième étage...'
  }
  return json.dumps(payload)

def printException(exception):
  for arg in exception.args:
    print(arg)

# ---------------------------------------------------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
  
  getAllPosts()
  createPost()
