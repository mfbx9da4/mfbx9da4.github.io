$(document).ready(function() {

    // If view port too short leave blurred
    if ($(window).height() < 500) {
        return;
    }

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
        } else {
            loadImage();
        }
    });

    function loadImage() {
        var fallback = $('img.poster.fallback');
        var source = '/assets/img/4415.png';

        var img = new Image();
        img.onload = function () {
            console.log('loaded');
            fallback.attr('src', source);
            fallback.css({display: 'block'});
            $('img.poster.blurred').addClass('fadeOut');
            fallback.addClass('fadeIn');
        }
        img.src = source;
    }

    function playVideo() {
        var vid = document.querySelector('video');
        vid.addEventListener('ended', function(ev) {
            vid.currentTime = 0.1;
            vid.play();
        });
        vid.load();
        vid.addEventListener('loadeddata', function(ev) {
            vid.play();
            $('img.poster.blurred').addClass('fadeOut');
            $('video').addClass('fadeIn');
        });
    }
})
