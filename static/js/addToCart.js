window.onload = () => {
    let add_button = document.querySelector('#add_cart');
    add_button.addEventListener('click', (event) => {
        path_name = window.location.pathname;
        let product_id = path_name.slice(path_name.lastIndexOf('/')+1)
        console.log(product_id);
        let cart = window.localStorage.getItem('cart');
        if (cart) {
            cart = JSON.parse(cart);
            console.log(cart);
            if(cart[product_id]){
                cart[product_id] = cart[product_id]+1;
            }else{
                cart[product_id] = 1;
            }
            
        }else{
            cart={};
            cart[product_id] = 1;
        }
        localStorage.setItem('cart', JSON.stringify(cart));

        let main_content = document.querySelector('#main-content');
        let alert_div = document.createElement('div');
        alert_div.classList.add('alert', 'alert-success', 'font-weight-bold');
        alert_div.textContent = 'Product added to cart successfully';
        main_content.prepend(alert_div);
    })

}

