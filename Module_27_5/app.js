const handleUsers = () => {
    fetch('https://fakestoreapi.com/users')
    .then(res=>res.json())
    .then(data=>{
        displayUsers(data);
    })
    
}

const displayUsers = (users) => {
    const parent = document.getElementById('all-users');
    users.forEach((user) => {
        const div = document.createElement('div');
        div.classList.add('user')
        div.innerHTML = `
            <h1>${user.username}</h1>
            <p>${user.email}</p>
            
            <button><a target="_blank" href="userDetails.html?user_id=${user.id}">Details</a></button>
        `;
        parent.appendChild(div);
    })
}




const handleUserDetails = () => {
    const param = new URLSearchParams(window.location.search).get("user_id") || 1;
    fetch(`https://fakestoreapi.com/users/${param}`)
    .then(res=>res.json())
    .then(data=>displayUserDetail(data))
}

const displayUserDetail = (user) => {
    const parent = document.getElementById('user-detail-container');
    const div = document.createElement('div');
    div.classList.add("user");
    div.innerHTML = `
        <p>${user.name.firstname}</p>
        <p>${user.name.lastname}</p>

        <div class="address">
            <p>${user.address.city}</p>
            <p>${user.address.street}</p>
            <p>${user.address.number}</p>
            <p>${user.address.zipcode}</p>
            <p>${user.address.geolocation.lat}</p>
            <p>${user.address.geolocation.long}</p>
        </div>
        <p>${user.phone}</p>
    `;
    parent.appendChild(div);
}








handleUserDetails();





handleUsers();