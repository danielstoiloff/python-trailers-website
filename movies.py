import fresh_tomatoes
import media


shawshank = media.Movie("Shawshank Redemption",
                        "A banker who is sentenced to life in Shawshank State Penitentiary.",
                        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

the_godfather = media.Movie("The Godfather",
                     "Marlon Brando and Al Pacino are the leaders of the fictional Corleone New York crime family",
                     "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                     "https://www.youtube.com/watch?v=fB_8VCwXydM")

the_godfather_2 = media.Movie("The Godfather Part II",
                       "Both sequel and prequel to The Godfather",
                       "https://upload.wikimedia.org/wikipedia/en/0/03/Godfather_part_ii.jpg",
                       "https://www.youtube.com/watch?v=8PyZCU2vpi8")

pulp_fiction = media.Movie("Pulp Fiction",
                       "American black comedy crime film written and directed by Quentin Tarantino.",
                       "https://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
                       "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

the_good_the_bad = media.Movie("The Good, the Bad and the Ugly",
                       "Three gunslingers competing to find fortune in a buried cache.",
                       "https://upload.wikimedia.org/wikipedia/en/4/45/Good_the_bad_and_the_ugly_poster.jpg",
                       "https://www.youtube.com/watch?v=WCN5JJY_wiA")

twelve_angry = media.Movie("12 Angry Men",
                       "12 men as they deliberate the guilt or acquittal of a defendant on the basis of reasonable doubt.",
                       "https://upload.wikimedia.org/wikipedia/en/9/91/12_angry_men.jpg",
                       "https://www.youtube.com/watch?v=fSG38tk6TpI")

movies = [shawshank, the_godfather, the_godfather_2, pulp_fiction, the_good_the_bad, twelve_angry]

fresh_tomatoes.open_movies_page(movies)
