$(document).ready(function() {
	$('h1.title').hover(function() {
		$('.profile-img').addClass('hover');
	});
	$('h1.title').mouseleave(function() {
		$('.profile-img').removeClass('hover');
	});

	$('.profile-img').hover(function() {
		$('.hover-message').show();
		$('.hover-message').addClass('bounceInUp');
	});

	$('.profile-img').mouseleave(function() {
		$('.hover-message').hide();
		$('.hover-message').removeClass('bounceInUp');
	});


	/*====================================
	=            Morph Button            =
	====================================*/

    var docElem = window.document.documentElement, didScroll, scrollPosition;

    // trick to prevent scrolling when opening/closing button
    function noScrollFn() {
        window.scrollTo( scrollPosition ? scrollPosition.x : 0, scrollPosition ? scrollPosition.y : 0 );
    }

    function noScroll() {
        window.removeEventListener( 'scroll', scrollHandler );
        window.addEventListener( 'scroll', noScrollFn );
    }

    function scrollFn() {
        window.addEventListener( 'scroll', scrollHandler );
    }

    function canScroll() {
        window.removeEventListener( 'scroll', noScrollFn );
        scrollFn();
    }

    function scrollHandler() {
        if( !didScroll ) {
            didScroll = true;
            setTimeout( function() { scrollPage(); }, 60 );
        }
    };

    function scrollPage() {
        scrollPosition = { x : window.pageXOffset || docElem.scrollLeft, y : window.pageYOffset || docElem.scrollTop };
        didScroll = false;
    };

    scrollFn();

    var morphButtons = []

    $('.morph-button').each(function(i, elem) {
    	if (Modernizr.csstransitions || $(window).width() < 400) {
		    morphButtons.push(new UIMorphingButton(elem, {
		        closeEl : '.icon-close',
		        onBeforeOpen : function() {noScroll();},
		        onAfterOpen : function() {noScroll();},
		        onBeforeClose : function() {noScroll();},
		        onAfterClose : function() {canScroll();}
		    }));
    	} else {
    		$(elem).click(function(ev) {
    			var target = $(ev.target);
    			window.target = target;
    			var href = target.closest('.project').attr('href');
    			window.location.href = href;
    		})
    	}
    })
	/*=====  End of Morph Button  ======*/

    $(document.body).click(function(event) {
        if ($(event.target).parents('.morph-content').length < 1) {
            closeModal();
        }
    });

    function closeModal() {
        for (var i = 0; i < morphButtons.length; i ++) {
            var button = morphButtons[i];
            var buttonEl = $(morphButtons[i].el);
            if (buttonEl.hasClass('active')) {
                button.toggle();
            }
        }
    }

    $(document.body).keydown(function(event) {
        if (event.keyCode == 27) {
            // esc key
            closeModal();
        } else if (event.keyCode == 37 || event.keyCode == 39) {
            var goRight = event.keyCode == 39;
            for (var i = 0; i < morphButtons.length; i ++) {
                var button = morphButtons[i];
                var buttonEl = $(morphButtons[i].el);
                if (buttonEl.hasClass('active')) {
                    if (goRight) {
                        var next_i = (i + 1) % morphButtons.length;
                    } else {
                        var next_i = (i - 1) % morphButtons.length;
                    }
                    var nextButton = morphButtons[next_i];
                    button.toggle();
                    setTimeout(function () {nextButton.toggle()}, 800)
                    break;
                }
            }
        }
    })

});
