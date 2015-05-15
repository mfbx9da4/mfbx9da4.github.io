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