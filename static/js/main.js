document.addEventListener('DOMContentLoaded', function () {
    console.log("DOM loaded")
});

let menueLinks = document.querySelectorAll("#menu").forEach( item => {
    item.addEventListener("click", redirect)
})


async function redirect(event) {
    event.preventDefault();
    let className = event.target.className
    if (className === "main") {
        window.location.href = '/';
    } else{
        window.location.href = '/' + className;
    }
}

