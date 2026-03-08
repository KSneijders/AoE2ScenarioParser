const collapseToC = () => {
    if (window.screen.width < 1220) {
        document.querySelectorAll('.md-nav__toggle').forEach((e) => e.classList.add('disable-instant-css'))
        document.querySelectorAll('.md-nav__item--nested .md-nav__toggle').forEach((e) => e.classList.add('disable-instant-css'))

        return;
    }

    /*
     | Update window path name to only useful part
     |
     | '/AoE2ScenarioParser/api_docs/player/player/'
     | ['','AoE2ScenarioParser','api_docs','player','player','']
     | ['player','player']
     */
    const path = window.location.pathname.split('/').slice(3, -1);
    console.log("Path", path);

    const primary = '.md-nav--primary .md-nav__item.md-nav__item--nested';
    const selector = '.md-nav__toggle ~ .md-nav:not([data-md-level="0"]):not([data-md-level="1"])';

    const completeSelector = `${primary} ${selector}`;
    console.log(`Selector: [${completeSelector}]`)

    let index = 0;
    document.querySelectorAll(completeSelector)
        .forEach((e) => {
            const input = e.parentNode.children[0];
            const label = e.parentNode.children[1];

            console.log(label, input)

            if (!label || !('click' in label) || index >= path.length)
                return;

            const labelName = label.innerText.toLowerCase();  /* Do not trim */
            const pathName = path[index].toLowerCase().replace('_', '');

            console.log(`\tLabel: [${labelName}] // Path: [${pathName}]`)

            const collapseElement = labelName !== pathName;

            if (collapseElement) {
                label.click();  /* Close the menu item */
            } else {
                index++;
                console.log(`Match! Continue index to: ${index}`)
            }

            if (input) {
                input.classList.add('disable-instant-css');
            }
        });
}

window.addEventListener('load', function() {
    collapseToC();
});
