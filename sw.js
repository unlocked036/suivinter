// Service worker : fait fonctionner l'appli hors connexion.
// Pour publier une nouvelle version de l'appli, changez simplement le numéro ci-dessous.
var CACHE = 'suivi-v1';
var FILES = ['./', './index.html', './manifest.webmanifest', './icon-192.png', './icon-512.png', './icon-maskable-512.png', './apple-touch-icon.png'];

self.addEventListener('install', function (e) {
  e.waitUntil(caches.open(CACHE).then(function (c) { return c.addAll(FILES); }).then(function () { return self.skipWaiting(); }));
});

self.addEventListener('activate', function (e) {
  e.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.filter(function (k) { return k !== CACHE; }).map(function (k) { return caches.delete(k); }));
    }).then(function () { return self.clients.claim(); })
  );
});

self.addEventListener('fetch', function (e) {
  var req = e.request, url = new URL(req.url);
  // On ne touche ni aux envois de données, ni aux autres sites, ni à l'éventuel serveur de synchronisation.
  if (req.method !== 'GET' || url.origin !== self.location.origin || url.pathname.indexOf('/api/') !== -1) return;

  // Page : le réseau d'abord (les mises à jour s'affichent dès qu'on est en ligne), le cache en secours.
  if (req.mode === 'navigate') {
    e.respondWith(
      fetch(req).then(function (res) {
        if (res.ok) { var copy = res.clone(); caches.open(CACHE).then(function (c) { c.put('./index.html', copy); }); }
        return res;
      }).catch(function () { return caches.match('./index.html'); })
    );
    return;
  }
  // Icônes et manifeste : le cache d'abord.
  e.respondWith(caches.match(req).then(function (hit) { return hit || fetch(req); }));
});
