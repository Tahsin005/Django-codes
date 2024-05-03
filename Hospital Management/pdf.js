const handlePdf = () => {
    const doctor_id = new URLSearchParams(window.location.search).get("doctorId");
    const user_id = localStorage.getItem('user_id');
    fetch(`https://testing-8az5.onrender.com/doctor/list/${doctor_id}`)
    .then(response => response.json())
    .then(data =>  {
        fetch(`https://testing-8az5.onrender.com/users/${user_id}`)
        .then(response => response.json())
        .then(pddata => {
            const newData = [data, pddata];
            const parent = document.getElementById('pdf-container');
            const div = document.createElement('div');

            div.innerHTML = `
                <div class="pd d-flex justify-content-around align-items-center">
                <div class="patient doctor">
                    <h1>${newData[1].username}</h1>
                    <h1>${newData[1].first_name} ${newData[1].last_name}</h1>
                    <h1>${newData[1].email}</h1>
                    <h1>Hwllo</h1>
                </div>
                <div class="doctor">
                    <h2 class="doc-name">Matt labalnc</h2>
                    <h3>Designation</h3>
                    <h5>Specialiszation: </h5>
                </div>
            </div>
            `;
            parent.appendChild(div);
            downloadPdf();
            
            console.log(newData);
        });

    });

    
}

const downloadPdf = () =>{
    const element = document.getElementById('pdf-container');
    
    // Options for PDF creation
    const opt = {
        margin:       10,
        filename:     'smartcare.pdf',
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  { scale: 2 },
        jsPDF:        { unit: 'in', format: 'a4', orientation: 'portrait' }
    };

    // Create PDF from HTML element
    html2pdf(element, opt);
}



handlePdf();

