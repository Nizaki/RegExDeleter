import fnmatch
import os
import glob
for dir in os.walk('.'):
    print(dir[0])
    f240p = glob.glob(dir[0]+'/*240p.mp4')
    f360p = glob.glob(dir[0]+'/*360p.mp4')
    f480p = glob.glob(dir[0]+'/*480p.mp4')
    f720p = glob.glob(dir[0]+'/*720p.mp4')
    f1080p = glob.glob(dir[0]+'/*1080p.mp4')
    print(dir[0])
    if not f1080p:
        if not f720p:
            if not f480p:
                if not f360p:
                    if not f240p:
                        print(dir[0], 'found nothing')
                else:
                    print('360 found delete the rest')
                    for filepath in f240p:
                        try:
                            os.remove(filepath)
                            print('removing', filepath)
                        except:
                            print("error while deleteing file : ", filepath)
            else:
                print('480 found delete the rest')
                for filepath in f240p+f360p:
                    try:
                        os.remove(filepath)
                        print('removing', filepath)
                    except:
                        print("error while deleteing file : ", filepath)
        else:
            print('780 found detete the rest')
            for filepath in f240p+f360p+f480p:
                try:
                    os.remove(filepath)
                    print('removing', filepath)
                except:
                    print("error while deleteing file : ", filepath)
    else:
        print('1080 found delete the rest')
        for filepath in f240p+f360p+f480p+f720p:
            try:
                os.remove(filepath)
                print('removing', filepath)
            except:
                print("error while deleteing file : ", filepath)
