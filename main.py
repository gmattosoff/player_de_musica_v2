from tkinter import *
import customtkinter as ctk
from PIL import ImageTk, Image
from pygame import mixer

window = Tk()
window.title('Player de Música v2')
window.geometry('570x500')
window.resizable(False, False)
window.config(background='black')

songs = ['meantime','moon','never']
covers = ['meantime','moon','never']

mixer.init()
song = 'meantime'
index = 0
vol = 0.5
vol_text = 5

cover1 = Image.open(f'player_de_musica_v2/covers/meantime.png')
resized_image = cover1.resize((300,300))
cover1 = ImageTk.PhotoImage(resized_image)

cover2 = Image.open(f'player_de_musica_v2/covers/moon.png')
resized_image = cover2.resize((300,300))
cover2 = ImageTk.PhotoImage(resized_image)

cover3 = Image.open(f'player_de_musica_v2/covers/never.png')
resized_image = cover3.resize((300,300))
cover3 = ImageTk.PhotoImage(resized_image)

label = Label(image=cover1, anchor=N)
label.place(x=130, y=70)


def atualizar_cover():
    global song
    if song == 'meantime':
        label.config(image=cover1)
    elif song == 'moon':
        label.config(image=cover2)
    elif song == 'never':
        label.config(image=cover3)


def tocar(song):
    global song_tocando, song_name
    mixer.music.load(f'player_de_musica_v2/songs/{song}.mp3')
    mixer.music.play()
    song_tocando = song
    mixer.music.set_volume(vol)
    play_pause_btn.config(image=pause_img, command=lambda: pausar())
    nome()
    now_playing.config(text=f'Now playing: {song_name}')


def pausar():
    global pausado, now_playing
    mixer.music.pause()
    pausado = True
    if covers[index] == song_tocando:
        play_pause_btn.config(image=play_img, command=lambda: despausar())
    else:
        play_pause_btn.config(image=play_img, command=lambda: tocar(song))


def despausar():
    global pausado, now_playing
    mixer.music.unpause()
    pausado = False
    play_pause_btn.config(image=pause_img, command=lambda: pausar())
    

def proxima():
    global song, index
    index = songs.index(song)
    if songs[index] != 'never':
        index += 1
    else:
        index = 0
    song = songs[index]
    atualizar_cover()


def anterior():
    global song, index
    index = songs.index(song)
    if songs[index] != 'meantime':
        index -= 1
    else:
        index = 2
    song = songs[index]
    atualizar_cover()


def aumentar():
    global vol, vol_text
    if vol_text < 10:
        vol += 0.1
        vol_text += 1
        mixer.music.set_volume(vol)
        print(vol)
        number.config(text=vol_text)
        centralizar()


def diminuir():
    global vol, vol_text
    if vol_text > 0:
        vol -= 0.1
        vol_text -= 1
        mixer.music.set_volume(vol)
        number.config(text=vol_text)
        centralizar()


def centralizar():
    if vol_text != 10:
        number.place(x=56, y=189)
    else:
        number.place(x=45, y=189)


def nome():
    global song_name
    if song_tocando == 'never':
        song_name = 'Never Let Me Down Again'
        now_playing.place(x=70)
    elif song_tocando == 'moon':
        song_name = 'The Killing Moon'
        now_playing.place(x=115)
    else:
        song_name = 'In The Meantime'
        now_playing.place(x=115)


pause_img = Image.open('player_de_musica_v2/imgs/pause.png')
pause_img = ImageTk.PhotoImage(pause_img)

play_img = Image.open('player_de_musica_v2/imgs/play.png')
play_img = ImageTk.PhotoImage(play_img)

play_pause_btn = Button(window, image=play_img, command=lambda: tocar(song))
play_pause_btn.place(x=244, y=395)

next_img = Image.open('player_de_musica_v2/imgs/next.png')
next_img = ImageTk.PhotoImage(next_img)
next_btn = Button(window, image=next_img, command=lambda: proxima())
next_btn.place(x=320, y=420)

prev_img = Image.open('player_de_musica_v2/imgs/previous.png')
prev_img = ImageTk.PhotoImage(prev_img)
prev_btn = Button(window, image=prev_img, command=lambda: anterior())
prev_btn.place(x=215, y=420)

plus_img = Image.open('player_de_musica_v2/imgs/plus.png')
plus_img = ImageTk.PhotoImage(plus_img)
plus_btn = Button(window, image=plus_img, command=lambda: aumentar())
plus_btn.place(x=50, y=150)

minus_img = Image.open('player_de_musica_v2/imgs/minus.png')
minus_img = ImageTk.PhotoImage(minus_img)
minus_btn = Button(window, image=minus_img, command=lambda: diminuir())
minus_btn.place(x=50, y=240)

now_playing = Label(window, text='Selecione uma música', background='black', fg='white', font=('Helvetica bold', 18))
now_playing.place(x=160, y=20)

number = Label(window, text=vol_text, background='black', fg='white', font=('Helvetica bold', 26))
centralizar()

window.mainloop()