const navLinks = document.getElementById('navLinks')
const btn = document.getElementById('btn')
const hamburgerOpenMenu = document.getElementById('hamburger_openMenu')
const hamburgerCloseMenu = document.getElementById('hamburger_closeMenu')

hamburgerOpenMenu.addEventListener('click', show)
hamburgerCloseMenu.addEventListener('click', hide)

function show() {
  navLinks.style.display = 'flex'
  navLinks.style.top = '3.7rem'
  btn.style.display = 'block'
  btn.style.top = '60%'
  hamburgerCloseMenu.style.display = 'block'
  hamburgerOpenMenu.style.display = 'none'
}

function hide() {
  navLinks.style.top = '-100%'
  btn.style.top = '-100%'
  hamburgerCloseMenu.style.display = 'none'
  hamburgerOpenMenu.style.display = 'block'
}
