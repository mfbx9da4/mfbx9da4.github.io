var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
  '/',
  '/assets/img/chaordic-profile.jpg',
  '/assets/html5up-identity/assets/css/main.css',
  '/assets/html5up-identity/images/bg.jpg',
  '/assets/html5up-identity/assets/css/images/overlay.png',
  '/assets/img/Fish-Tank/MP4/Fish-Tank.mp4',
  // '/assets/img/Fish-Tank/WEBM/Fish-Tank.webm',
  // '/assets/img/Fish-Tank/Snapshots/Fish-Tank.jpg',
  // '/assets/cv.pdf',
  // '/assets/cvs.pdf',
  // 'https://fonts.googleapis.com/css?family=Source+Sans+Pro:300',
  // 'https://fonts.gstatic.com/s/sourcesanspro/v11/6xKydSBYKcSV-LCoeQqfX1RYOo3ik4zwlxdu3cOWxw.woff2',
  '/assets/html5up-identity/assets/fonts/fontawesome-webfont.woff2?v=4.6.3'
];

self.addEventListener('install', function(event) {
  console.log('install')

  // force new service worker to become the active one
  self.skipWaiting();

  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

function isIncluded (url, urls) {
  for (var i = 0; i < urls.length; i++) {
    var toCacheUrl = urls[i]
    if (url.indexOf(toCacheUrl) > -1) {
      return true
    }
  }
  return false;
}

function mobileAndTabletcheck () {
  var check = false;
  (function(a){if(/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino|android|ipad|playbook|silk/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0,4))) check = true;})(navigator.userAgent||navigator.vendor||window.opera);
  return check;
};

// On fetch, use cache but update the entry with the latest contents
// from the server.
self.addEventListener('fetch', function(event) {

  var url = event.request.url;
  console.log('fetch', url)

  // var includes = isIncluded(url, urlsToCache.slice(1))
  // var split = url.split(location.origin)
  // url = split[1] || split[0]
  // var includes = urlsToCache.includes(url)
  // console.log('includes', url, includes)

  if (url.indexOf('chrome-extension') > -1
    || url.indexOf('/sw.js') > -1) {
    console.log('ignore', url)
    return
  }

  event.respondWith(fromCache(event))
});

// Open the cache where the assets were stored and search for the requested
// resource. Notice that in case of no matching, the promise still resolves
// but it does with `undefined` as value.
function fromCache(event) {
  var request = event.request;
  return caches.open(CACHE_NAME).then(function (cache) {
    return cache.match(request).then(function(cachedResponse) {
      if (cachedResponse) {
        // If we found a match in the cache, return it, but also
        // update the entry in the cache in the background.
        event.waitUntil(
          cache
            .add(request)
            .catch(function(error) {
              console.log('Could not fetch again', error, request.url);
              return error
            })
        )
        console.log('hit', request.url)
        return cachedResponse;
      }

      // If we didn't find a match in the cache, use the network.
      // And update the cache
      return fetchAndUpdateCache(cache, request);
    })
  });
}


// Update consists in opening the cache, performing a network request and
// storing the new response data.
// function update(request) {
//   return caches.open(CACHE_NAME).then(function (cache) {
//     return fetch(request)
//       .then(function (response) {
//         return cache.put(request, response.clone()).then(function () {
//           console.log('update cache for', request.url)
//           return response;
//         });
//       })
//       .catch(function (error) {
//         console.log('fail', error)
//       })
//   });
// }

// Update consists in opening the cache, performing a network request and
// storing the new response data.
function fetchAndUpdateCache(cache, request) {
  console.log('fetchAndUpdateCache', request.url)
  return fetch(request)
    .then(function (response) {
      console.log('fetched, update cache for', request.url)
      return cache.put(request, response.clone()).then(function () {
        return response;
      });
    })
    .catch(function (error) {
      console.log('fail', error)
    })
}

self.addEventListener('activate', function(event) {
  console.log('🎉 Service worker updated')
});

