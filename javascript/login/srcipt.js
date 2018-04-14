window.onload = function () {
    var btn = document.getElementById("btn");
    var objUsername = document.getElementById("username");
    var objPassword = document.getElementById("password");


    btn.onclick = function () {
        btn.style.display = "none";
        login.style.display = "block";
    };

    this.onsubmit = function(){
        var username = objUsername.value;
        var password = objPassword.value;
        var regexUsername = new RegExp("\\w[-\\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\\.)+[A-Za-z]{2,14}");
        if(regexUsername.test(username)){
            alert("right");
        }
        else{
            alert("please input a right email!")
        }
        var regexPassword = new RegExp("[\\w*]{6,10}");
        if(regexPassword.test(password)){
            alert("Right");
        }else{
            alert("please input 6-10 characters");
        }
    }

}