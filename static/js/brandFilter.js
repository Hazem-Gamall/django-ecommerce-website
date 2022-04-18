let form = document.querySelector('#filters_form');

form.addEventListener('submit', (event)=>{
    event.preventDefault();
    url_params = new URLSearchParams();
    checked_brands = Array.from(document.getElementsByClassName('brand-filter')).filter((brand)=>brand.checked);
    checked_brands.forEach((brand) => url_params.append('brand',brand.value));

    price_filter = Array.from(document.getElementsByClassName('price-filter')).filter(radio => radio.checked)[0].value
    url_params.append('price-filter', price_filter);
    window.location.search = window.location.search.replace(/(&?(brand|price-filter).+(&|$)|$)+/,`&${url_params.toString()}`);
    // console.log(window.location.search.replace(/(brand.+(&|$)|$)+/,`&${url_params.toString()}`));
})