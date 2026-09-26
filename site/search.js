const form = document.querySelector('#text-search');
const query = document.querySelector('#query');
const component = document.querySelector('#component');
const status = document.querySelector('#text-search-status');
const results = document.querySelector('#search-results');
const more = document.querySelector('#more-results');
const normalize = text => text.normalize('NFKC').toLocaleLowerCase();
let index, pending, matches = [], shown = 0;
form.hidden = false;
query.value = new URLSearchParams(location.search).get('q')?.slice(0, 200) || '';
async function loadIndex() {
  if (index) return index;
  if (!pending) pending = fetch('search-index.json').then(response => {
    if (!response.ok) throw new Error('Index request failed');
    return response.json();
  }).then(data => {
    index = data;
    for (const doc of data) {
      const option = document.createElement('option');
      option.value = doc.url; option.textContent = doc.title; component.append(option);
      for (const passage of doc.passages) passage.normalized = normalize(passage.text);
    }
    return index;
  }).catch(error => { pending = undefined; throw error; });
  return pending;
}
function showMore() {
  const end = Math.min(shown + 30, matches.length);
  for (; shown < end; shown++) {
    const {doc, passage} = matches[shown];
    const article = document.createElement('article'); article.className = 'search-result';
    const heading = document.createElement('h2');
    const link = document.createElement('a'); link.href = doc.url + '#' + passage.anchor; link.textContent = doc.title;
    heading.append(link); article.append(heading);
    const excerpt = document.createElement('p');
    const terms = normalize(query.value).trim().split(/\s+/);
    const first = Math.max(0, passage.normalized.indexOf(terms[0]) - 100);
    excerpt.textContent = (first ? '…' : '') + passage.text.slice(first, first + 500) + (passage.text.length > first + 500 ? '…' : '');
    article.append(excerpt); results.append(article);
  }
  more.hidden = shown >= matches.length;
  status.textContent = matches.length ? `${matches.length} matching passages. Showing ${shown}.` : 'No matching passages. Try fewer words or another document.';
}
let request = 0;
async function search(event) {
  event?.preventDefault();
  const currentRequest = ++request;
  const words = normalize(query.value).trim().split(/\s+/).filter(Boolean);
  results.replaceChildren(); more.hidden = true;
  history.replaceState(null, '', words.length ? '?q=' + encodeURIComponent(query.value.trim()) : location.pathname);
  if (!words.length) { status.textContent = 'Enter words to search the publication text.'; return; }
  status.textContent = 'Loading document text…';
  try {
    const docs = await loadIndex();
    if (currentRequest !== request) return;
    matches = [];
    for (const doc of docs) {
      if (component.value && doc.url !== component.value) continue;
      for (const passage of doc.passages) if (words.every(word => passage.normalized.includes(word))) matches.push({doc, passage});
    }
    shown = 0; showMore();
  } catch { if (currentRequest === request) status.textContent = 'Document text could not load. Try Search again, or use the publication library.'; }
}
form.addEventListener('submit', search);
component.addEventListener('change', search);
more.addEventListener('click', showMore);
if (query.value) search();
else {
  status.textContent = 'Loading document text…';
  loadIndex().then(() => { if (!request) status.textContent = 'Ready to search 14 documents. Enter words above.'; })
    .catch(() => { if (!request) status.textContent = 'Document text could not load. Try Search again, or use the publication library.'; });
}
