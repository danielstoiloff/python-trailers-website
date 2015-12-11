import webbrowser

class Movie():
    """This is some sample documentation for the Class Movie."""
    RATINGS = ["P", "PG", "PG13", "R"]

    #Initialize constructor
    def __init__(this_self, name, plot, image_url, trailer_url):
        this_self.title = name
        this_self.storyline = plot
        this_self.poster_image_url = image_url
        this_self.trailer_youtube_url = trailer_url

    #Play trailer 
    def showTrailer(self):
        webbrowser.open_new_tab(self.trailer_youtube_url)

