// twitterDateCreate.js converts string-formatted dates in a MongoDB 
// which were obtained from the Twitter API into JavaScript Date() objects
var cursor = db.posts.find();
var document = cursor.hasNext() ? cursor.next() : null;

while(document) {
		db.posts.update( {_id:document._id}, {$set:{"created_at":new Date(document.created_at)}} );
		printjson(document.created_at);

document = cursor.hasNext() ? cursor.next() : null;

}

