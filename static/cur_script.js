// Autocomplete logic for both currency fields
function setupAutocomplete(inputId, suggestionsId) {
    const input = document.getElementById(inputId);
    const suggestions = document.getElementById(suggestionsId);

    input.addEventListener("input", async () => {
        const query = input.value;
        if (query) {
            const response = await fetch(`/api/search-currencies?q=${query}`);
            const data = await response.json();
            showSuggestions(data, input, suggestions);
        } else {
            suggestions.innerHTML = "";
        }
    });

    document.addEventListener("click", (e) => {
        if (!suggestions.contains(e.target) && e.target !== input) {
            suggestions.innerHTML = "";
        }
    });
}

function showSuggestions(currencies, input, suggestions) {
    suggestions.innerHTML = "";
    currencies.forEach(currency => {
        const div = document.createElement("div");
        div.textContent = currency;
        div.addEventListener("click", () => {
            input.value = currency;
            suggestions.innerHTML = "";
        });
        suggestions.appendChild(div);
    });
}

// Set up autocomplete for both fields
setupAutocomplete("from_currency", "from_suggestions");
setupAutocomplete("to_currency", "to_suggestions");

// Handle form submission via AJAX
document.getElementById("convert-form").addEventListener("submit", async function(e) {
    e.preventDefault();
    const from = document.getElementById("from_currency").value;
    const to = document.getElementById("to_currency").value;
    const amount = document.getElementById("amount").value;
    const resultDiv = document.getElementById("conversion-result");
    const outputDiv = document.getElementById("conversion-output");

    if (!from || !to || !amount) {
        resultDiv.innerHTML = "<span style='color:red;'>Please fill all fields.</span>";
        return;
    }

    resultDiv.innerHTML = "Converting...";
    outputDiv.innerHTML = ""; // czyść poprzedni wynik

    try {
        const response = await fetch(`/api/convert-currency`, {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams({
                amount: amount,
                from_currency: from,
                to_currency: to
            })
        });
        const data = await response.json();
        if (data.result !== undefined) {
            resultDiv.innerHTML = "";
            outputDiv.innerHTML = `<h2>Converted Amount: ${data.result}</h2>`;
        } else {
            resultDiv.innerHTML = `<span style='color:red;'>${data.error || 'Conversion failed.'}</span>`;
            outputDiv.innerHTML = "";
        }
    } catch (err) {
        resultDiv.innerHTML = "<span style='color:red;'>Error connecting to API.</span>";
        outputDiv.innerHTML = "";
    }
});
