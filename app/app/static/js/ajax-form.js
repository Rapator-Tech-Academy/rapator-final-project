$(document).ready(function(){

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');
    
    
    $("#createProduct").on('submit', function(event) {
        event.preventDefault();
        create_product();
    })
    
    function create_product(){
        $.ajax({
            url : window.location.pathname, // the endpoint
            type : "POST", // http method
            data : { 
                csrfmiddlewaretoken: csrftoken,
                image: $("#formFileSm").val()
            }, // data sent with the post request
        
            // handle a successful response
            success : function(data) {
                console.log("success")
            },
        
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                console.log(err)
            }
        });
    };

});