$(document).ready(function () {
	var rateStatus = document.getElementById("rate")
	var score = document.getElementById("show_rate")

	score.innerHTML = rateStatus.value;

	rateStatus.oninput = function () {
		score.innerHTML = this.value;	
	}

});