// Converts utc epoch-seoncds (time index used by reddit API) into 
// JavaScript date object
var cursor = db.posts.find();
var document = cursor.hasNext() ? cursor.next() : null;

while(document) {
	var utcSec = document.data.children[0].data.created;
	var d = new Date(0);
	d.setUTCSeconds(utcSec);
	db.posts.update( {'data.children.0.data.id': document.data.children[0].data.id}, {$set:{'data.children.0.data.created': d}} );
	
	printjson(d);
	document = cursor.hasNext() ? cursor.next() : null;

}

