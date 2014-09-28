$(document).ready(function() {
	$("#send-btn").click(function(){
		var emailBody = $(".htapQuestionContainer").html();
		var smsBody = $("#questionID").find(".htapSection").text();
		smsb = String(smsBody);
		
 
		var textboxEmail = $("#email").val();
		var textboxSms   = $("#sms").val();
 
		$("#check").removeClass('show').addClass('hide');
        $("#loading").removeClass('hide').addClass('show');
 
        
 
		$.ajax({
  		url: "/twilio/",
  		data: {"to": textboxSms, "message": smsb},
        type:'GET',
        success: function(){
			
      	},
      	});
 
		$.ajax({
  		url: "/sendgrid/",
  		data: {"to": textboxEmail , "message": emailBody},
        type:'GET',
        success: function(){
    	    $("#loading").removeClass('show').addClass('hide');
			$("#check").removeClass('hide').addClass('show');
		},
		error: function(){
			$("#loading").removeClass('show').addClass('hide');
			$("#error").removeClass('hide').addClass('show');
		},
      	});
 
	});
});