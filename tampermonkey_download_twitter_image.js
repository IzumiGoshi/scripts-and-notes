// ==UserScript==
// @name        New script
// @namespace   Violentmonkey Scripts
// @match       *://x.com/*
// @grant       none
// @version     1.0
// @author      -
// @description 5/17/2024, 8:49:08 AM
// ==/UserScript==


function downloadImage(imageUrl) {
    let filename = imageUrl.split('/').pop();
    var xhr = new XMLHttpRequest();
    xhr.open('GET', imageUrl, true);
    xhr.responseType = 'blob';
    xhr.onload = function() {
        if (xhr.status === 200) {
            var blob = xhr.response;
            var url = window.URL.createObjectURL(blob);

            var a = document.createElement('a');
            a.href = url;
            a.download = filename || 'image.jpg'; // Default filename if not specified
            document.body.appendChild(a);
            a.click();

            // Cleanup
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
        }
    };
    xhr.send();
}

let mouse_pos = [25, 25];
document.addEventListener('mousemove', e => {
  mouse_pos = [e.clientX, e.clientY];
  //console.log(mouse_pos);
});

document.addEventListener('keydown', function(event) {
  console.log(event.key);
    if (event.key === 'd') {
      let img_el = document.elementFromPoint(mouse_pos[0], mouse_pos[1]);
      if (img_el.tagName != 'IMG') { return; }
      console.log('src: ' + img_el.src);
      downloadImage(img_el.src);
    }
});

