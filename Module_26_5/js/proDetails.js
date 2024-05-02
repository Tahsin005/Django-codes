const loadProduct = () => {
    const param = new URLSearchParams(window.location.search).get("proId"); 

    fetch(`https://fakestoreapi.com/products/${param}`)
    .then(response => response.json())
    .then(data => displayProduct(data));
}

const displayProduct = (product) => {
    const parent = document.getElementById('spe-product')

    const div = document.createElement('div');
    div.classList.add('product-card');
    div.innerHTML = `
        <img class="product-img" src="${product.image}" alt="">
        <h4>${product.title}</h4>
        <h5>$${product.price}</h5>
        <p>${product.description}</p>
        <p>${product.rating.rate}</p>
        <p>${product.rating.count}</p>
    `;
    parent.appendChild(div);
}
loadProduct();