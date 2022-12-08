from PIL import Image
class GIF():
    def split_gif_into_frames(self):
        num_key_frames = 14

        with Image.open('laba8/start.gif') as im:
            for i in range(num_key_frames):
                im.seek(im.n_frames // num_key_frames * i)
                im.save('laba8/cat{}.png'.format(i))


    def create_gif_from_frames(self):
        frames = []
        for frame_number in range(0,14):
            frame = Image.open(f'laba8/cat{frame_number}.png')
            frames.append(frame)

        frames[0].save(
            'laba8/finish.gif',
            save_all=True,
            append_images=frames[0:],
            optimazie=True,
            duration=140,
            loop=0
        )
GIF().split_gif_into_frames()
GIF().create_gif_from_frames()


"""Узнаем сколько кадров в гифке"""
"""im = Image.open('laba8/start.gif')
print("Number of frames: "+str(im.n_frames))"""