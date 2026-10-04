const root=document.documentElement;
const toggle=document.getElementById('themeToggle');
const save=document.getElementById('save');
const status=document.getElementById('status');
const stored=localStorage.getItem('md3-theme');
if(stored==='light'||stored==='dark') root.dataset.theme=stored;
toggle.addEventListener('click',()=>{
  const current=root.dataset.theme|| (matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');
  const next=current==='dark'?'light':'dark';
  root.dataset.theme=next; localStorage.setItem('md3-theme',next);
});
save.addEventListener('click',()=>{status.textContent='Settings saved.';});
