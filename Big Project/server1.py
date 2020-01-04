#Question 3

from flask import Flask, jsonify, request, abort

app = Flask(__name__, 
        static_url_path='', 
        static_folder='.')

blogposts=[{"post_id":1, "Subject":"Living Abroad", "Author_id":"Emmigrant2020", "Body":"Living in Spain is great","totalPosts":1},
{"post_id":2, "Subject":"Further Education", "Author_id":"Student2020", "Body":"Studying at night is hard","totalPosts":1},
{"post_id":3, "Subject":"Favourite Sport", "Author_id":"Sports2020", "Body":"Football is the best","totalPosts":1}
]

nextId=4

#@app.route('/')
#def index():
    #return "Hello, World!"

# curl "http://127.0.0.1:5000/blogposts"
@app.route("/blogposts")
def getAll():
    return jsonify(blogposts)

#curl "http://127.0.0.1:5000/blogposts/3"
#{"Author":"Sports2020","Body":"Football is the best","Subject":"Favourite Sport","id":3}
@app.route("/blogposts/<int:post_id>")
def findBy(post_id):
    foundBlogPosts = list(filter(lambda p: p["post_id"] == post_id, blogposts))
    if len(foundBlogPosts) == 0:
            return jsonify({}) , 204
    return jsonify(foundBlogPosts[0])

#curl -i -H "Content-Type:application/json" -X POST -d "{\"Author\":\"PoliticsNerd1\",\"Subject\":\"Vote Fine Gael\",\"Body\":\"Sure aren't they fine\"}" "http://127.0.0.1:5000/blogposts"
@app.route("/blogposts", methods=["POST"])
def create():
    global nextId
    if not request.json:
        abort(400)
        #do other checking format/other
    blogpost = {
        "post_id": nextId,
        "Author_id": request.json["Author_id"],
        "Subject": request.json["Subject"],
        "Body": request.json["Body"],
        "TotalPosts":1
    }
    nextId += 1
    blogposts.append(blogpost)
    #Do add to Author here
    return jsonify(blogpost)
    #return (nextId)

#curl -i -H "Content-Type:application/json" -X PUT -d "{\"Author\":\"PoliticsNerd1\",\"Subject\":\"Never Vote Fine Gael\",\"Body\":\"Sure aren't they crooks\"}" "http://127.0.0.1:5000/blogposts/4"
@app.route("/blogposts/<int:post_id>", methods=["PUT"])
def update(id):
    foundBlogPosts = list(filter(lambda p: p["post_id"] == id, blogposts))
    if len(foundBlogPosts) == 0:
        abort(404)
    foundBlogPost = foundBlogPosts[0]
    if not request.json:
        abort(400)
    reqJson = request.json
    if "Author_id" in reqJson:
        foundBlogPost["Author_id"] = reqJson["Author_id"]
    if "Subject" in reqJson:
        foundBlogPost["Subject"] = reqJson["Subject"]
    if "Body" in reqJson:
        foundBlogPost["Body"] = reqJson["Body"]
    #Do add to Author here

    return jsonify(foundBlogPost)

@app.route("/blogposts/<int:post_id>", methods=["DELETE"])
def delete(id):
    foundBlogPosts = list(filter(lambda p: p["post_id"] == id, blogposts))
    if len(foundBlogPosts) == 0:
        abort(404)
    blogposts.remove(foundBlogPosts[0])
    return jsonify({"done":True})

@app.route("/data/<string:Author_id>", methods=["POST"])
def addToAuthor(Author_id):
    print("test")
    foundBlogPost = list(filter(lambda a: a["Author_id"] == Author_id, blogposts))
    if len(foundBlogPost) == 0:
        abort(404)
    if not request.json:
        abort(400)
    #if not "Author_id" in request.json or type(request.json["Author_id"]) is not str:
        abort(401)
    
    newPost = request.json["Author_id"]
    
    foundBlogPost[0]["totalPosts"] += newPost
    
    return jsonify(foundBlogPost[0])

@app.route("/data/authorHistory")
def getPosts():
    blogposts.sort(key=lambda x: x.totalPosts, reverse=True)
    return jsonify(blogposts)

if __name__ == '__main__' :
    app.run(debug= True)

