function myFunction(){
	alert("Testing sample javascript!");
}

function time(){
	var time = new Date($.now());
	var current_time = time.getHours() + ":" + time.getMinutes() + ":" + time.getSeconds();
	alert("Current time is: " + current_time);
}

$(document).ready(function(){ 

	$("#test").text("Jquery library is loaded");
	
	// Add the value of "Search..." to the input field and a class of .empty
	$("#search").val("Search...").addClass("empty");
	
	// When you click on #search
	$("#search").focus(function(){
		
		// If the value is equal to "Search..."
		if($(this).val() == "Search...") {
			// remove all the text and the class of .empty
			$(this).val("").removeClass("empty");;
		}
		
	});
	
	// When the focus on #search is lost
	$("#search").blur(function(){
		
		// If the input field is empty
		if($(this).val() == "") {
			// Add the text "Search..." and a class of .empty
			$(this).val("Search...").addClass("empty");	
		}
		
	});

});
//document.getElementById("icon rainy").style.visibility = "hidden";
//$("#sun_shower").hide();
