$(document).ready(function () {
	// Get the modal
	var modals = document.querySelectorAll('[id^=deleteModal]');
	// console.log(modals);
	
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


	
	$('#search-property').on('click', function (e) { 
		if ($('filter-results').val() !== "") {
			console.log("happy");
			$('#filter-results').load(location.href + ' #filter-results');
		}
		let search_word = $('#search-input').val();
		$.ajax({
		type: 'POST',
		url: '/properties/search/'+search_word,
		contentType: 'application/json',
		data: '{}',
		success: function (data) {
			console.log(data);
		for (let properties of data) {
			$('#filter-results').append('<div class="results"><div class="upper-result">\
				<div class="result-img">\
					<div class="big-img">\
						<img src='+ properties.img_path +' alt="">\
					</div>\
				</div>\
				<div class="details">\
					<div class="buttons">\
						<button class="sale">'+properties.availability.toUpperCase()+'</button>\
						<button class="new">NEW</button>\
					</div>\
					<div class="description">\
						<div class="inner-description">\
							<h4>'+properties.description+'</h4>\
							<p>\
								<i class="fa fa-map-marker location" aria-hidden="true"></i> \
								'+properties.state
							+'</p>\
							<p class="landmarks">\
								<i class="fa fa-compass" aria-hidden="true"></i>\
								'+properties.landmark
							+'</p>\
						</div>\
					</div>\
					<div class="price">\
						<div class="text-price">\
							<p>Price</p>\
						</div>\
						<div class="amount">\
							<h4>#'+properties.price+'</h4>'
							+'<button><a href="{{url_for('+'"details",'+'property_id=property.id)}}">Take a tour</a></button>'
						+'</div>'+
					'</div>'+
				'</div>'+
			'</div>'+
		'</div>');
		}
		}
	});
	});


	// var rangeInput = document.querySelector('input[type="range"]');
	// if (rangeInput === null) {
	// 	rangeInput.value = 1;
	// 	console.log(rangeInput.value);
	// }
	var rateStatus = document.getElementById("rate")
	var score = document.getElementById("show_rate")
	if (rateStatus.value == null) {
		rateStatus.value = 1
	}
	// console.log(rateStatus.value);
	score.innerHTML = rateStatus.value;

	rateStatus.oninput = function () {
		score.innerHTML = rateStatus.value;	
	}


});