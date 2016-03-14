$(document).ready(function() {
	var vid = document.querySelector('video');
	vid.addEventListener('ended', function(ev) {
		vid.currentTime = 0.1;
		vid.play();
	});
	vid.load();
	vid.addEventListener('loadeddata', function(ev) {
		vid.play();
		$('img.poster').addClass('fadeOut');
		$('video').addClass('fadeIn');
	});
})
