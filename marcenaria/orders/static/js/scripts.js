window.addEventListener('DOMContentLoaded', function() {
    const send_button = document.getElementById('submit')
    const inputs = document.querySelectorAll('input, textarea, select');

    inputs.forEach(input => {
        input.setAttribute('disabled', true);
    });

    send_button.addEventListener('click', function(){
        inputs.forEach(input => {
            input.removeAttribute('disabled')
        });

        send_button.textContent = 'Salvar';
        send_button.setAttribute('type', 'submit')
    })

    

});

