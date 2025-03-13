window.addEventListener('DOMContentLoaded', function() {
    const btnEdit = document.getElementById('submit'); 
    const form = document.querySelector('.edit_order'); // Pegue o formulário correto
    const inputs = form.querySelectorAll('input, textarea, select'); // Pegue apenas os inputs do formulário

    // Desativa todos os inputs no início
    inputs.forEach(input => input.setAttribute('disabled', 'disabled'));

    let edit = false;  

    btnEdit.addEventListener('click', function(event) {
        event.preventDefault(); 

        if (!edit) {
            // Habilita os inputs para edição
            inputs.forEach(input => input.removeAttribute('disabled'));

            btnEdit.classList.remove('btn-primary');
            btnEdit.classList.add('btn-success');
            btnEdit.textContent = 'Salvar';

            edit = true;
        } else {
            form.requestSubmit(); // Agora enviará corretamente os dados do formulário certo
        }
    });
});