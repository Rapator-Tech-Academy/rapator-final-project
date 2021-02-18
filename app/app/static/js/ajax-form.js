$(document).ready(function(){

    let valueOfDelivery;
    let valueOfIsNew;

    let alertMessageHTML = `
        <div class="alert alert-warning" role="alert" id="alertMessage" style="margin-top:1.3rem">
            Sizin elanınız yoxlanış üçün müvəffəqiyyətlə göndərildi. Qaydalara uyğun olduğu halda sizin mail hesabınıza bildiriş göndəriləcək.
        </div>
    `

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

    if ($('input[name ="is_new"]').is(':checked')) {
        valueOfIsNew = 'True'
    }else{
        valueOfIsNew = 'None'
    }

    if ($('input[name ="delivery"]').is(':checked')) {
        valueOfDelivery = 'True'
    }else{
        valueOfDelivery = 'None'
    }
    
    
    $("#createProduct").on('submit', function(event) {
        event.preventDefault();
        create_product();
    })
    
    function create_product(){
        $.ajax({
            url : window.location.pathname,
            type : "POST",
            data : { 
                csrfmiddlewaretoken: csrftoken,
				title : $('input[name ="title"]').val(),
				price : $('input[name="price"]').val(),
				description : $('textarea[name ="description"]').val(),
				city : $('select[name ="city"]').val(),
                category : $('select[name ="category"]').val(),
                user_email : $('input[name ="email"]').val(),
                is_new : valueOfIsNew,
                delivery : valueOfDelivery,
            },
        
            success : function(data) {
                console.log("success")
                $('.new-lot-form').prepend(alertMessageHTML);

                $('html, body').animate({
                    scrollTop: $("#alertMessage").offset().top
                }, 1000);

                setTimeout(() => window.location.reload(), 5000);
            },
        
            error : function(xhr,errmsg,err) {
                console.log(err)
            }
        });
    };

});