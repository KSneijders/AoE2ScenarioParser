const collapseToC = () => {
    /*
     | Update window path name to only useful part
     |
     | '/AoE2ScenarioParser/api_docs/player/player/'
     | ['','AoE2ScenarioParser','api_docs','player','player','']
     | ['player','player']
     */
    const path = window.location.pathname.split('/').slice(3, -1);
    console.log(path);

    const primary = '.md-nav--primary .md-nav__item.md-nav__item--nested';
    const selector = '.md-nav__toggle ~ .md-nav:not([data-md-level="0"]):not([data-md-level="1"])';

    console.log(primary, selector)

    let index = 0;

    document.querySelectorAll(`${primary} ${selector}`)
        .forEach((e) => {
            const input = e.parentNode.children[0];
            const label = e.parentNode.children[1];

            if (!label || !('click' in label))
                return;

            const labelName = label.innerText.toLowerCase();
            const pathName = path[index].toLowerCase().replace('_', '');

            const collapseElement = labelName !== pathName;

            if (collapseElement) {
                label.click();
            } else {
                index++;
            }

            if (input) {
                input.classList.add('disable-instant-css');
            }
        });
}

window.addEventListener('load', function() {
    collapseToC();
});
