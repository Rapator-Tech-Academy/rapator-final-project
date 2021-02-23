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

    $("#editProduct").on('submit', function(event) {
        event.preventDefault();
        edit_product();
    })

    let imageProduct;

    $('#ImageBrowse').on('change', function () {
        fileReader = new FileReader();
        fileReader.onload = function () {
          var data = fileReader.result;  // data <-- in this var you have the file data in Base64 format
        };
        fileReader.readAsDataURL($('#ImageBrowse').prop('files')[0]);

        imageProduct = fileReader
    });

    
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
                image : imageProduct,
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
    function edit_product(){
        $.ajax({
            url : window.location.pathname,
            type : "POST",
            data : { 
                csrfmiddlewaretoken: csrftoken,
				title : $('input[name ="title"]').val(),
				price : $('input[name="price"]').val(),
				description : $('textarea[name ="description"]').val(),
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