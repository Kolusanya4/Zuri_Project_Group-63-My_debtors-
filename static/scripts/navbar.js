const navLinks = document.getElementById('navLinks')
const btn = document.getElementById('btn')
const hamburgerMenu = document.getElementById('hamburger_menu')

hamburgerMenu.addEventListener('click', () => {
  hamburgerMenu.classList.toggle('close')
  // navLinks.style.display = 'flex'
  // btn.style.display = 'block'
})
