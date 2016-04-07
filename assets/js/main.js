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


	// modal behaviour
	if (false && $(window).width() > 700) {
		var urlToId = function(url) {
			return url.split('/').join('');
		}

		$('.project-content').each(function(i,e) {
			var element = $(e);
			element.attr('id', urlToId(element.attr('data-url')));
		})

		$('.project > a').click(function(event) {
			event.preventDefault();
			var url_split = event.delegateTarget.href.split('/');
			var last_part = url_split[url_split.length - 1];
			var content = $("#" + last_part).toggle();
			console.log(content);
		});
	}


});
