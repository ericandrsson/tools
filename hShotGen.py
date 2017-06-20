import os


def ShotGen():
    folderList = ['io/incoming', 'io/outgoing', 'geo/assets/cameras', 'geo/assets/characters', 'geo/assets/FX',
                  'geo/assets/vehicles', 'maps/HDRI', 'maps/textures', 'production/docs', 'production/reviews']

    for folder in folderList:
        if not os.path.exists(folder):
            os.makedirs(folder)


ShotGen()




