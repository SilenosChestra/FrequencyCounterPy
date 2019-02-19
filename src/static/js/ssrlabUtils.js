'use strict'

function setLocale(locale) {
	window.location.href = window.location.pathname + "?lang="+locale.substr(0,2);
}

$(document).ready(function() {
	$('.setLocale').click(function(e) {
		e.preventDefault(); 
		var localeId = $( this ).attr('href');
		switch (localeId) {
			case "#By":
				setLocale("be_BY.UTF-8");
				break;
			case "#Ru":
				setLocale("ru_RU.UTF-8");
				break;
			case "#En":
				setLocale("en_US.UTF-8");
				break;
			default:
				setLocale("en_US.UTF-8");
				break;
		}
	});
});