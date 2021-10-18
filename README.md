# Spotify Playlist Cover Creator

Transform this

<img src="background.jpg" width="200">

Into this

<img src="Chill Vibes cover.jpg" width="200">

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
