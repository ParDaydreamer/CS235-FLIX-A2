from datetime import date, datetime
from typing import List, Iterable


class User:
    def __init__(
            self, username: str, password: str
    ):
        self._username: str = username
        self._password: str = password
        self._comments: List[Comment] = list()
        self.__watched = list()
        self.__reviews = list()
        self.__time_spent = 0

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str:
        return self._password

    @property
    def comments(self) -> Iterable['Comment']:
        return iter(self._comments)

    def add_comment(self, comment: 'Comment'):
        self._comments.append(comment)

    @property
    def watched_movies(self):
        return self.__watched

    @watched_movies.setter
    def watched_movies(self, watched):
        if isinstance(watched, list):
            self.__watched = watched

    @property
    def reviews(self):
        return self.__reviews

    @reviews.setter
    def reviews(self, rvws):
        if isinstance(rvws, list):
            self.__reviews = rvws

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, time_spent):
        if isinstance(time_spent, int):
            self.__time_spent = time_spent

    def watch_movie(self, movie):
        self.__watched.append(movie)
        self.__time_spent += movie.runtime_minutes

    def add_review(self, review):
        self.__reviews.append(review)

    @property
    def __repr__(self):
        return f"<User {self.__username}>"

    def __eq__(self, other):
        if self._username == other._username:
            return True
        else:
            return False

    def __lt__(self, other):
        if self._username < other._username:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self._username + str(self._password))


class Comment:
    def __init__(
            self, user: User, movie: 'Movie', comment: str, timestamp: datetime
    ):
        self._user: User = user
        self._movie: Movie = movie
        self._comment: Comment = comment
        self._timestamp: datetime = timestamp

    @property
    def user(self) -> User:
        return self._user

    @property
    def movie(self) -> 'Movie':
        return self._movie

    @property
    def comment(self) -> str:
        return self._comment

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    def __eq__(self, other):
        if not isinstance(other, Comment):
            return False
        return other._user == self._user and other._movie == self._movie and other._comment == self._comment and other._timestamp == self._timestamp

class Review:
    def __init__(self, movie: 'Movie', user: User, rating: float) -> None:
        self.__movie = movie
        self.__user = user
        if 0 < rating < 11:
            self.__rating = rating
        else:
            self.__rating = None
        self.__timestamp = datetime.today()

    @property
    def movie(self):
        return self.__movie

    @property
    def user(self):
        return self.__user

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp

    def __repr__(self):
        return f'<Review {self.__movie}, {self.__review_text}, {self.__rating}, {self.__timestamp}>'

    def __eq__(self, other):
        if self.__movie == other.movie:
            return (self.__user == other.user and self.__rating == other.rating and self.__timestamp == other.timestamp)
        else:
            return False

'''class Article:
    def __init__(
            self, date: date, title: str, first_para: str, hyperlink: str, image_hyperlink: str, rank: int = None
    ):
        self._rank: int = rank
        self._year: date = date
        self._title: str = title
        self._first_para: str = first_para
        self._hyperlink: str = hyperlink
        self._image_hyperlink: str = image_hyperlink
        self._comments: List[Comment] = list()
        self._tags: List[Tag] = list()

    @property
    def rank(self) -> int:
        return self._rank

    @property
    def date(self) -> date:
        return self._year

    @property
    def year(self) -> date:
        return self._year

    @property
    def title(self) -> str:
        return self._title

    @property
    def first_para(self) -> str:
        return self._first_para

    @property
    def hyperlink(self) -> str:
        return self._hyperlink

    @property
    def image_hyperlink(self) -> str:
        return self._image_hyperlink

    @property
    def comments(self) -> Iterable[Comment]:
        return iter(self._comments)

    @property
    def number_of_comments(self) -> int:
        return len(self._comments)

    @property
    def number_of_tags(self) -> int:
        return len(self._tags)

    @property
    def tags(self) -> Iterable['Tag']:
        return iter(self._tags)

    def is_tagged_by(self, tag: 'Tag'):
        return tag in self._tags

    def is_tagged(self) -> bool:
        return len(self._tags) > 0

    def add_comment(self, comment: Comment):
        self._comments.append(comment)

    def add_tag(self, tag: 'Tag'):
        self._tags.append(tag)

    def __repr__(self):
        return f'<Article {self._year.isoformat()} {self._title}>'

    def __eq__(self, other):
        if not isinstance(other, Article):
            return False
        return (
                other._year == self._year and
                other._title == self._title and
                other._first_para == self._first_para and
                other._hyperlink == self._hyperlink and
                other._image_hyperlink == self._image_hyperlink
        )

    def __lt__(self, other):
        return self._year < other._year'''

