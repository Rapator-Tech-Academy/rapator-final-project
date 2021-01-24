$(document).ready(() => {
    let api_url = `${location.origin}/api/get-products/`
    let products = $('.products-list')

    fetch(api_url)
        .then((response) => response.json())
        .then((data) => Prodcut(data))
    
    function Prodcut(data){
        for(value in data){
            products.append(`
            <div class="products-i">
                <a href="#" class="products-link mb-2">
                    <div class="card">
                        <img class="card-img-top" src="${location.origin}${data[value]['image_url']}" alt="Card image cap">
                        <div class="products-price-container">
                            <div class="products-price">
                                <span class="price-val">${ data[value]['price']} AZN </span>
                            </div>
                        </div>
                        <div class="card-body">
                        <h5 class="card-title products-name">${ data[value]['title'] } </h5>
                        <p class="card-text">${ data[value]['city'] }, bugün, 18:21</p>
                        </div>
                    </div>
                </a>
            </div>`)
        }
    }
})