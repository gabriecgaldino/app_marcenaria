window.addEventListener('DOMContentLoaded', function() {
    const btnEdit = document.getElementById('submit'); 
    const form = document.querySelector('form');  
    const inputs = document.querySelectorAll('input, textarea, select');  

    let edit = false;  

    btnEdit.addEventListener('click', function(event) {
        event.preventDefault(); 

        if (!edit) {
            inputs.forEach(input => input.removeAttribute('disabled'));

            btnEdit.classList.remove('btn-primary');
            btnEdit.classList.add('btn-success');
            btnEdit.textContent = 'Salvar';

            edit = true;
        } else {
            form.requestSubmit()
        }
    });
});