document.addEventListener('DOMContentLoaded', function() {
    
    function configurarBotaoUpload(inputId, labelId) {
        var inputElement = document.getElementById(inputId);
        var labelElement = document.getElementById(labelId);

        if (inputElement && labelElement) {
            inputElement.addEventListener('change', function() {
                if (this.files && this.files.length > 0) {
                    labelElement.innerHTML = '<i class="bi bi-file-earmark-check text-success me-2"></i>' + this.files[0].name;
                } else {
                    labelElement.innerHTML = 'Escolher arquivo';
                }
            });
        }
    }

    configurarBotaoUpload('csvTecnicos', 'labelCsvTecnicos');
    configurarBotaoUpload('csvDocentes', 'labelCsvDocentes');
    configurarBotaoUpload('csvProbatorio', 'labelCsvProbatorio');
    configurarBotaoUpload('csvContrato', 'labelCsvContrato');
});