# MusicOnEmotion
Steps to start Project
1. Clone this repository in your local.
2. Create virtual environment and install packages in requirements.txt file using following command,
   pip install -r requirements.txt
3. Migrate model to database using,
   python manage.py makemigrations
   python manage.py migrate
4. Create superuser using
   python manage.py createsuperuser
5. Login to admin pannel and Add Playlists Happy,Sad,Angree,Nuetral and add song to each playlist like add happy songs to happy playlist.
6. Go to https://drive.google.com/file/d/1BAfniPXQZLu8TZC0BI_TIJosjpRlgsnY/view?usp=sharing    and download model.h5 file.
7. Add this model file in project base direcrory where manage.py file is there.
8. Run development server using
   python manage.py runserver
   
