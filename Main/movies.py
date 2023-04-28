import imdb
from concurrent.futures import ThreadPoolExecutor

class MovieRecommendation:
    def __init__(self):
        """
        Initialize an instance of the MovieRecommendation class with the imdb module's Cinemagoer.
        """
        self.ia = imdb.Cinemagoer()

    def get_movie_data(self, movie_id):
        """
        Given a movie_id, return a tuple of the movie's title, rating and year.

        Args:
            movie_id (str): The id of the movie.

        Returns:
            tuple: A tuple of the movie's title, rating and year.
        """
        movie = self.ia.get_movie(movie_id)
        return (movie.get('title'), movie.get('rating'), movie.get('year'))

    def recommend_movie(self, genre, min_rating, year):
        """
        Given a genre, minimum rating and year, recommend top 5 movies that match the criteria.

        Args:
            genre (str): The genre of the movie to be recommended.
            min_rating (float): The minimum rating of the movie to be recommended.
            year (int): The minimum year of the movie to be recommended.

        Returns:
            list: A list of tuples containing the title, rating and year of the top 5 recommended movies.
        """
        results = self.ia.get_top50_movies_by_genres(genre)
        filtered_results = [r for r in results if r.get('rating') and r['rating'] >= min_rating and r['year'] >= year]
        sorted_results = sorted(filtered_results, key=lambda r: r['rating'], reverse=True)
        final_lst = []
        movie_ids = [r.movieID for r in sorted_results]
        with ThreadPoolExecutor() as executor:
            movie_data = list(executor.map(self.get_movie_data, movie_ids))
        for title, rating, year in movie_data:
            final_lst.append((title, f"{rating}", f"{year}"))
        return final_lst

    def recommendation_lst_shorter(self, lst):
        """
        Given a list of movie recommendations, return a shorter list of maximum 5 recommendations.

        Args:
            lst (list): A list of tuples containing the title, rating and year of recommended movies.

        Returns:
            str: A string for the list of shortened movie recommendations.
        """
        if len(lst) > 5:
            lst_fet = lst[0:5]
        else:
            lst_fet = lst
        if len(lst) > 1 and len(lst) >= 5:
            nu_lst = [f"Recommendation number {i + 1}: {lst[i][0]}" for i in range(len(lst_fet))]
            string = "\n".join(["".join(item) for item in nu_lst])
            string_final = "Here are my Top 5 Recommendations: \n" + string
        elif len(lst) == 1:
            string_final = [f"I recommend watching: {lst[0][0]}"]
        else:
            nu_lst = [f"Recommendation number {i + 1}: {lst[i][0]}" for i in range(len(lst_fet))]
            string = "\n".join(["".join(item) for item in nu_lst])
            string_final = "Here are my Top Recommendations: \n" + string

        return string_final

    #a staticmethod to organize the output list to user
    @staticmethod
    def stringer(lst):
        if len(lst) > 5:
            lst_fet = lst[0:5]
        else:
            lst_fet = lst
        return "\n".join([", ".join(item) for item in lst_fet])

