(function () {
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("visible"); });
  }

  var navLinks = document.querySelectorAll("[data-nav]");
  var sections = [];
  navLinks.forEach(function (link) {
    var id = link.getAttribute("href");
    if (id && id.charAt(0) === "#") {
      var section = document.querySelector(id);
      if (section) sections.push({ link: link, section: section });
    }
  });

  if (sections.length && "IntersectionObserver" in window) {
    var navIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          navLinks.forEach(function (l) { l.classList.remove("active"); });
          var match = sections.find(function (s) { return s.section === entry.target; });
          if (match) match.link.classList.add("active");
        }
      });
    }, { rootMargin: "-40% 0px -50% 0px", threshold: 0 });
    sections.forEach(function (s) { navIO.observe(s.section); });
  }
})();
