# Backend Auto-Correct Documentation
backend's initial index command gives the documentation of our backend code so
all methods and arguments are detailed in how to use the backend auto correct
docs.
The backend uses two different routes for getting and inserting words
into our compare tree. The first route is GET /auto-correct/?link=<value> 
This will take the query parameter “link” and should respond with a JSON object 
that has all words within a distance <= 2 away from the query word. The query 
parameter value “slokk”, for example, should be “slack” if we want to navigate 
to the CUAir slack, NOT “cuair/slack”! 
The second route is POST /insert-words This will take a JSON object with an 
array called “links”, that will load valid links into the wordTree. It responds 
with a JSON object that contains a list of parent node strings. If the word 
wasn’t inserted, the string should be “not_inserted”. If the node became the 
root and doesn’t have a parent, the string should be “none”.


## Usage of Getting links
**Definition**
`GET links`

**Response**

- `200 OK` on success

```json
{
    "links" : "String List holding all available links"
}
```

### Adding words to our collection of useable links

**Definition**
`POST links`

**Arguments**
- "json": containing a key value of links holding a string list of all links
- "links": list string of all unique links within the json that we wish to add 
            to the tree
        
**Response**

-`201 Created` on success

```json
{
    "closest_parent" : ['none', 'cuair', 'cuair', 'plane', 'not_inserted']
}
