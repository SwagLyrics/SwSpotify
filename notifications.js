const notification_timeout = 4000;
let isFirst = true;
const interval = 1000;
const hash = hex_md5("temp");

const alert_str = "[SwagLyrics for Spotify]";
console.log(alert_str, "initializing (available: " + (typeof window.Notification != 'undefined') + ")");

const selectors = {
	albumArt:
		'#main .Root__now-playing-bar .now-playing-bar__left .cover-art-image.cover-art-image-loaded',
	trackName: '.track-info__name a',
	artistName: '.track-info__artists a',
	playPauseBtn:
		'#main .Root__now-playing-bar .now-playing-bar__center .player-controls__buttons button:nth-child(3)',
	prevBtn:
		'#main .Root__now-playing-bar .now-playing-bar__center .player-controls__buttons button:nth-child(2)',
	nextBtn:
		'#main .Root__now-playing-bar .now-playing-bar__center .player-controls__buttons button:nth-child(4)',
};

const checks = {
	art: function () {
		let $img = $('#cover-art').find('.sp-image-img');
		if ($img.length > 0) {

			return document.querySelector(`${selectors.albumArt}`).style.backgroundImage;
		}
		return null;
	},
	name: function () {
		return document.querySelector(`${selectors.trackName}`).innerText;
	},
	artist: function () {
		return document.querySelector(`${selectors.artistName}`).innerText;
	}
};

if (window.Notification) {
	console.log(alert_str, "requesting notification permission");
	window.Notification.requestPermission(function () {
		console.log(alert_str, "notification permission granted");
		if (!localStorage.scn_hash) {
			localStorage.scn_hash = hash;
		}
		setInterval(function () {
			let result = {};
			let hash = null;
			let text = null;
			let cont = false;

			for (let i in checks) {
				if (checks.hasOwnProperty(i)) {
					text = checks[i].call();
					if (typeof text != "undefined" && text != null && text.length > 0) {
						result[i] = text;
						cont = true;
					}
				}
			}

			const xhr = new XMLHttpRequest();
			const url = "http://127.0.0.1:5042";
			xhr.open("POST", url, true);
			xhr.setRequestHeader("Content-type", "application/json");
			xhr.onreadystatechange = function () {
				if (xhr.readyState == 4 && xhr.status == 200) {
					let json = JSON.parse("{}");
				}
			};
			let data = JSON.stringify({title: result.name, artist: result.artist});

			// if(isFirst){
			// 	// send initial data packet
			// 	xhr.send(data);
			// 	isFirst = false;
			// }

			if (cont) {
				setTimeout(function () {
					hash = hex_md5(JSON.stringify(result));
					if (localStorage.scn_hash !== hash) {
						localStorage.scn_hash = hash;
						console.log(alert_str, "new song", result);
						let notification = new window.Notification(result.name, {
							body: result.artist,
							icon: result.art
						});
						setTimeout(function () {
							notification.close();
						}, notification_timeout);
					}
					xhr.send(data);
				}, 200);
			}
		}, interval);
	});
}



 


