function LoadPrinter(config, rootElement) {
	this.name = config.name;
	this.customLoadingFn = config.load;
	this.rootElement = rootElement;
	this.element = document.createElement('div');
	this.element.innerHTML = '<div class="load-printer">' +
		'<span class="title"></span>' +
		'<span class="dots"></span>' +
		'<span class="result"></span>' +
		'</div>';
	this.rootElement.appendChild(this.element);
	this.load();
};

LoadPrinter.prototype = {
	load: function () {
		var self = this;
		this.startTime = new Date().getTime();
		this.printStartLoading();
		this.customLoadingFn(function() {
			self.printEndLoading();
		});
	},

	printStartLoading: function() {
		this.type('Loading ' + this.name + ' ', this.element.querySelector('.title'));
	},

	printEndLoading: function() {
		this.type('DONE in ' + (new Date().getTime() - this.startTime) / 1000 + ' seconds', this.element.querySelector('.result'));
	},

	type: function (string, element, config) {
		var config = config || {};
		var default_config = {
			strings: [string],
			showCursor: false,
			typeSpeed: 0
		};
		for (var key in default_config) {
			config[key] = config[key] || default_config[key];
		}

		if (window.jQuery) {
			// stop any animation on that element
			this.typer && this.typer.complete();
			$(element).typed({
				strings: [string],
				typeSpeed: 0,
				showCursor: false
			});
		} else {
			this.typer = new Typer(element, config);
			this.typer.type(string);
		}
	}
};


function Typer(element, config) {
	config = config || {};
	this.element = element;
	this.charPause = config.charPause || 1;
	this.callback = config.callback || function () {};
}

Typer.prototype = {
	type: function (string, strPos) {
		var self = this;
		strPos = strPos || 0;
		self.isTyping = true;

		if (self._stop) {
			return;
		}

		if (self._complete) {
			self.element.innerText = string;
			return;
		}

		if (strPos === string.length) {
			self.isTyping = false;
			return self.callback();
		}

		var charPause = self.charPause * 30;
		var humanize = Math.round(Math.random() * (charPause * 3 - charPause));

		setTimeout(function () {
			self.element.innerText = string.substr(0, strPos + 1);
			strPos ++;
			self.type(string, strPos)
		}, humanize);
	},

	stop: function () {
		this._stop = true;
	},

	complete: function () {
		this._complete = true;
	}
};


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
