from django.db import models


class EmotionPlaylist(models.Model):
    name=models.CharField(max_length=10)
    img=models.ImageField(upload_to='images/emotion/')





class Song(models.Model):
    title= models.TextField()
    EmotionPlaylist=models.ForeignKey(EmotionPlaylist,on_delete=models.CASCADE)
    artist= models.TextField()
    image= models.ImageField(upload_to="images/")
    audio_file = models.FileField(upload_to="songs/", blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)
    

    def __str__(self):
        return self.title