var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
  '/assets/img/chaordic-profile.jpg',
  '/assets/img/Fish-Tank/MP4/Fish-Tank.mp4',
  '/assets/img/Fish-Tank/WEBM/Fish-Tank.webm',
  '/assets/img/Fish-Tank/Snapshots/Fish-Tank.jpg',
  '/assets/cv.pdf',
  '/assets/html5up-identity/assets/css/main.css'
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});
