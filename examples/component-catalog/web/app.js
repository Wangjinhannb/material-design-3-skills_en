
const root=document.documentElement;
const themeToggle=document.querySelector('#themeToggle');
const setTheme=(dark)=>{root.dataset.theme=dark?'dark':'light';document.body.classList.toggle('dark',dark);};
let dark=false;themeToggle.addEventListener('click',()=>{dark=!dark;setTheme(dark)});
document.querySelector('#mixed').indeterminate=true;
const dialog=document.querySelector('#dialog');
document.querySelector('[data-open="dialog"]').addEventListener('click',()=>dialog.showModal());
const sheet=document.querySelector('#sheet');
document.querySelector('[data-open="sheet"]').addEventListener('click',()=>{sheet.hidden=false;sheet.querySelector('button').focus()});
document.querySelector('[data-close="sheet"]').addEventListener('click',()=>{sheet.hidden=true;document.querySelector('[data-open="sheet"]').focus()});
document.querySelectorAll('[role="tab"]').forEach(tab=>tab.addEventListener('click',()=>{document.querySelectorAll('[role="tab"]').forEach(x=>x.setAttribute('aria-selected','false'));tab.setAttribute('aria-selected','true')}));
document.querySelectorAll('.segmented button').forEach(btn=>btn.addEventListener('click',()=>{btn.parentElement.querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed','false'));btn.setAttribute('aria-pressed','true')}));
