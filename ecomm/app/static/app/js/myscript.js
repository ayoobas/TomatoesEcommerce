$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 2,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 4,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 6,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this.parentNode.children[2] 
    console.log("pid = ", id)
    console.log("eml = ", eml)
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:id
        },
        success:function(data){
           console.log("data = ", data);
           eml.innerText = data.quantity
           document.getElementById("amount").innerText = data.amount 
           document.getElementById("totalamount").innerText = data.totalamount
        }
    })
})

$('.minus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this.parentNode.children[2] 
    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            prod_id:id
        },
        success:function(data){
            eml.innerText=data.quantity 
            document.getElementById("amount").innerText=data.amount 
            document.getElementById("totalamount").innerText=data.totalamount
        }
    })
})


$('.remove-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this
    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
            prod_id:id
        },
        success:function(data){
            document.getElementById("eml").innerText= "Cart " +data.quantity 
            document.getElementById("amount").innerText=data.amount 
            document.getElementById("totalamount").innerText=data.totalamount
            eml.parentNode.parentNode.parentNode.parentNode.remove() 
        }
    })
})



$('.remove-wishlist').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this
    $.ajax({
        type:"GET",
        url:"/removewish",
        data:{
            prod_id:id
        },
        success:function(data){
            document.getElementById("eml").innerText= "Cart " +data.quantity 
            document.getElementById("amount").innerText=data.amount 
            document.getElementById("totalamount").innerText=data.totalamount
            eml.parentNode.parentNode.parentNode.parentNode.remove() 
        }
    })
})






$('.plus-wishlist').click(function(){
    var id=$(this).attr("pid").toString();
    $.ajax({
        type:"GET",
        url:"/pluswishlist",
        data:{
            prod_id:id
        },
        success:function(data){
           /* alert(data.message)*/
            document.getElementById("wish").innerText= "Wishlist " +data.quantity 
            window.location.href = `http://localhost:8000/product-detail/${id}`
          
        }
    })
})


$('.minus-wishlist').click(function(){
    var id=$(this).attr("pid").toString();
    $.ajax({
        type:"GET",
        url:"/minuswishlist",
        data:{
            prod_id:id
        },
        success:function(data){
            /*alert(data.message)*/
            document.getElementById("wish").innerText= "Wishlist " +data.quantity 
            window.location.href = `http://localhost:8000/product-detail/${id}`
        }
    })
})


const togglePassword = document.querySelector('#togglePassword');
const password = document.querySelector('#password');
togglePassword.addEventListener('click', (e) => {
    const type = password.getAttribute('type') === 'password' ? 'text': 'password';
    password.setAttribute('type', type);
    e.target.classList.toggle('bi-eye');
})

const ctogglePassword = document.querySelector('#ctogglePassword');
const cpassword = document.querySelector('#cpassword');
ctogglePassword.addEventListener('click', (e) => {
    const type = cpassword.getAttribute('type') === 'password' ? 'text': 'password';
    cpassword.setAttribute('type', type);
    e.target.classList.toggle('bi-eye');
})