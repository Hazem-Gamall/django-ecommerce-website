
let search_form = document.querySelector('#search_form');
search_form.addEventListener('submit', (event) => {

    query = document.querySelector('#search-bar').value;
    category = document.querySelector('#dropDownMenuButton').textContent;
    window.location.href = `/testApp/search/${category}/${query}`;
    event.preventDefault();
})
console.log(search_form);