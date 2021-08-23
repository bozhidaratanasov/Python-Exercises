from project.album import Album


class Band:
    albums = []

    def __init__(self, name):
        self.name = name

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for album in self.albums:
            if album.name == album_name and not album.published:
                return f"Album {album_name} has been removed."
            elif album.name == album_name and album.published:
                return "Album has been published. It cannot be removed."
        return f"Album {album_name} is not found."

    def details(self):
        album_details = ""
        for album in self.albums:
            album_details += album.details() + "\n"

        return f"Band {self.name} \n" \
               f"{album_details}"
