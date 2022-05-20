// import {getCart} from './getCart.js';

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
    main_card_body.innerHTML = ''
    let total_price = 0
    for (const id in cart) {
        let product = await (await fetch(`/product/api/${id}`)).json()
        total_price += Number(product.price);
        let product_card = document.createElement('div');
        let product_card_row = document.createElement('div');
        let card_body = document.createElement('div');
        let card_body_col = document.createElement('div');
        let card_img = document.createElement('img');
        let card_img_col = document.createElement('div');
        let card_text = document.createElement('div');
        let card_header = document.createElement('div');
        let card_remove_button = document.createElement('button');
        let product_quantity = document.createElement('p');

        product_card.classList.add('card', 'shadow');

        card_body.classList.add('card-body');
        
        card_body_col.classList.add('col-12' ,'col-md-7');

        card_img.src = `/static/images/${product.image}`;
        card_img.classList.add('h-100', 'w-100');

        card_img_col.classList.add('col-12', 'col-md-5');

        card_text.classList.add('card-text')
        card_text.textContent = product.description;

        card_header.classList.add('card-header');
        card_header.textContent = product.name.toUpperCase();

        product_card_row.classList.add('row');

        
        product_quantity.innerHTML = `<strong>Quantity: ${cart[id]}</strong>`;


        card_remove_button.classList.add('btn', 'btn-danger','remove-btn');
        card_remove_button.textContent = 'Remove';
        card_remove_button.id = id;
        card_remove_button.addEventListener('click', (event)=>{
            let cart = window.localStorage.getItem('cart');
            if(cart){
                cart = JSON.parse(cart);
                delete cart[event.target.id];
                window.localStorage.setItem('cart', JSON.stringify(cart));
                location.reload();
            }
        });

        card_img_col.append(card_img);

        card_body_col.append(card_body);

        card_body.append(card_text, product_quantity, card_remove_button);

        product_card_row.append(card_img_col, card_body_col);

        product_card.append(card_header, product_card_row);

        main_card_body.append(product_card, document.createElement('hr'));

        let id_input = document.createElement('input');
        id_input.type='hidden';
        id_input.name='id';
        id_input.value=`${id},${cart[id]}`;
        console.log(id_input);
        document.querySelector('#checkout-form').append(id_input);
    }

    let total_price_element = document.createElement('h3');
    total_price_element.textContent = `Total Price: EGP ${total_price}`;
    total_price_element.classList.add('text-center');
    main_card_body.appendChild(total_price_element);

}


