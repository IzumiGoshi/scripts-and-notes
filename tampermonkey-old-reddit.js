// ==UserScript==
// @name         old reddit
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  redirect to old.reddit.com
// @author       You
// @match        https://www.reddit.com/*
// @icon         https://www.google.com/s2/favicons?domain=reddit.com
// @grant        none
// ==/UserScript==

window.addEventListener('load', function() {
    //window.location.href = "https://old.reddit.com/";
    var loc = "" + window.location;
    var parts = loc.split('/');
    if (parts.includes("r")) {
        parts.forEach(function(item, i) { if (item == "www.reddit.com") parts[i] = "old.reddit.com"; });
        loc = parts.join('/');
    }
    else {
        loc = "old.reddit.com";
    }
    window.location.href = loc;
}, false);
