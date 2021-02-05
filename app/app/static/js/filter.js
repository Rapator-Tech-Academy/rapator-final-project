$(document).ready(() => {
    let api_url = `${location.origin}/api/get-products/`
    let body = $('.body')

    fetch(api_url)
        .then((response) => response.json())
        .then((data) => Prodcut(data))
    
    function Prodcut(data){
        for(value in data){
            body.append(`<div class="card" style="width: 18rem; margin-top: 2rem; margin-left:2rem">
            <div class="card-body">
              <h5 class="card-title"> ${ data[value]['title'] } </h5>
              <p class="card-text">${data[value]['description']}</p>
              <a href="${data[value]['slug']}" class="btn btn-primary">Go somewhere</a>
            </div>
          </div>`)
        }
    }
}
)