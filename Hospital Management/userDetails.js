const loadUserDetails = () => {
    const user_id = localStorage.getItem('user_id');
    fetch(`https://testing-8az5.onrender.com/users/${user_id}`)
     .then(response => response.json())
     .then(data => {
        const parent = document.getElementById('user-details-container');
        const div = document.createElement('div');
        div.classList.add("user-all");

        div.innerHTML = `
        <div class="user-img">
            <img src="./images/man-1.jpg" alt="">
        </div>
        <div class="user-info">
            <h1>${data.username}</h1>
            <h3>${data.email}</h3>
            <h3>${data.first_name} </h3>

        </div>
        
        `;
        parent.appendChild(div);
     });
}

loadUserDetails();