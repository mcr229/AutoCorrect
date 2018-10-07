#import the necessary modules to back end
import wordTree
from flask import Flask, request, jsonify, Response, abort, render_template
#using flask to handle GET and POST requests
app = Flask(__name__)

#creation of our similarWords tree with edit distance of 2
similarWords = wordTree.wordTree(2)


#checks that str_lst is a list of only strings
def checkStringList(str_lst):
    for x in str_lst:
        if not isinstance(x, str):
            return False
    return True
#checks that key is a key in key_lst
def isKey(key_lst, key):
    for x in key_lst:
        if x == key:
            return True
    return False

"""
[index] is used for to give the documentation of our backend device
"""
@app.route('/')
def index():
    return render_template("docs.html")

"""
[GET] handles all auto correct calls and requires the signatuer '/auto_correct/'
and a link argument after it; it is always a GET method. If there are no words
to compare it to then will return a 404 message, otherwise a json containing 
the similar links is given as a response.
"""
@app.route('/auto-correct/', methods = ['GET'])
def GET():
    #requires argument link and gives us the word that it contains
    queryword = request.args.get('link')
    #if the word somehow has a none type, or link does not work then
    #abort to HTTP 400 bad request
    if(queryword == None):
        abort(400)
    #if nothing is in our tree then we give an empty list of compareable words
    if(similarWords.getWord() == None):
        return jsonify({"links": []}), 200
    else:
        #add all words to possible and then output as json
        possible = similarWords.get_similar_words(queryword)
        return jsonify({"links": possible}), 200

"""
[POST] handles all word insertions and requires the signature '/insert-words' 
and a valid json request. It is always a post method. If a non-valide json 
request is made, then a 404 message is outputted. Otherwise, a json of the
closest parents are given as a response, and the links are added to the
similar word tree.
"""
@app.route('/insert-words', methods = ['POST'])
def POST():
    #requests a json
    content = request.get_json()
    #if links is not a key in the json the abort 400 bad request
    if not isKey(content.keys(), "links"):
        abort(400)
    #set the given links into variable list_of_links
    list_of_links = content['links']
    #check the typing of the list and aborts if it is not a list of strings
    if not ((isinstance((list_of_links), list)) and 
                                            (checkStringList(list_of_links))):
        abort(400)
    #accumulator for our response list
    acc = []
    #insert words into tree and then add the responses to accumulator
    for x in list_of_links:
        acc = acc + [similarWords.insert(x)]
    return jsonify({"closest_parent" : acc}), 201

#runs the program.
if __name__ == '__main__':
    app.run(debug=True)