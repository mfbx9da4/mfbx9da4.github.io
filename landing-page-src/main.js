include "loadPrinter.js"

include "typer.js"

var resources = [
	{
		name: 'javascript',
		load: function(fn) {
			$script('/assets/js/landing-page-libs.min.js', 'libs');
			$script.ready(['libs'], fn);
		}
	}, {
		name: 'vid',
		load: function(fn) {
			var vid = document.querySelector('video');
			vid.addEventListener('progress', function(ev) {
				console.log('progress');
			});
			vid.addEventListener('loadeddata', function(ev) {
				console.log('loaded video');
				fn();
				setTimeout(function () {
					$(vid).removeClass('hide');
					$('.loader').addClass('hide');
					$('.intro').removeClass('hide');
					$('.intro div').typed({
						strings:["Hey, ^500 I'm Dave the dev. ^500<br>That's me on the right. ^500<br>That is where I live. ^500<br>This is my <a href='/'>site</a>. ^500"],
						showCursor: false,
						typeSpeed: 20
					});
					$('.print').addClass('hide');
				}, 1000);
			});
		}
	}, {
		name: 'fonts',
		load: function (fn) {
			var start = new Date().getTime();
			WebFontConfig = {
			  google: { families: ['Dancing+Script::latin'] },
			  fontactive: function(familyName, fvd) {
			  	console.log('loaded font');
				fn()
			  },
			};
			getGoogleFonts();
		}
	}
];

var printHello = function (printElement) {
	var div = document.createElement('div');
	printElement.appendChild(div);
	var typer = new Typer(div);
	typer.type('Hey give me a sec :-)');
}

var printElement = document.querySelector('main .print');

printHello(printElement);

for (var i = 0; i < resources.length; i ++) {
	var resource = resources[i];
	var loader = new LoadPrinter(resource, printElement);
}

function getGoogleFonts() {
  var wf = document.createElement('script');
  wf.src = ('https:' == document.location.protocol ? 'https' : 'http') +
    '://ajax.googleapis.com/ajax/libs/webfont/1/webfont.js';
  wf.type = 'text/javascript';
  wf.async = 'true';
  var s = document.getElementsByTagName('script')[0];
  s.parentNode.insertBefore(wf, s);
};
