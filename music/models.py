from django.db import models


def tmp_directory(instance, filename):
    """Get tmp directory"""
    return f"music/tmp/{filename}"


def song_directory_path(instance, filename):
    """Get song directory path to save."""
    fileExtension = filename.rsplit('.', 1)[1]
    return f"music/songs/{instance.id}_{instance.name}.{fileExtension}"


def image_artist_directory_path(instance, filename):
    """Get image of the artist directory path to save."""
    fileExtension = filename.rsplit('.', 1)[1]
    return f"artist/image/{instance.id}_{instance.name}.{fileExtension}"


class Artist(models.Model):
    """Artist Model."""

    id = models.AutoField(auto_created=True, primary_key=True,
                          serialize=False, verbose_name='ID')
    name = models.CharField(max_length=200)
    image = models.ImageField(
        null=True, upload_to=image_artist_directory_path)

    def __str__(self):
        """Get str representation."""
        return self.name

    def __repr__(self):
        """Get str representation."""
        return self.__str__()

    def save(self, *args, **kwargs):
        """Sobrecargamos el metodo save para que almacende de forma corrercta los id's"""
        if self.pk is None:
            saved_image = self.image
            self.image = None
            super(Artist, self).save(*args, **kwargs)
            self.image = saved_image
        super(Artist, self).save(*args, **kwargs)


class Song(models.Model):
    """Song model."""

    id = models.AutoField(auto_created=True, primary_key=True,
                          serialize=False, verbose_name='ID')
    name = models.CharField(max_length=200)
    song_file = models.FileField(null=True, upload_to=song_directory_path)

    # Relations
    artist = models.ManyToManyField("music.Artist", related_name="songs")

    def __str__(self):
        """Get str representation"""
        artist_str = ""
        artist = list(self.artist.all())
        if(len(artist) == 0):
            return f"{self.name}"
        artist_str = f"{artist[0].name}"
        for artist in artist[1:]:
            artist_str += f", {artist.name}"
        return f"{self.name} by {artist_str}"

    def __repr__(self):
        """Get str representation."""
        return self.__str__()

    def save(self, *args, **kwargs):
        """Sobrecargamos el metodo save para que almacende de forma corrercta los id's"""
        if self.pk is None:
            saved_song = self.song_file
            self.song_file = None
            super(Song, self).save(*args, **kwargs)
            self.song_file = saved_song
        super(Song, self).save(*args, **kwargs)

    def get_song_path(self):
        return "media/" + self.song_file.name
