import math

class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for el in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: str):
        for i in range(len(self.photos)):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                j = self.photos[i].index(label)
                return f"{label} photo added successfully on page {i+1} slot {j+1}"
        return "No more free spots"

    def display(self):
        representation = "-" * 11
        for i in range(len(self.photos)):
            representation += f"\n {len(self.photos[i]) * '[]'} \n {'-' * 11}"
        representation += "\n"
        return representation