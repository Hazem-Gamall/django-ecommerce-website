window.onload = () => {
    let cart = getCart()
    renderCardsFromCart(cart);
    
    let checkout_form = document.querySelector('#checkout-form');
    checkout_form.addEventListener('submit', (event)=>{
        window.localStorage.clear();
        console.log(event);
    })
}



let renderCardsFromCart = async (cart) => {
    let main_card_body = document.querySelector('#main-card-body');
    currency_formatter = new Intl.NumberFormat('en-US');
    main_card_body.innerHTML = ''
    let total_price = 0
    for (const id in cart) {
        let product = await (await fetch(`/product/api/${id}`)).json()

        total_price += Number(product.price * cart[id]);


        let product_card = document.createElement('div');
        product_card.innerHTML = 
        `<div class="card shadow">
            <div class="card-header">
                ${product.name.toUpperCase()}
            </div>
            <div class="row">
                <div class="col-12 col-md-5">
                    <img class="h-100 w-100" src="/static/images/${product.image}">
                    
                </div>
                <div class="col-12 col-md-7">
                    <div class="card-body">
                        <div class="card-text">
                            ${product.description}
                        </div>
                        <p>
                            <strong>Quantity: ${cart[id]}</strong>
                        </p>
                        <button class="btn btn-danger remove-btn" id=${id}>
                            Remove
                        </button>
                        <p class="mt-3">
                            <strong>Price: ${currency_formatter.format(product.price)}</strong>
                        </p>
                    </div>

                </div>
            </div>
        </div>`

        main_card_body.append(product_card, document.createElement('hr'));
       

        card_remove_button = product_card.querySelector(`.btn`)
        console.log(card_remove_button)
        card_remove_button.addEventListener('click', (event)=>{
            let cart = window.localStorage.getItem('cart');
            if(cart){
                cart = JSON.parse(cart);
                delete cart[event.target.id];
                window.localStorage.setItem('cart', JSON.stringify(cart));
                location.reload();
            }
        });

       
        let id_input = document.createElement('input');
        id_input.type='hidden';
        id_input.name='id';
        id_input.value=`${id},${cart[id]}`;
        console.log(id_input);
        document.querySelector('#checkout-form').append(id_input);
    }

    let total_price_element = document.createElement('div');
    total_price_element.innerHTML = 
    `
    <h3 class="text-center">
        <strong>Total Price: EGP ${currency_formatter.format(total_price)}
    </h3>
    `;
    // total_price_element.textContent = `Total Price: EGP ${currency_formatter.format(total_price)}`;
    // total_price_element.classList.add('text-center');
    main_card_body.append(total_price_element.firstElementChild);

}


