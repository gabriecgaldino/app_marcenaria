user = document.getElementById('id-username').getAttribute('value')
pass = document.getElementById('id-password').getAttribute('value')

document.querySelector('.btn').addEventListener('submit', function() {
    console.log(user, pass)
})
