function checkEmail(){
    var email = document.getElementById("Email").value;
    $('#preloader').show();
    $.ajax({
        url: CheckEmailURL,
        type: "POST",
        headers: {
            "X-CSRFToken": csrfToken
          },
        data: {
            email: email
        },
        dataType: 'json',
        success: function(data){
            if(data.message == "Login")
            {
                console.log("Login");
                $(".step-1").removeClass("active");
                $(".step-2").addClass("active");
            }
            else if(data.message == "Register")
            {
                console.log("Register");
                $(".step-1").removeClass("active");
                $(".step-3").addClass("active");
            }
            else if(data.message == "Invalid Email"){
                document.getElementById("Invalid_Email_Div").style.visibility = "visible";
                setTimeout(function () {
                    document.getElementById("Invalid_Email_Div").style.visibility = 'hidden';
                  }, 2000);
            }
            // Disable the NExt Button here
        },
        complete: function(){
            $('#preloader').hide();
          }
    });
}

function verify_OTP(){
    var email = document.getElementById("Email").value;
    var OTP = $("#OTP").val();
    $('#preloader').show();
    $.ajax({
        url: VerifyOTPURL,
        type: "POST",
        headers: {
            "X-CSRFToken": csrfToken
            },
        data: {
            email: email,
            OTP: OTP
        },
        dataType: 'json',
        success: function(data){
            if(data.message == "Verified")
            {
                $(".step-3").removeClass("active");
                $(".step-4").addClass("active");
            }
            else if(data.message == "Invalid OTP")
            {
                document.getElementById("Invalid_OTP_Div").style.visibility = "visible";
                setTimeout(function () {
                    document.getElementById("Invalid_OTP_Div").style.visibility = 'hidden';
                  }, 2000);
                
            }
        },
        complete: function(){
            $('#preloader').hide();
          }
    });
}

function checkBothPasswords(){
    var password = document.getElementById("register-Password").value;
    var confirmPassword = document.getElementById("register-confirm-password").value;
    if(password == '' || confirmPassword == ''){
        document.getElementById("empty_Passwords").style.visibility = "visible";
        setTimeout(function () {
            document.getElementById("empty_Passwords").style.visibility = 'hidden';
          }, 2000);
          return false;
    }
    if(password != confirmPassword){
        document.getElementById("Password_Mismatch_Div").style.visibility = "visible";
        setTimeout(function () {
            document.getElementById("Password_Mismatch_Div").style.visibility = 'hidden';
          }, 2000);
    }
    else{
        $(".step-4").removeClass("active");
        $(".step-5").addClass("active");
    }
}

function username_availability(){
    var username = document.getElementById("username").value;
    $.ajax({
        url: UsernameAvailabilityURL,
        type: "POST",
        headers: {
            "X-CSRFToken": csrfToken
            },
        data: {
            username: username
        },
        dataType: 'json',
        success: function(data){
            console.log(data);
            if(data.message == "Available")
            {
                document.getElementById("username_availability_available").style.visibility = "visible";
                setTimeout(function () {
                    document.getElementById("username_availability_available").style.visibility = 'hidden';
                  }, 2000);
            }
            else if(data.message == "Not Available")
            {
                document.getElementById("username_availability_taken").style.visibility = "visible";
                setTimeout(function () {
                    document.getElementById("username_availability_taken").style.visibility = 'hidden';
                  }, 2000);
            }
        }
    });

}

var typingTimer;                //timer identifier
var doneTypingInterval = 500;  //time in ms, 5 seconds for example
var $input = $('#username');

//on keyup, start the countdown
$input.on('keyup', function () {
  clearTimeout(typingTimer);
  typingTimer = setTimeout(doneTyping, doneTypingInterval);
});

//on keydown, clear the countdown 
$input.on('keydown', function () {
  clearTimeout(typingTimer);
});

//user is "finished typing," do something
function doneTyping() {
    username_availability();
}

