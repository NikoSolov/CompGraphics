# pip install fastprogress
# pip install pydub
#import pip
#pip.main(['install','fastprogress','pydub'])

from pydub import AudioSegment
from pydub.utils import mediainfo
from fastprogress import progress_bar

import os
import glob
from pathlib import Path
from concurrent.futures.process import ProcessPoolExecutor
import concurrent

def parallel(func, arr, max_workers):
    """
    Call `func` on every element of `arr` in parallel using `max_workers`.
    Adapted from fastai. Thanks!
    """
    if max_workers<2: _ = [func(o,i) for i,o in enumerate(arr)]
    else:
        with ProcessPoolExecutor(max_workers=max_workers) as ex:
            futures = [ex.submit(func,o,i) for i,o in enumerate(arr)]
            for f in progress_bar(concurrent.futures.as_completed(futures), total=len(arr)): pass

def proc_vid(v, i):
    video, pth_to, pth = v
    mp3_filename = pth_to/video.parent.relative_to(pth)/(video.stem + '.mp3')
    os.makedirs(mp3_filename.parent, exist_ok=True)
    cover_dir = None
    # Try to discover a cover image in the current album's folder
    # by looking for generic filenames.
    if os.path.isfile(video.parent/'cover.jpg'):
        cover_dir = video.parent/'cover.jpg'
    elif os.path.isfile(video.parent/'cover.png'):
        cover_dir = video.parent/'cover.jpg'
    elif os.path.isfile(video.parent/'Cover.jpg'):
        cover_dir = video.parent/'Cover.jpg'
    elif os.path.isfile(video.parent/'Cover.png'):
        cover_dir = video.parent/'Cover.png'
    elif os.path.isfile(video.parents[1]/'cover.jpg'):
        cover_dir = video.parents[1]/'cover.jpg'
    elif os.path.isfile(video.parents[1]/'cover.png'):
        cover_dir = video.parents[1]/'cover.jpg'
    elif os.path.isfile(video.parents[1]/'Cover.jpg'):
        cover_dir = video.parents[1]/'Cover.jpg'
    elif os.path.isfile(video.parents[1]/'Cover.png'):
        cover_dir = video.parents[1]/'Cover.png'

    k = AudioSegment.from_file(video, format='flac')
    if cover_dir is not None:
        k.export(str(mp3_filename), format='mp3', tags=mediainfo(str(video)).get('TAG', {}), cover=str(cover_dir))
    else:
        k.export(str(mp3_filename), format='mp3', tags=mediainfo(str(video)).get('TAG', {}))

def convert():
    folder_with_albums = './my_mixtape_archives/'  # Path with folders of flac files
    extension_list = ('**/*.flac',)

    dirs = os.listdir(folder_with_albums)

    for ost in dirs:
        if ost.endswith('-mp3'): continue
        print("\nConverting ", ost, '\n')
        pth = Path(folder_with_albums)/ost
        
        i = 0
        pth_to = Path(pth.name + '-mp3')
        os.makedirs(pth_to, exist_ok=True)

        for extension in extension_list:
            videos = [(f, pth_to, pth) for f in pth.glob(extension)]
            if len(videos) > 0:
  
                parallel(proc_vid, videos, max_workers=os.cpu_count())
                break

    print('\n\n')

if __name__ == "__main__":
    convert()