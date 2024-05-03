const handleRegistration = (event) => {
    event.preventDefault();
    const username = getValue("username");
    const first_name = getValue("first_name");
    const last_name = getValue("last_name");
    const email = getValue("email");
    const password = getValue("password");
    const confirm_password = getValue("confirm_password");

    const info = {username, first_name, last_name, email, password, confirm_password};
    if (password === confirm_password) {
        document.getElementById('error').innerText = "";
        if (/^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/.test(password)) {
            console.log(info);

            fetch("https://testing-8az5.onrender.com/patient/register/", {
                method: "POST",
                headers: {
                    "content-type": "application/json",
                },
                body: JSON.stringify(info),
            })
            .then(response => response.json())
            .then(data =>  {
                console.log(data)
             });

        } else {
            document.getElementById('error').innerText = "Passwords must contain minimum eight characters, at least one letter, one number and one special character";
        }
    } else {
        document.getElementById('error').innerText = "Passwords do not match";
    }
};

const getValue = (id) => {
    const value = document.getElementById(id).value;
    return value;
};

const handleLogin = (event) => {
    event.preventDefault();
    const username = getValue("login-username");
    const password = getValue("login-password");

    fetch("https://testing-8az5.onrender.com/patient/login/",{
        method: "POST",
        headers: {
            "content-type": "application/json",
        },
        body: JSON.stringify({username, password}),
    })
    .then(response => response.json())
    .then(data =>  {
        console.log(data);
        
        if (data.token && data.user_id) {
            localStorage.setItem("token", data.token);
            localStorage.setItem("user_id", data.user_id);
            window.location.href = "index.html";
        }
 
    });

}