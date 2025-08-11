// Simple toggle dark mode (future enhancement)
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
}

// Future search/filter functionality placeholder
function filterTable(inputId, tableId) {
    const input = document.getElementById(inputId);
    const filter = input.value.toUpperCase();
    const table = document.getElementById(tableId);
    const rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++) {
        const cells = rows[i].getElementsByTagName("td");
        let match = false;

        for (let j = 0; j < cells.length; j++) {
            const cellText = cells[j].innerText || cells[j].textContent;
            if (cellText.toUpperCase().indexOf(filter) > -1) {
                match = true;
                break;
            }
        }

        rows[i].style.display = match ? "" : "none";
    }
}
