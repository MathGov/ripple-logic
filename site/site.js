const controls = document.querySelector('#search-controls');
const input = document.querySelector('#search');
const cards = [...document.querySelectorAll('.document')];
controls.hidden = false;
function filter() {
  const terms = input.value.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
  let count = 0;
  for (const card of cards) {
    card.hidden = !terms.every(term => card.textContent.toLocaleLowerCase().includes(term));
    if (!card.hidden) count++;
  }
  document.querySelector('#search-status').textContent = `${count} of ${cards.length} components`;
  document.querySelector('#no-results').hidden = count !== 0;
}
input.addEventListener('input', filter);
document.querySelector('#clear-search').addEventListener('click', () => { input.value = ''; filter(); input.focus(); });
