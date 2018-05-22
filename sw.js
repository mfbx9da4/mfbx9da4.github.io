var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
  '/',
  '/assets/img/chaordic-profile.jpg',
  '/assets/img/Fish-Tank/MP4/Fish-Tank.mp4',
  '/assets/img/Fish-Tank/WEBM/Fish-Tank.webm',
  '/assets/img/Fish-Tank/Snapshots/Fish-Tank.jpg',
  '/assets/cv.pdf',
  '/assets/cvs.pdf',
  '/assets/html5up-identity/assets/css/main.css',
  '/assets/html5up-identity/images/bg.jpg',
  '/assets/html5up-identity/assets/css/images/overlay.png',
  'https://fonts.googleapis.com/css?family=Source+Sans+Pro:300',
  'https://fonts.gstatic.com/s/sourcesanspro/v11/6xKydSBYKcSV-LCoeQqfX1RYOo3ik4zwlxdu3cOWxw.woff2',
  '/assets/html5up-identity/assets/fonts/fontawesome-webfont.woff2?v=4.6.3'
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

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        // Cache hit - return response
        if (response) {
          console.log('hit', event.request.url)
          return response;
        }
        console.log('miss', event.request.url)

        // IMPORTANT: Clone the request. A request is a stream and
        // can only be consumed once. Since we are consuming this
        // once by cache and once by the browser for fetch, we need
        // to clone the response.
        var fetchRequest = event.request.clone();

        return fetch(fetchRequest).then(
          function(response) {
            // Check if we received a valid response
            if(!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }

            // IMPORTANT: Clone the response. A response is a stream
            // and because we want the browser to consume the response
            // as well as the cache consuming the response, we need
            // to clone it so we have two streams.
            var responseToCache = response.clone();

            caches.open(CACHE_NAME)
              .then(function(cache) {
                cache.put(event.request, responseToCache);
              });

            return response;
          }
        );
      })
    );
});

self.addEventListener('activate', function(event) {
  console.log('Service worker updated')
});
