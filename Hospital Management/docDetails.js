// alert('From doc')

const getparams = () => {
    const param = new URLSearchParams(window.location.search).get("doctorId");

    loadTime(param);

    fetch(`https://testing-8az5.onrender.com/doctor/list/${param}`)
    .then(response => response.json())
    .then(data =>  displayDetails(data));
    
    
    fetch(`https://testing-8az5.onrender.com/doctor/review/?doctor_id=${param}`)
    .then(response => response.json())
    .then(data =>  displayReview(data));

    
}

const loadTime = (id) => {
    fetch(`https://testing-8az5.onrender.com/doctor/availabletime/?doctor_id=${id}`)
    .then(response => response.json())
    .then(data =>  {
        console.log(data);
        data.forEach((item) => {
            const parent = document.getElementById('time-container');
            const option = document.createElement('option');
            option.value = item.id;
            option.innerText = item.name;
            parent.appendChild(option);
        })
    });

}


const handleAppointment = () => {
    const status = document.getElementsByName("status");

    const selected = Array.from(status).find((button) => button.checked) ;
    
    const symptom = document.getElementById("symptom").value;
    const time = document.getElementById("time-container");
    const selectedTime = time.options[time.selectedIndex];


    // console.log(selected.value);
    // console.log(symptom);
    // console.log(selectedTime.value);
    const param = new URLSearchParams(window.location.search).get("doctorId");
    const patient_id = localStorage.getItem('patient_id');

    const info = {
        appointment_type: selected.value,
        appointment_status: "Pending",
        time: selectedTime.value,
        symptom: symptom,
        cancel: false,
        patient: patient_id,
        doctor: param,
    }
    console.log(info);

    fetch("https://testing-8az5.onrender.com/appointment/", {
        method: "POST",
        headers: {
            "content-type": "application/json",
        },
        body: JSON.stringify(info),
    })
    .then(response => response.json())
    .then(data =>  {
        console.log(data);
        window.location.href = `pdf.html?doctorId=${param}`
    })

}


const displayReview = (reviews) => {
    reviews.forEach((review) => {
        const parent = document.getElementById('doc-details-review');
        const div = document.createElement('div');
        div.classList.add('review-card');
        div.innerHTML = `
            <img src="./images/girl.png" alt="">
            <h4>${review.reviewer}</h4>
            <h5>${review.doctor}</h5>
            <p>${review.body.slice(0, 100)}</p>
            <p>${review.created_on}</p>
            <h6>${review.rating}</h6>
        `;
        // div.innerText = "this is doctor reiveew"
        parent.appendChild(div);
    })
}
const displayDetails = (doctor) => {
    // console.log(doctor);
    const parent = document.getElementById('doc-details');
    const div = document.createElement('div');
    div.classList.add('doc-details-container');
    div.innerHTML = `
        <div class="doctor-img">
        <img src="${doctor.image}" alt="">
    </div>
    <div class="doc-info">
        <h1>${doctor.full_name}</h1>
        <h3>${doctor.designation}</h3>
        <h6>
        ${doctor?.specialization?.map((item) => {
            return `<button class="doc-detail-btn">${item}</button>`;
        })}
        </h6>
        <p class="w-50">Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel nihil, perferendis quo odio explicabo voluptate?</p>

        <h4>Fees : ${doctor.fee} BDT</h4>
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
            Take Appointment
        </button>
    </div>
    
    `;
    parent.appendChild(div);
}


const loadPatientId = () => {
    const user_id = localStorage.getItem('user_id');
    fetch(`https://testing-8az5.onrender.com/patient/list/?user_id=${user_id}`)
    .then(response => response.json())
    .then(data => {
        localStorage.setItem('patient_id', data[0].id);
    });
}



// console.log('from now');





loadPatientId();
getparams();