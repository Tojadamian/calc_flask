function toggleNum2(){
    const operation = document.getElementById("operation").value;
    const num2Field = document.getElementById("num2Field");
    if (operation === 'sqrt' ){
        num2Field.style.display = 'none';
        num2Field.required = false;
        num2Field.value = '';
    } else {
        num2Field.style.display = 'block';
        num2Field.required = true;
    }
}

window.onload = function() {
    toggleNum2();
    document.getElementById("operation").addEventListener("change", toggleNum2);
};