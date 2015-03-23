## Viewport
Set width and height of the viewport
Initial scale is for inital zoom level (need initial-scale 1 for landscape iOS)

examples

	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="viewport" content="width=500, height=600, initial-scale=1">

## Media queries
set styles portrait

	@media all and (orientation: portrait) { ... }

device independent pixel

	window.devicePixelRatio

## Responsive images
Send DPR (density pixel ratio) in header (with vary to avoid caching)

## Touch
- ~10 mm for a touch button
- Don't rely on hover

a

	if ('ontouchstart' in window) {
		addTouchHandlers();
	}

## Device access

	<input type="file" accept="image/*;capture=camera||camcorder||microphone">

or

	navigator.getUserMedia({video: true}, fn)

get media

	MediaStreamTrack.getSources(fn)

fullscreen

	element.webkitRequestFullscreen()

geoloc

	navigator.geolocation.watchPosition

## Offline

	navigator.onLine

	<html manifest="manifest.appcache">