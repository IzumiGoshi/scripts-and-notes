// ==UserScript==
// @name         block_youtube
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  redirect to subs
// @author       You
// @match        https://www.youtube.com/*
// @icon         https://www.google.com/s2/favicons?domain=youtube.com
// @grant        none
// ==/UserScript==


var intervalID = window.setInterval(
    function() {
        if (window.location.href == "https://www.youtube.com" || window.location.href == "https://www.youtube.com/") {
            window.location.href = "https://www.youtube.com/feed/subscriptions";
        }
}, 333);