class Movie:
    def __init__(self, title=None, year=None, rank: int = None):
        self.__rank = rank
        self.__title = None
        if (isinstance(title, str) and len(title) > 0):
            self.__title = title.strip()
        self.__year = None
        if (isinstance(year, int) and year >= 1900):
            self.__year = year
        self.__description = None
        self.__director = None
        self.__runtime_minutes = 0
        self.__actors = []
        self.__genres = []
        self._comments: List[Comment] = list()
        self._hyperlink: str = f"https://www.imdb.com/find?s=tt&q={self.__title}"
        self._image_hyperlink: str = "static/movie.png"
        self._rating = float(10)
        self._votes = 0
        self._revenue = 'N/A'
        self._metascore = 'N/A'

    @property
    def votes(self):
        return self._votes

    @votes.setter
    def votes(self, votes):
        self._votes = int(votes)

    @property
    def revenue(self):
        return self._revenue

    @revenue.setter
    def revenue(self, revenue):
        self._revenue = revenue

    @property
    def metascore(self):
        return self._metascore

    @metascore.setter
    def metascore(self, metascore):
        self._metascore = metascore

    @property
    def rating(self):
        return round(self._rating, 2)

    @rating.setter
    def rating(self, rating):
        self._rating = rating

    def add_rating(self, rating: int):
        pass

    def set_rating(self, rating:int, user: User):
        self._rating = ((self._votes * self._rating) + rating) / (self._votes+1)
        self._votes += 1

    @property
    def hyperlink(self) -> str:
        return self._hyperlink

    @property
    def image_hyperlink(self) -> str:
        return self._image_hyperlink

    @image_hyperlink.setter
    def image_hyperlink(self, hyperlink:str):
        self._image_hyperlink = hyperlink

    def is_of_genre(self, genre:'Genre'):
        return genre in self.__genres

    @property
    def comments(self) -> Iterable[Comment]:
        return iter(self._comments)

    def add_comment(self, comment: Comment):
        self._comments.append(comment)

    @property
    def rank(self) -> int:
        return self.__rank

    @property
    def date(self) -> int:
        return self.__year

    @property
    def year(self) -> date:
        return self.__year


    def __repr__(self):
        return f"<Movie {self.__title}, {self.__year}>"

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, ttl):
        if (isinstance(ttl, str) and len(ttl) > 0):
            self.__title = ttl.strip()

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, dscrptn):
        if (isinstance(dscrptn, str) and len(dscrptn) > 0):
            self.__description = dscrptn.strip()

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, drctr):
        if (isinstance(drctr, Director)):
            self.__director = drctr

    @property
    def director_name(self) -> str:
        print(self.__director_full_name)
        return self.__director_full_name

    '''def director_name(self) -> str:
        return self.__director_full_name'''

    @property
    def genres(self):
        return self.__genres

    @genres.setter
    def genres(self, genres):
        if (isinstance(genres, list)):
            self.__genres = genres

    @property
    def runtime_minutes(self):
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime):
        if (isinstance(runtime, int)):
            if (runtime >= 0):
                self.__runtime_minutes = runtime
            else:
                raise ValueError

    @property
    def actors(self):
        return self.__actors

    @actors.setter
    def actors(self, actor_list):
        if (isinstance(actor_list, list)):
            self.__actors = actor_list

    def actors_list(self):
        ctrlst = ' '
        for actor in self.__actors:
            ctrlst += actor
        return ctrlst

    def add_genre(self, genre):
        if (isinstance(genre, Genre)):
            if not genre in self.__genres:
                self.__genres.append(genre)

    def remove_genre(self, genre):
        if (isinstance(genre, Genre)):
            if genre in self.__genres:
                self.__genres.remove(genre)
        elif (isinstance(genre, str)):
            for genre in self.__genres:
                if genre.genre_name == genre:
                    self.__genres.remove(genre)

    def add_actor(self, actor):
        if (isinstance(actor, Actor)):
            if not actor in self.__actors:
                self.__actors.append(actor)

    def add_director(self, director):
        if (isinstance(director, Director)):
            if director != self.__director:
                self.__director == director

    def remove_actor(self, actor):
        if (isinstance(actor, Actor)):
            if actor in self.__actors:
                self.__actors.remove(actor)
        elif (isinstance(actor, str)):
            for actor in self.__actors:
                if actor.actor_full_name == actor:
                    self.__actors.remove(actor)

    def __eq__(self, other):
        if self.__title == other.__title:
            return (self.__year == other.__year)
        else:
            return False

    def __lt__(self, other):
        if self.__title == other.__title:
            return (self.__year < other.__year)
        else:
            return (self.__title < other.__title)

    def __hash__(self):
        return hash(self.__title + str(self.__year))

