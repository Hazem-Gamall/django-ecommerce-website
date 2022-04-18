
let elements = document.getElementsByClassName('dropdown-item');
Array.from(elements).forEach((element) => {
    element.addEventListener('click', (event) => {
        let button = document.querySelector('#dropDownMenuButton');
        // alert(`Clicked ${event.target.innerText}!`);
        button.textContent = event.target.innerText;
    });
});