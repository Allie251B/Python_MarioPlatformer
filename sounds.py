from pygame import mixer


class Sound:
    def __init__(self):
        self.music_channel = mixer.Channel(0)
        self.music_channel.set_volume(0.2)
        self.sound_channel = mixer.Channel(1)
        self.sound_channel.set_volume(0.2)

        self.allowSound = True

        self.soundtrack = mixer.Sound("./backgrounds/sound/soundtrack.mp3")
        self.pickup = mixer.Sound("./backgrounds/sound/bonus2.wav")
        self.hit = mixer.Sound("./backgrounds/sound/hit.wav")
        self.death = mixer.Sound("./backgrounds/sound/death.wav")
        self.jump = mixer.Sound("./backgrounds/sound/jump.wav")
        self.click = mixer.Sound("./backgrounds/sound/clicks.mp3")
        self.complete = mixer.Sound("./backgrounds/sound/level_completed.wav")
        self.health = mixer.Sound("./backgrounds/sound/health.wav")

    def play_sound(self, sfx):
        if self.allowSound:
            self.sound_channel.play(sfx)

    def play_music(self, music):
        self.music_channel.play(music)