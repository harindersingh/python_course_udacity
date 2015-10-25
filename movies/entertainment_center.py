import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
					"A marine on an alien planet",
					"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					"https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock",
					"Using rock music to learn",
					"https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
					"https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
					"A rat is a chef in Paris",
					"http://ia.media-imdb.com/images/M/MV5BMTMzODU0NTkxMF5BMl5BanBnXkFtZTcwMjQ4MzMzMw@@._V1_SX214_AL_.jpg",
					"https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_Paris = media.Movie("Midnight in Paris",
					"Going back in time to meet at authors",
					"https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/215px-Midnight_in_Paris_Poster.jpg",
					"https://www.youtube.com/watch?v=5nOF93SzX6s")

hunger_games = media.Movie("Hunger Games",
					"A really real reality show",
					"http://www.apnatimepass.com/the-hunger-games-catching-fire-movie-poster-1.jpg",
					"https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_Paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)