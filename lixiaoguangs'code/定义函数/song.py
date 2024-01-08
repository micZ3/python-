def song_s(singer,songname):
    song_list = singer +''+songname
    return song_list.title()

while True:
    print("\nWhat's your favorite song?" )
    print("enter 'q' and you will quit !")
    sisnger = input("sidnger:  ")
    if sisnger =='q':
        break
    songname = input("songname:  ")
    if songname == 'q':
        break

    
    whole_songs = song_s(sisnger,songname)
    print("\nThis is your fauourite song---"+ whole_songs)

 


