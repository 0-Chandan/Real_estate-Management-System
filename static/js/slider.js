var swiper = new Swiper(".slide-content", {
    slidesPerView: 3,
    spaceBetween: 25,
    loop: true,
    centerSlide: true,
    fade:true,
    grabCursor: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
      dynamicBullets: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevE1: ".swiper-button-prev",
    },
    breakpoints: {
      0 : {
        slidesPerView: 1,
      },
      520 : {
        slidesPerView: 2,
      },
      990 : {
        slidesPerView: 3,
      }
    },
  });
  Conclusion