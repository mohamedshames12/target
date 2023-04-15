const btnMenu = document.getElementById("menu");
const navbar = document.querySelector(".navbar");
const close = document.querySelector("#close");
btnMenu.addEventListener("click", () => {
    navbar.classList.add("active");
    setTimeout(() => { 
        close.style.display = "block";
     }, 300)
})

close.addEventListener("click", () => {
    navbar.classList.remove("active");
    setTimeout(() => { 
        close.style.display = "none";
     }, 250)
})


