from PIL import Image

from fryer import fryer

'''
    Quick meme thrown together with the help of StackOverflow and some GitHub repos found online
'''


def load():
    image = Image.open(input('Enter the image name: '))
    layers = int(input('How many layers do you want? '))
    emote_amount = int(input('How many emotes per layer do you want? '))
    noise = float(input('Noise level (recommended from 0.1 to 1): '))
    contrast = float(input('Contrast level (0-500 or more): '))
    return image, layers, emote_amount, noise, contrast


if __name__ == '__main__':
    image, layers, emote_amount, noise, contrast = load()

    fried = fryer.fry(image, emote_amount, noise, contrast)
    for layer in range(layers - 1):
        fried = fryer.fry(fried, emote_amount, noise, contrast)

    fried.save('out.png')
