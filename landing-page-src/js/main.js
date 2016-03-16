$(document).ready(function() {

    var shouldPlayVideo = false;
    // Provided we have autoplay or no touch events
    // (ie desktop) play the video
    Modernizr.on('videoautoplay', function(result) {
        shouldPlayVideo = !!result;
        if (result) {
            console.log('supported videoautoplay');
        } else {
            console.log('not supported videoautoplay');
        }

        if (!shouldPlayVideo && !Modernizr.touchevents) {
            console.log('No touch events');
            shouldPlayVideo = true;
        }

        if (shouldPlayVideo) {
            playVideo();
        }
    });

    function playVideo() {
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
    }
})
