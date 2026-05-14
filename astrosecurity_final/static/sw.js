// AstroSecurity Service Worker v1
// Cachea assets estáticos para funcionamiento offline básico

const CACHE_NAME = 'astrosecurity-v1';

// Archivos que se guardan en caché al instalar
const STATIC_ASSETS = [
  '/',
  '/presentacion',
  '/static/css/style.css',
  '/static/img/logo.png',
  '/static/img/icon-192.png',
  '/static/img/icon-512.png',
  '/offline'
];

// ── Instalación: pre-cachear assets ──────────────
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(STATIC_ASSETS).catch(() => {
        // Si algún asset falla, continuar igual
      });
    })
  );
  self.skipWaiting();
});

// ── Activación: limpiar cachés viejas ─────────────
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
      )
    )
  );
  self.clients.claim();
});

// ── Fetch: red primero, caché como respaldo ────────
self.addEventListener('fetch', event => {
  // Solo interceptar GET
  if (event.request.method !== 'GET') return;

  // Assets estáticos: caché primero
  if (event.request.url.includes('/static/')) {
    event.respondWith(
      caches.match(event.request).then(cached => {
        return cached || fetch(event.request).then(response => {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
          return response;
        });
      })
    );
    return;
  }

  // Páginas HTML: red primero, offline como respaldo
  event.respondWith(
    fetch(event.request).catch(() =>
      caches.match(event.request).then(cached =>
        cached || caches.match('/offline')
      )
    )
  );
});
