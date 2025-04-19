document.addEventListener("DOMContentLoaded", function () {
    gsap.registerPlugin(ScrollTrigger);

    gsap.from(".hero h1", { opacity: 0, y: -50, duration: 1 });
    gsap.from(".hero p", { opacity: 0, y: 20, duration: 1, delay: 0.5 });
    gsap.from(".scroll-btn", { opacity: 0, y: 30, duration: 1, delay: 1 });

    gsap.utils.toArray(".step, .card").forEach((el) => {
        gsap.from(el, {
            scrollTrigger: {
                trigger: el,
                start: "top 90%",
                toggleActions: "play none none none"
            },
            opacity: 0,
            y: 50,
            duration: 0.8,
            ease: "power2.out"
        });
    });

    document.querySelectorAll(".scroll-btn, .glow-btn").forEach((btn) => {
        btn.addEventListener("click", function (event) {
            event.preventDefault();
            let target = document.querySelector(this.getAttribute("href"));
            if (target) {
                window.scrollTo({ top: target.offsetTop - 50, behavior: "smooth" });
            }
        });
    });
});
