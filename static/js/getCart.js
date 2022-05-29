let getCart = () =>{
    let cart = window.localStorage.getItem('cart');
    if (!cart) {
        return null
    }
    let cart_obj = JSON.parse(cart);
    console.log(cart_obj);
    return cart_obj;
}
