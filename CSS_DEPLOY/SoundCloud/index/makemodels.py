from models import Playlist
from faker import faker

l = [1, 2, 3, 4, 5]

for i in l:
    for j in range(5):
        myfake = Faker('ko_KR')
        pl = PlayList()
        pl.title = myfake.word()
        pl.name = myfake.name()
        pl.img = "#"
        pl.mood = i
        pl.save()

