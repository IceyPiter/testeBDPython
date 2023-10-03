function setLogOut(){
    listUser = document.getElementById("elementsUser")
    alert("AAAAAAAAAAAAAAAAAAAAAaa")
    user = document.getElementById("Registrar")
    teste = document.getElementById("Registrar").value
    alert("AAAAAAAAAAAAAAAAAAAAAaa")
    alert(teste)
    if(user == "Registrar-se"){
        return
    }else{
        user.setAttribute("href", "{% url 'mandar_msg' %}")
        let logOut = document.createElement("li");
        let logOut2 = document.createElement("a");
        logOut.appendChild(logOut2)
        logOut2.innerHTML = "LogOut";
        listUser.appendChild(logOut);
        logOut2.setAttribute("class", "ms-2")
        logOut2.setAttribute("href", `{% url 'deslogar<${user}>' %}`)
    }
}
