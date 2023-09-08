// Forget pass window

function forgotPassWindow()
{
    document.getElementById("forgotpasscont").classList.toggle("window");
    
}

// LOGIN TO SIGN UP AND VICE VERSA

function login_signin()
{
    document.getElementById("signincont").classList.toggle("logsign");   
    document.getElementById("logincont").classList.toggle("logsign");

    document.getElementById("loginbgcont").classList.toggle("logsign");
    document.getElementById("signinbgcont").classList.toggle("logsign");  
}
