let addBtn = document.getElementsByClassName("addBtn")[0]
let addingPage = document.getElementsByClassName("addingPage")[0]
let items = document.getElementsByClassName("items")[0]
let backImg = document.getElementsByClassName("back-img")[0]
addBtn.addEventListener("click", function () {
    addingPage.classList.remove("d-none")
    addBtn.classList.add("d-none")
    items.classList.add("d-none")
    backImg.classList.toggle("d-none")
})