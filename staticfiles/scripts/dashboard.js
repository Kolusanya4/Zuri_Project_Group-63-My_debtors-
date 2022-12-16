const sideNavbar = document.getElementById('sideNavbar')
const hamburgerOpenMenu = document.getElementById('hamburger_openMenu')
const hamburgerCloseMenu = document.getElementById('hamburger_closeMenu')

hamburgerOpenMenu.addEventListener('click', show)
hamburgerCloseMenu.addEventListener('click', hide)

function show() {
  sideNavbar.style.display = 'block'
  sideNavbar.style.left = '0'
  hamburgerCloseMenu.style.display = 'block'
  hamburgerOpenMenu.style.display = 'none'

}

function hide() {
  sideNavbar.style.left = '-100%'
  hamburgerCloseMenu.style.display = 'none'
  hamburgerOpenMenu.style.display = 'block'
}