class Director:
    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()
        self._director_asso_movies: List[Movie] = list()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    @director_full_name.setter
    def director_full_name(self, full_name):
        if full_name == "" or type(full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = full_name.strip()

    @property
    def director_asso_movies(self) -> Iterable[Movie]:
        return iter(self._director_asso_movies)

    @property
    def number_of_directed_movies(self) -> int:
        return len(self._director_asso_movies)

    def is_director_of(self, movie: Movie) -> bool:
        if movie in self._director_asso_movies:
            return True
        return False

    def __repr__(self):
        return f"<Director {self.director_full_name}>"

    def __eq__(self, other: 'Director'):
        if type(self) == type(other):
            if self.director_full_name == other.director_full_name:
                return True
        return False

    def __lt__(self, other: 'Director'):
        if type(self) == type(other):
            if self.director_full_name < other.director_full_name:
                return True
        if type(self) != type(other):
            raise TypeError
        return False

    def __hash__(self):
        return hash(self.director_full_name)

    def add_movie(self, movie):
        if (isinstance(movie, Movie)):
            if not movie in self._director_asso_movies:
                self._director_asso_movies.append(movie)

    def remove_movie(self, movie):
        if (isinstance(movie, Movie)):
            if movie in self._director_asso_movies:
                self._director_asso_movies.remove(movie)
        elif (isinstance(movie, str)):
            for movie in self._director_asso_movies:
                if movie.name == movie:
                    self._director_asso_movies.remove(movie)


class Genre:

    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()
        self._genre_asso_movies: List[Movie] = list()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    @genre_name.setter
    def genre_name(self, name: str):
        if name == "" or type(name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = name.strip()

    @property
    def genre_asso_movies(self) -> Iterable[Movie]:
        return iter(self._genre_asso_movies)

    @property
    def number_of_tagged_movies(self) -> int:
        return len(self._genre_asso_movies)

    def is_applied_to(self, movie: Movie) -> bool:
        return movie in self._genre_asso_movies

    def add_movie(self, movie: Movie):
        self._genre_asso_movies.append(movie)

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if self.genre_name != other.genre_name or type(other) is not Genre:
            return False
        else:
            return True

    def __lt__(self, other):
        if self.genre_name >= other.genre_name or type(other) is not Genre:
            return False
        else:
            return True

    def __hash__(self):
        return hash(self.genre_name)


class Actor:
    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.colleagues = set()
        self._actor_asso_movies = list()

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    @actor_full_name.setter
    def actor_full_name(self, full_name):
        if full_name == "" or type(full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = full_name.strip()

    @property
    def actor_asso_movies(self) -> list():
        return self._actor_asso_movies

    @property
    def number_of_acted_movies(self) -> int:
        return len(self._actor_asso_movies)

    def is_actor_of(self, movie: Movie) -> bool:
        if movie in self._actor_asso_movies:
            return True
        return False

    @property
    def actor_name(self) -> str:
        return self.__actor_full_name

    '''def actor_name(self) :
        return self.__actor_full_name'''

    def __repr__(self):
        return f"<Actor {self.actor_full_name}>"

    def __eq__(self, other: 'Actor'):
        if type(self) == type(other):
            if self.actor_full_name == other.actor_full_name:
                return True
        return False

    def __lt__(self, other: 'Actor'):
        if type(self) == type(other):
            if self.actor_full_name < other.actor_full_name:
                return True
        if type(self) != type(other):
            raise TypeError(f"Type error, should be actor")
        return False

    def __hash__(self):
        return hash(self.actor_full_name)

    def add_actor_colleague(self, colleague: 'Actor'):
        if type(self) != type(colleague):
            raise TypeError(f"Colleague should be actor")
        self.colleagues.add(colleague)

    def check_if_this_actor_worked_with(self, other):
        if type(self) != type(other):
            raise TypeError("Colleague should be actor")
        else:
            return other in self.colleagues

    def add_movie(self, movie):
        if (isinstance(movie, Movie)):
            if not movie in self._actor_asso_movies:
                self._actor_asso_movies.append(movie)
        else:
            print(123)

    def remove_movie(self, movie):
        if (isinstance(movie, Movie)):
            if movie in self._actor_asso_movies:
                self._actor_asso_movies.remove(movie)
        elif (isinstance(movie, str)):
            for movie in self._actor_asso_movies:
                if movie.name == movie:
                    self._actor_asso_movies.remove(movie)


class ModelException(Exception):
    pass


def make_comment(comment_text: str, user: User, movie: Movie, timestamp: datetime = datetime.today()):
    comment = Comment(user, movie, comment_text, timestamp)
    user.add_comment(comment)
    movie.add_comment(comment)

    return comment


def make_genre_association(movie: Movie, genre: Genre):
    if genre.is_applied_to(movie):
        raise ModelException(f'Genre {genre.genre_name} already applied to Movie "{movie.title}"')

    movie.add_genre(genre)
    genre.add_movie(movie)

def make_director_association(movie: Movie, director: Director):
    if director.is_director_of(movie):
        raise ModelException(f'director {director.director_name} already applied to Movie "{movie.title}"')

    movie.add_director(director)
    director.add_movie(movie)


def make_actor_association(movie: Movie, actor: Actor):
    if actor.is_actor_of(movie):
        raise ModelException(f'actor {actor.actor_name} already applied to Movie "{movie.title}"')

    movie.add_actor(actor.actor_name)
    actor.add_movie(movie)


def make_year_association(movie: Movie, year: int):
    if year.is_applied_to(movie):
        raise ModelException(f'Year {year} already applied to Movie "{movie.title}"')
    movie.add_genre(year)
