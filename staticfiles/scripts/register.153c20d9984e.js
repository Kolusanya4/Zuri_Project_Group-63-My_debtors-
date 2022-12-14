let schBtn=document.getElementsByClassName('owner-btn')
let debtBtn=document.getElementsByClassName('debtor-btn')
let schForm=document.getElementsByClassName('school-form')
let debtForm=document.getElementsByClassName('debtor-form')
let headText=document.getElementsByTagName('h3')[0]
console.log(headText)

debtForm[0].classList.add('hide')
schBtn[0].addEventListener('click',()=>{
    headText.textContent='Create school-owner account'
    debtForm[0].classList.add('hide')
    schForm[0].classList.remove('hide')
    schBtn[0].style.backgroundColor='white'
    schBtn[0].style.color='#274690'
    debtBtn[0].style.backgroundColor='#274690'
    debtBtn[0].style.color='white'
    debtBtn[0].style.border='2px solid white'
})

debtBtn[0].addEventListener('click',()=>{
    headText.textContent='Create  debtor account'
    schForm[0].classList.add('hide')
    debtForm[0].classList.remove('hide')
    debtBtn[0].style.backgroundColor='white'
    debtBtn[0].style.color='#274690'
    schBtn[0].style.backgroundColor='#274690'
    schBtn[0].style.color='white'
    schBtn[0].style.border='2px solid white'
})