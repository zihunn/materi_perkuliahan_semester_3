

function windowScroll() {
    const navbar = document.getElementById("navbar");
    if (
        document.body.scrollTop >= 50 ||
        document.documentElement.scrollTop >= 50
    ) {
        navbar.classList.add("nav-sticky");
    } else {
        navbar.classList.remove("nav-sticky");
    }
}

window.addEventListener('scroll', (ev) => {
    ev.preventDefault();
    windowScroll();
});



var scroll = new SmoothScroll('#navbar-navlist a', {
    speed: 500,
    offset: 70
});



var spy = new Gumshoe('#navbar-navlist a', {
    
    navClass: 'active', 
    contentClass: 'active', 
    offset: 80
});


function fadeIn() {
    var fade = document.getElementById("error-msg");
    var opacity = 0;
    var intervalID = setInterval(function () {
        if (opacity < 1) {
            opacity = opacity + 0.5;
            fade.style.opacity = opacity;
        } else {
            clearInterval(intervalID);
        }
    }, 200);
}



window.onload = function preloader() {
    setTimeout(() => {
        document.getElementById('preloader').style.visibility = 'hidden';
        document.getElementById('preloader').style.opacity = '0';
        window.Unicons.refresh();
    }, 1000);
};


feather.replace();


var bodyElem = document.documentElement;


if (bodyElem.hasAttribute("data-bs-theme") && bodyElem.getAttribute("data-bs-theme") == "light") {
    sessionStorage.setItem("data-layout-mode", "light");
} else if (bodyElem.getAttribute("data-bs-theme") == "dark") {
    sessionStorage.setItem("data-layout-mode", "dark");
}

if (sessionStorage.getItem("data-layout-mode") == null) {
    bodyElem.setAttribute("data-bs-theme", "light");
} else if (sessionStorage.getItem("data-layout-mode")) {
    bodyElem.setAttribute("data-bs-theme", sessionStorage.getItem("data-layout-mode"));
}

var lightDarkBtn = document.getElementById('light-dark-mode');
if (lightDarkBtn) {
    lightDarkBtn.addEventListener('click', function (event) {
        if (bodyElem.hasAttribute("data-bs-theme") && bodyElem.getAttribute("data-bs-theme") == "dark") {
            bodyElem.setAttribute('data-bs-theme', 'light');
            sessionStorage.setItem("data-layout-mode", "light");
        } else {
            bodyElem.setAttribute('data-bs-theme', 'dark');
            sessionStorage.setItem("data-layout-mode", "dark");
        }
    });
} 











