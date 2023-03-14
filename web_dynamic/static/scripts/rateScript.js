$(document).ready(function () {
	// Get the modal
	var modals = document.querySelectorAll('[id^=deleteModal]');
	console.log(modals);
	
	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
		// console.log(event.target.id);
		Array.prototype.forEach.call(modals, callback);

		function callback(element, iterator) {
			// console.log(iterator, element.id);
			if (event.target.id == element.id) {
				element.style.display = "none";
			}
		}
		
	}

	var property_id = null;
	$(".deletebtn").each(function (indexInArray, valueOfElement) { 
		console.log($(valueOfElement));
		 $(valueOfElement).click(function () {
			var value = $(valueOfElement).siblings('.propertyId').data('id');
			// var value = $('.propertyId').data('id');
			property_id = value
			console.log(value);
			$.ajax({
				url: '/properties/property_id',
				type: 'DELETE',
				success: function(result) {
					console.log("Success");
				}
			});
		});
	});




	var rateStatus = document.getElementById("rate")
	var score = document.getElementById("show_rate")

	score.innerHTML = rateStatus.value;

	rateStatus.oninput = function () {
		score.innerHTML = this.value;	
	}


});