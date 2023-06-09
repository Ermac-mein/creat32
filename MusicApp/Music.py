import tkinter as tk
from tkinter import filedialog
import pygame


class MusicPlayerApp:
    def __init__(self, master):
        self.master = master
        master.title("Music Player")

        # Create buttons
        self.play_button = tk.Button(master, text="Play", command=self.play_music)
        self.play_button.pack()

        self.pause_button = tk.Button(master, text="Pause", command=self.pause_music)
        self.pause_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_music)
        self.stop_button.pack()

        self.load_button = tk.Button(master, text="Load Music", command=self.load_music)
        self.load_button.pack()

        self.volume_scale = tk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_scale.set(50)  # Default volume level
        self.volume_scale.pack()

        self.progress_bar = tk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL)
        self.progress_bar.pack()

        # Initialize pygame mixer
        pygame.mixer.init()

        self.playlist = []
        self.current_song_index = None

    def play_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()
        else:
            if self.current_song_index is not None:
                song_path = self.playlist[self.current_song_index]
                pygame.mixer.music.load(song_path)
                pygame.mixer.music.play()

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume) / 100)

    def load_music(self):
        filetypes = (("MP3 files", "*.mp3"), ("All files", "*.*"))
        selected_files = filedialog.askopenfilenames(filetypes=filetypes)
        for file in selected_files:
            self.playlist.append(file)
        if self.current_song_index is None:
            self.current_song_index = 0

    def update_progress_bar(self):
        if pygame.mixer.music.get_busy():
            current_position = pygame.mixer.music.get_pos() / 1000  # in seconds
            song_duration = pygame.mixer.music.get_length() / 1000  # in seconds
            progress = (current_position / song_duration) * 100
            self.progress_bar.set(progress)
        else:
            self.progress_bar.set(0)

        self.master.after(1000, self.update_progress_bar)

root = tk.Tk()
app = MusicPlayerApp(root)
root.after(1000, app.update_progress_bar)  # Start progress bar update after 1 second
root.mainloop()
