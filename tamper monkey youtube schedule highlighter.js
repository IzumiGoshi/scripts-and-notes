// ==UserScript==
// @name         YT_SCHEDULE_HIGHLIGHT
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://www.youtube.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=youtube.com
// @grant        none
// ==/UserScript==



let LAST_RAN = Date.now() - 200;

function fix_times() {
	if (Date.now() - LAST_RAN < 200) {
		// console.log('SKIPPED');
		return;
	}

	let times = document.getElementsByClassName('inline-metadata-item');
	for (let t of times) {
		let ih = t.innerHTML;
		let nows = Date.now() / 1000;
		let DAY_SECONDS = 60*60*24;
		let HOUR_SECONDS = 60*60;

		if (! ih.startsWith('Scheduled for')) { continue; }

		let mdy = ih.slice(14, );
		let mdys = Date.parse(mdy) / 1000;
		// console.log('mdys: ', mdys);
		let until = mdys - nows;
		let days_left = Math.floor(until / DAY_SECONDS);
		let hours_left = (until - (days_left * DAY_SECONDS)) / HOUR_SECONDS;
		hours_left = hours_left.toFixed(2);

		/*
			NEON GREEN ->      less than 24 hours
			YELLOW-ORANGE ->   less than 48 hours
			BLUE ->            over 2 days
		*/
		let NEON_RED = '#ff621f';
		let YELLOW_ORANGE = '#f2c924';
		let BLUE = '#1f85de';
		let col = BLUE;
		if (days_left < 1) { col = NEON_RED; }
		else if (days_left < 2) { col = YELLOW_ORANGE; }
		let new_ih = "<span style='color: COLOR; font-size: 2.25rem; font-weight: bold;'>DAYS HOURS</span>";
		new_ih = new_ih.replace('COLOR', col);
		new_ih = new_ih.replace('DAYS', days_left + ' DAYS');
		new_ih = new_ih.replace('HOURS', '  ' + hours_left + ' HOURS');

		t.innerHTML = new_ih;

		LAST_RAN = Date.now();
		// console.log('RAN');
	}
}

// window.addEventListener("load", (event) => { fix_times(); });

document.addEventListener("scroll", (event) => { fix_times(); });
