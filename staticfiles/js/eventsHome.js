/* jshint version: 2.13.6 */

/* This whole script was made by github copilot ai:
    - Main function: 
        - Show only 1/2/3 cards in the carousel based on the screen size
*/
document.addEventListener('DOMContentLoaded', function () {
    const carouselId = 'carouselUpcomingEvents';
    const carousel = document.getElementById(carouselId);
    if (!carousel) return;

    // Collect all individual card elements (the columns) from the initial markup
    function collectCards() {
        const cols = Array.from(carousel.querySelectorAll('.carousel-inner .col-12, .carousel-inner .col-sm-6, .carousel-inner .col-md-4, .carousel-inner .col'));
        // filter out any container rows or carousel-item wrappers, keep only direct card columns
        return cols.filter(el => el.classList.contains('col-12') || el.classList.contains('col-sm-6') || el.classList.contains('col-md-4') || el.classList.contains('col'))
                             .map(c => c.outerHTML);
    }

    function build(per) {
        const inner = carousel.querySelector('.carousel-inner');
        if (!inner) return;
        const cards = collectCards();
        inner.innerHTML = '';

        for (let i = 0; i < cards.length; i += per) {
            const item = document.createElement('div');
            item.className = 'carousel-item';
            if (i === 0) item.classList.add('active');
            const row = document.createElement('div');
            row.className = 'row';
            for (let j = 0; j < per; j++) {
                const idx = i + j;
                if (idx >= cards.length) break;
                // insert card HTML
                const wrapper = document.createElement('div');
                wrapper.innerHTML = cards[idx];
                // append the column node(s) inside the row
                Array.from(wrapper.childNodes).forEach(n => row.appendChild(n));
            }
            item.appendChild(row);
            inner.appendChild(item);
        }
    }

    function getPerByWidth() {
        const w = window.innerWidth;
        // <576px -> 1, >=576 and <992 -> 2, >=992 -> 3
        if (w < 576) return 1;
        if (w < 992) return 2;
        return 3;
    }

    // initial build
    build(getPerByWidth());

    // rebuild on resize when breakpoint changes
    let lastPer = getPerByWidth();
    let resizeTimer = null;
    window.addEventListener('resize', function () {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function () {
            const per = getPerByWidth();
            if (per !== lastPer) {
                build(per);
                lastPer = per;
            }
        }, 150);
    });
});