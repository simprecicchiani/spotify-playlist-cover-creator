# Spotify Playlist Cover Creator

[![status](https://img.shields.io/badge/Follow%20me%20on-Spotify-green)](https://open.spotify.com/user/1166736052?si=52be728bc0fa4ce8)

|Transform this|Into this|
|:---|:---|
|<img src="background.jpg" height="200">|<img src="Chill Vibes cover.jpg" height="200">|

With this simple script
```
$ python3 main.py backgroung.jpg 'Chill Vibes' white center
```

### Manual
Requires `python3` and `pillow` installed. Script arguments:
- backgroung image directory
- cover title (in a string)
- text color (format `white` or `#ffffff` or `(255, 255, 255)`)
- text vertical position (either `center` or `up` or `down`)
