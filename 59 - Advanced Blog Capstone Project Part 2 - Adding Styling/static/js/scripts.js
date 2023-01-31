
let show = false
const olderBtn = document.getElementById('older')
const blogList = document.querySelector('.post-list')

function toggle() {
    show = !show
    show ? olderBtn.innerText = "→ Hide Posts " : olderBtn.innerText = "Older Posts →"
    displayOlder(show)
}

function displayOlder(show) {
    let len = blogList.children.length
    if (show) {
        blogList.children[len - 1].classList.remove('d-none');
        blogList.children[len - 2].classList.remove('d-none')
    } else {
        blogList.children[len - 1].classList.add('d-none');
        blogList.children[len - 2].classList.add('d-none')
    }
}
displayOlder(show)

olderBtn.addEventListener('click', toggle)