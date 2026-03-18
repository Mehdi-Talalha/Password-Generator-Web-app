// Here im ganna make the image border 50%
// i selected the image by querySelector and change her style
document.addEventListener('DOMContentLoaded', function() {
    const logoImage = document.querySelector('.logo-image-head')
    if (logoImage) {
        logoImage.style.borderRadius = '50%'
    }
})