import requests

# Please do not run this script a lot (more than once a minute) since the call getAllMovies can be resource intensive
# If you would like to test this script you can use the call getMoviesByTitle like this: 
#           response = requests.get("http://bechdeltest.com/api/v1/getMoviesByTitle?title=matrix")
response = requests.get("http://bechdeltest.com/api/v1/getAllMovies")
file_object = open('bachdel-unabridged.csv', 'w')
file_object.write('id,year,title,rating,pass\n')
file_object.close()
file_object = open('bachdel.csv', 'a')
i = 1
for movie in response.json():
	pass_str = "0"
	rating_str = ""
	if 'rating' in movie:
		rating_str = str(movie['rating'])
		if(movie['rating'] == 3):
			pass_str = "1"
        id_str = ""
        if 'id' in movie:
		id_str = str(movie['id'])
        year_str = ""
	if 'year' in movie:
		year_str = str(movie['year'])
	title_str = ""
	if 'title' in movie:
		title_str = movie['title']
	row = ""
	row += id_str + ','
	row += year_str + ',' 
	row += title_str.replace(",", ".") + ','
	row += rating_str + ','
	row += pass_str + ',' + '\n'
	file_object.write(row)
	print(str(i) + ": " + row)
	if not ('id' in movie and 'year' in movie and 'title' in movie  and 'rating' in movie):
		print("Bad row: " + str(movie))
	i += 1
file_object.close()


