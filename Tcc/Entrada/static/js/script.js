function setLogOut(){
    listUser = document.getElementById("elementsUser")
    user = document.getElementById("Registrar-se")
    if(user == "Registrar-se"){
        continue
    }else{
        let logOut = document.createElement("li");
        let logOut2 = document.createElement("a");
        logOut.appendChild(logOut2)
        logOut2.innerHTML = "LogOut";
        listUser.appendChild(logOut);
        logOut2.setAttribute("class", "ms-2")
        logOut2.setAttribute("href", `{% url 'deslogar<${user}>' %}`)
    }
}
