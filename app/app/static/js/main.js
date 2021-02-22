$(document).ready(() => {

    let product_api_url = `${location.origin}/api/get-products/`
    let statistics_api_url = `${location.origin}/api/statistics/`
    let homePageUrl = window.location.protocol + "//" + window.location.host + "/"

    let day_visits_class = $('.day-visits');
    let day_hits_class = $('.day-hits');
    let daily_new_product_class = $('.daily-new-product');
    let products = $('.products-row');


    // Getting query params
    $.urlParam = function (name) {
        var results = new RegExp('[\?&]' + name + '=([^&#]*)')
                          .exec(window.location.search);
    
        return (results !== null) ? results[1] || 0 : false;
    }
    
    

    $("#searchProductForm").on('submit', function(event) {
        event.preventDefault();
        let keyword = $("#keywordInput").val();
        let city = $("#citySelect").val();
        let category = $.urlParam('category');

        if (city == "0"){
            city = "none"
        }
        if (category){
            window.location.replace(`${homePageUrl}elanlar/?keyword=${keyword}&city_id=${city}&category=${category}`)
        }else{
            window.location.replace(`${homePageUrl}elanlar/?keyword=${keyword}&city_id=${city}`)
        }
        
    })

    if ($.urlParam('user_id')){
        product_api_url = `${product_api_url}?user_id=${$.urlParam('user_id')}`
    }
    if ($.urlParam('category')){
        product_api_url = `${product_api_url}?category=${$.urlParam('category')}`
    }

    if ($.urlParam('keyword') && $.urlParam('city_id')){
        if ($.urlParam('category')){
            product_api_url = `${product_api_url}?keyword=${$.urlParam('keyword')}&city_id=${$.urlParam('city_id')}&category=${$.urlParam('category')}`
        }else{
            product_api_url = `${product_api_url}?keyword=${$.urlParam('keyword')}&city_id=${$.urlParam('city_id')}`
        }
    }
    
    console.log($.urlParam('city_id'))
    console.log(product_api_url)


    fetch(product_api_url)
        .then((response) => response.json())
        .then((data) => Product(data))
    
    fetch(statistics_api_url)
        .then((response) => response.json())
        .then((data) => Statistics(data))
        
    
    function Product(data){
        for(value in data){
             products.append(`
            <div class="products-i">
                <a href="${location.origin}/elanlar/${data[value]['slug']}" class="products-link mb-2">
                    <div class="card">
                        <div class="products-top">
                            <img class="card-img-top" src="${location.origin}${data[value]['image_url']}" alt="Card image cap">
                            <div class="products-price-container">
                                <div class="products-price">
                                    <span class="price-val">${ data[value]['price']} AZN</span>
                                </div>
                            </div>
                        </div>
                        <div class="products-name">${ data[value]['title'] }</div>
                        <div class="products-created">${ data[value]['city'] }, bugün, 18:21</div>
                    </div>
                </a>
            </div>
            `)
        }
    }


    function Statistics(data) {
        let new_user_count = data.daily_new_user.split('')
        let daily_product_views = data.daily_product_views.split('')
        let daily_added_new_products = data.daily_added_new_products.split('')

        function add_new_user_count_to_header(new_user_count){
            for(digit in new_user_count){
                day_visits_class.append(
                    `<span>${new_user_count[digit]}</span>`
                )
            }
        }
    
        function add_daily_product_view_to_header(daily_product_views){
            for(digit in daily_product_views){
                day_hits_class.append(
                    `<span>${daily_product_views[digit]}</span>`
                )
            }
        }
    
        function add_daily_new_product_count_to_header(daily_added_new_products){
            for(digit in daily_added_new_products){
                daily_new_product_class.append(
                    `<span>${daily_added_new_products[digit]}</span>`
                )
            }
        }

        add_new_user_count_to_header(new_user_count)
        add_daily_product_view_to_header(daily_product_views)
        add_daily_new_product_count_to_header(daily_added_new_products)
    }



    $("#phone_number").inputmask({"mask": "(999) 999-99-99"});

})