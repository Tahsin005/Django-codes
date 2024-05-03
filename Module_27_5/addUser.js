// script.js
document.getElementById('registration-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const firstname = document.getElementById('firstname').value;
    const lastname = document.getElementById('lastname').value;
    const city = document.getElementById('city').value;
    const street = document.getElementById('street').value;
    const number = document.getElementById('number').value;
    const zipcode = document.getElementById('zipcode').value;
    const lat = document.getElementById('lat').value;
    const long = document.getElementById('long').value;
    const phone = document.getElementById('phone').value;
    console.log(username, email, password, firstname, lastname, city, street, number, zipcode, lat, long, phone);

    try {
        const response = await fetch('https://fakestoreapi.com/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email: email,
                username: username,
                password: password,
                name:{
                    firstname: firstname,
                    lastname: lastname,
                },
                address:{
                    city: city,
                    street: street,
                    number: number,
                    zipcode: zipcode,
                    geolocation:{
                        lat: lat,
                        long: long,
                    }
                },
                phone: phone,
            }),
        });

        const data = await response.json();
        console.log('User created:', data);
    } catch (error) {
        console.error('Error creating user:', error);
    }
});
