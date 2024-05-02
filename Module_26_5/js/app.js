const loadProducts = () => {
    fetch('https://fakestoreapi.com/products')
    .then(response => response.json())
    .then(data => displayProducts(data))
}
const displayProducts = (products) => {
    const parent = document.getElementById('all-product')
    products.forEach((product) => {
        const div = document.createElement('div');
        div.classList.add('product');
        div.innerHTML = `
        <h3>${product.title}</h3>
        <h4>${product.price}</h4>
        <h5>${product.category}</h5>
        <img id="" class="product-img" src="${product.image}" alt="">
        <button><a href="proDetails.html?proId=${product.id}">Details</a></button>
        `;
        parent.appendChild(div);
    })
}



const loadCategory = () => {
    fetch('https://fakestoreapi.com/products/categories')
    .then(response => response.json())
    .then(data => displayCategory(data))
}
const displayCategory = (categories) => {
    const parent = document.getElementById('all-category')
    categories.forEach((category) => {
        const div = document.createElement('div');
        div.classList.add('category');
        div.innerHTML = `
        <button onclick="filterProduct()" ><a href="index.html?catnm=${category}">${category}</a></button>
        `;
        parent.appendChild(div);
    })
}



const filterProduct = () => {
    const param = new URLSearchParams(window.location.search).get("catnm"); 
    fetch(`https://fakestoreapi.com/products/category/${param}`)
    .then(response => response.json())
    .then(data => displayCatProduct(data));
}

const displayCatProduct = (cat) => {
    const parent = document.getElementById('cat-pro');
    cat.forEach((meow) => {
        const div = document.createElement('div');
        // div.classList.add('product-cat');
        div.innerHTML = `
        <h1>${meow.category}</h1>
        <h3>${meow.title}</h3>
        <h4>${meow.price}</h4>
        <h5>${meow.category}</h5>
        <img id="" class="product-img" src="${meow.image}" alt="">

        `;
        parent.appendChild(div);
    })
}
filterProduct()
loadCategory(loadCategory)




loadProducts();