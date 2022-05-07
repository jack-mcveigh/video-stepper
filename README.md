# Video Stepper

| Author | Email |
| ------ | ----- |
| Jack McVeigh | <jmcveigh5@gmail.com> |

---

## Purpose
To view view frame by frame footage of any mp4 video.

---

## Overview
The originally intended use was to view a loop of all nine main Star Wars movies buffered frame by frame with the effect of a slideshow. Now, the tool can play playlists of movies/tv shows, such as the Star Wars franchise and Friends, or single videos such as single movies or homemade movies.

![Example](assets/readme/raspberry_pi_display.png)
***Note: Users must supply their own, legally acquired mp4 files for use.***

---

## Installation
To install, run the following:
```bash
git clone https://github.com/jmcveigh55/video-stepper.git
cd video-stepper
source venv/bin/activate
pip3 install .
```

## Use


* To play a video:
>```bash
>source venv/bin/activate
>video-stepper video.mp4 &
>```

* To play a video with custom framerate:
>```bash
>source venv/bin/activate
>video-stepper video.mp4 -f 0.25 &
>```

* To play a playlist:
>The playlist should be in the format:
>```json
>{
>    ...,
>    "data": [
>        "video-1.mp4",
>        "video-2.mp4",
>        ...
>    ],
>    ...
>}
>```
>or
>```csv
>video_name,...
>video-1.mp4,...
>video-2.mp4,...
>```
> Run the following:
>```bash
>source venv/bin/activate
>video-stepper -p playlist.json &
>```
>or
>```bash
>source venv/bin/activate
>video-stepper -p playlist.json &
>```

* To loop indefinitely when using a playlist:
>```bash
>source venv/bin/activate
>video-stepper -p playlist.json -l &
>```

* To shuffle a playlist (When used with looping, playlist is shuffled each iteration):
>```bash
>video-stepper -p playlist.json -s
>```