from django.shortcuts import redirect, render,get_object_or_404
import cv2
from .models import EmotionPlaylist,Song
from django.contrib import messages
from django.db.models import Q

def home(request):
	songs=Song.objects.all()
	return render(request,'01_Home.html',{'songs':songs})

def profile(request):
	return render(request,'Profile.html')

def recentlyPlayed(request):
	songs=Song.objects.all()
	return render(request,'03_RecentlyPlayed.html',{'songs':songs})

def favourite(request):
	return render(request,'05_Favourite.html')

def playlist(request):
	playlists=EmotionPlaylist.objects.all()
	for i in playlists:
		print(i.img)
	return render(request,'04_Playlist.html',{'playlists':playlists})

def accounts(request):
	return render(request,'player.html')

def capture(request):
	return render(request,'camera.html')

	
def detect(request):
	emotion_dict = {0: "Angry", 1: "Disgust", 2: "Fear", 3: "Happy", 4: "Sad", 5: "Surprise", 6: "Neutral"}
	from keras import models
	import cv2
	import numpy as np
	model = models.load_model('model.h5')

	#cap = cv2.VideoCapture(0)


	#ret, frame = cap.read()
	frame=cv2.imread("images/im2.jpg")
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
		roi_gray = gray[y:y + h, x:x + w]
		cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
		cv2.normalize(cropped_img, cropped_img, alpha=0, beta=1, norm_type=cv2.NORM_L2, dtype=cv2.CV_32F)
		prediction = model.predict(cropped_img)
		
		cv2.putText(frame, emotion_dict[int(np.argmax(prediction))], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
		print(emotion_dict[int(np.argmax(prediction))])
		emotion=emotion_dict[int(np.argmax(prediction))]
		playlists=EmotionPlaylist.objects.filter(name=emotion)

	return render(request,'04_Playlist.html',{'playlists':playlists})

def songs(request,id):
	playlist=EmotionPlaylist.objects.filter(id=id)
	for playlist in playlist:
		name=playlist.name
	songs=Song.objects.filter(EmotionPlaylist_id=id)
	return render(request,'Songs.html',{'songs':songs,'name':name})
	
def search(request):
	name=request.POST['search']
	if name:
		songs=Song.objects.filter(Q(title__icontains=name) | Q(artist__icontains=name))
		if songs:
			return render(request,'Songs.html',{'songs':songs})
		else:
			messages.error(request,'No Songs Found')
			return redirect('home')
	
	return redirect('home')

def play(request,id):
    obj= get_object_or_404(Song,pk=id)
    data ={
        'obj':obj
    }
    return render(request,'playsong.html',data)