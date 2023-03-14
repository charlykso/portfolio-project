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
	// getting each element with the delete btn
	$(".deletebtn").each(function (indexInArray, valueOfElement) { 
		// console.log($(valueOfElement));
		 $(valueOfElement).click(function () {
			var value = $(valueOfElement).siblings('.propertyId').data('id');
			
			property_id = value
			// console.log(value);
			try{
				$.ajax({
					url: '/properties/'+property_id,
					type: 'DELETE',
					success: function(result) {
						if (result.msg === "Successful") {
							location.reload()
							$('h5#psuccess').html(result.msg)
							console.log(result.msg);
						}
					},
					error: function(err) {
						$("h5#perror").html(err.statusText)
						console.log(err.statusText);
					}
					
				});
			} catch (error)
			{
				$("h5#perror").html(err.statusText)
				console.log(error);
			}
		});
	});




	var rateStatus = document.getElementById("rate")
	var score = document.getElementById("show_rate")

	score.innerHTML = rateStatus.value;

	rateStatus.oninput = function () {
		score.innerHTML = this.value;	
	}


});