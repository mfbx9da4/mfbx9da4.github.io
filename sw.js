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
  console.log('install')
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

// On fetch, use cache but update the entry with the latest contents
// from the server.
self.addEventListener('fetch', function(evt) {
  if (evt.request.url.indexOf('chrome-extension') > -1) {
    console.log('ignore', evt.request.url)
    return
  }

  // You can use `respondWith()` to answer ASAP...
  evt.respondWith(fromCache(evt.request));
  // ...and `waitUntil()` to prevent the worker to be killed until
  // the cache is updated.
  evt.waitUntil(
    update(evt.request)
    // Finally, send a message to the client to inform it about the
    // resource is up to date.
    .then(refresh)
  );
});

// Open the cache where the assets were stored and search for the requested
// resource. Notice that in case of no matching, the promise still resolves
// but it does with `undefined` as value.
function fromCache(request) {
  return caches.open(CACHE_NAME).then(function (cache) {
    return cache.match(request).then(function(response) {
      console.log('hit', request.url)
      return response;
    })
  });
}


// Update consists in opening the cache, performing a network request and
// storing the new response data.
function update(request) {
  return caches.open(CACHE_NAME).then(function (cache) {
    return fetch(request).then(function (response) {
      return cache.put(request, response.clone()).then(function () {
        console.log('update cache for', request.url)
        return response;
      });
    });
  });
}

// Sends a message to the clients.
function refresh(response) {
  return self.clients.matchAll().then(function (clients) {
    clients.forEach(function (client) {
      // Encode which resource has been updated. By including the
      // [ETag](https://en.wikipedia.org/wiki/HTTP_ETag) the client can
      // check if the content has changed.
      var message = {
        type: 'refresh',
        url: response.url,
        // Notice not all servers return the ETag header. If this is not
        // provided you should use other cache headers or rely on your own
        // means to check if the content has changed.
        eTag: response.headers.get('ETag')
      };
      // Tell the client about the update.
      client.postMessage(JSON.stringify(message));
    });
  });
}

self.addEventListener('activate', function(event) {
  console.log('Service worker updated')
});

