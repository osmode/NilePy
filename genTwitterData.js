// Iterates through the posts to generate a second-indexed histogram
// The results are printed to the screen
// Note that the dates hard-coded

var cursor = db.posts.find();
var document = cursor.hasNext() ? cursor.next() : null;
var values = new Array(); 

max = 10000

for(i = 0; i < max; i++)
	values[i] = 0;

while(document) {

		year = document.created_at.getYear();
		date = document.created_at.getDate();
		hour = document.created_at.getHours();
		min = document.created_at.getMinutes();
		sec = document.created_at.getSeconds();

		tp = (date -27)*24*60 + (hour*60) + min;
		values[tp] = values[tp]+1;

document = cursor.hasNext() ? cursor.next() : null;

}

for(i = 0; i < max; i++) {
	if(values[i] > 0)
		print(i+' '+values[i]);
}

