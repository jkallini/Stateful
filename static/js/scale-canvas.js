document.addEventListener("DOMContentLoaded", function(event) {
    //get canvas
    let canv = document.getElementById('canvas');

    const width = 800;
    const height = 480;
    const pixelRatio = window.devicePixelRatio || 1;

    //get context
    let ctx = canv.getContext('2d');

    canv.width = width * pixelRatio;
    canv.height = height * pixelRatio;

    canv.style.width = `${width}px`;
    canv.style.height = `${height}px`;

    ctx.mozImageSmoothingEnabled = false;
    ctx.imageSmoothingEnabled = false;

    ctx.scale(pixelRatio, pixelRatio);
});