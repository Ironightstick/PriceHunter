function toggleMenu() {
    const menu = document.getElementById("menu");
    const overlay = document.getElementById("menuoverlay"); 

    const isActive = menu.classList.contains("active");

    if (isActive) {
        menu.classList.remove("active");
        overlay.classList.remove("active");
    } else {
        menu.classList.add("active");
        overlay.classList.add("active");
    }
}

function openSignInMenu() {
    document.getElementById("signinMenu").classList.add("active");
    document.getElementById("signinoverlay").classList.add("active"); 
}

function closeSignInMenu() {
    document.getElementById("signinMenu").classList.remove("active");
    document.getElementById("signinoverlay").classList.remove("active"); 
}