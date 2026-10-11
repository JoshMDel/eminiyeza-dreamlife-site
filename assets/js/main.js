(function () {
  'use strict';
  document.documentElement.classList.remove('no-js');

  // Mobile menu
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // Scroll reveal
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // Forms: posted to FormSubmit (delivers to the organisation's inbox)
  document.querySelectorAll('form[data-ajax]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var status = form.querySelector('.form-status');
      var btn = form.querySelector('button[type="submit"]');
      var hp = form.querySelector('.hp input');
      if (hp && hp.value) { return; }
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var label = btn.textContent;
      btn.disabled = true; btn.textContent = 'Sending…';
      status.className = 'form-status'; status.textContent = '';
      fetch(form.dataset.endpoint, {
        method: 'POST',
        headers: { 'Accept': 'application/json' },
        body: new FormData(form)
      }).then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (res.ok && res.j.success !== 'false') {
            form.reset();
            status.className = 'form-status ok';
            status.textContent = form.dataset.success || 'Thank you — we have received your message.';
          } else { throw new Error('failed'); }
        })
        .catch(function () {
          status.className = 'form-status err';
          status.textContent = 'Sorry, that did not send. Please email us at ' + form.dataset.fallback + '.';
        })
        .finally(function () { btn.disabled = false; btn.textContent = label; });
    });
  });

  // Footer year
  var y = document.getElementById('year');
  if (y) { y.textContent = new Date().getFullYear(); }
})();
