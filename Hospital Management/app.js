const loadServices = () => {
    fetch('https://testing-8az5.onrender.com/services/')
    .then(response => response.json())
    .then(data => displayService(data))
    .catch(error => console.log(error))
};

const displayService = (services) => {
    const parent = document.getElementById('service-container');
    for (const service of services) {
        const li = document.createElement('li');
        li.innerHTML = `
        <div class="card shadow h-100">
            <div class="ratio ratio-16x9">
                <img src="${service.image}" class="card-img-top" loading="lazy" alt="...">
            </div>
            <div class="card-body  p-3 p-xl-5">
                <h3 class="card-title h5">${service.name}</h3>
                <p class="card-text">${service.description.slice(0, 100)}</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
        </div>
        
        `;
        parent.appendChild(li);
    }
}



const loadDoctors = (search) => {
    document.getElementById("doctors").innerHTML = "";
    document.getElementById("spinner").style.display = "block";
    console.log(search);
    fetch(`https://testing-8az5.onrender.com/doctor/list/?search=${search ? search : ""}`)
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (data.results.length > 0) {
            displayDoctors(data?.results)
            document.getElementById("nodata").style.display = "none";
            document.getElementById("spinner").style.display = "none";
            
        } 
        else {
            document.getElementById("doctors").innerHTML = "";
            document.getElementById("nodata").style.display = "block";
            document.getElementById("spinner").style.display = "none";
            
        }
    })
};

const displayDoctors = (doctors) => {
    doctors?.forEach((doctor) => {
        const parent = document.getElementById("doctors");
        const div = document.createElement("div");
        div.classList.add("doc-card");
        div.innerHTML = `
            <img class="doc-img" src="${doctor?.image}" alt="">
            <h4>${doctor?.full_name}</h4>
            <h6>${doctor?.designation}</h6>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Modi, facere!</p>
            <p>
            ${doctor?.specialization?.map((item) => {
                return `<button>${item}</button>`;
            })}
            </p>
            <button type="button" class="btn btn-secondary"> <a target="_blank"  href="docDetails.html?doctorId=${doctor.id}">Details</a> </ button>
        `;

        parent.appendChild(div);
    });
}




const loadDesignation = () => {
    fetch('https://testing-8az5.onrender.com/doctor/designation/')
    .then(response => response.json())
    .then(data => {
        data.forEach((item) => {
            const parent = document.getElementById('drop-deg');
            const li = document.createElement('li');
            li.classList.add('dropdown-item');
            li.innerText = item.name;
            parent.appendChild(li);
        })
    });
}
const loadSpecialization = () => {
    fetch('https://testing-8az5.onrender.com/doctor/specialization/')
    .then(response => response.json())
    .then(data => {
        data.forEach((item) => {
            const parent = document.getElementById('drop-spe');
            const li = document.createElement('li');
            li.classList.add('dropdown-item');
            li.innerHTML = `
                <li onclick="loadDoctors('${item.name}')">${item.name}</li>
            
            `;
            parent.appendChild(li);
        })
    });
}




const handleSearch = () => {
    const value = document.getElementById('search').value;
    // https://testing-8az5.onrender.com/doctor/list/?search=trinity
    loadDoctors(value);
    document.getElementById('search').value = "";
}


const loadReview = () => {
    fetch("https://testing-8az5.onrender.com/doctor/review/")
    .then(response => response.json())
    .then(data => displayReview(data))
}

const displayReview = (reviews) => {
    reviews.forEach((review) => {
        const parent = document.getElementById('review-container');
        const div = document.createElement('div');
        div.classList.add('review-card');
        div.innerHTML = `
            <img src="./images/girl.png" alt="">
            <h4>${review.reviewer}</h4>
            <h5>${review.doctor}</h5>
            <p>${review.body.slice(0, 100)}</p>
            <p>${review.created}</p>
            <h6>${review.rating}</h6>
        `;
        parent.appendChild(div);
    })
}
loadServices();
loadDoctors();
loadSpecialization();
loadDesignation();
loadReview()