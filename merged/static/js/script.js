document.getElementById("refresh-btn").addEventListener("click", function () {
    document.getElementById("total-tests").textContent = Math.floor(Math.random() * 50) + 10;
    document.getElementById("passed-tests").textContent = Math.floor(Math.random() * 40) + 5;
    document.getElementById("warnings").textContent = Math.floor(Math.random() * 5);
    document.getElementById("failed-tests").textContent = Math.floor(Math.random() * 5);
});

function loadProject(projectName) {
    document.getElementById("project-title").textContent = projectName + " Dashboard Overview";
}
