async function generate() {
const prompt = document.getElementById("prompt").value;
const response = await fetch("http://localhost:5000/api/generate", {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify({ prompt }),
});
const data = await response.json();
document.getElementById("result").innerText = data.result;
loadHistory();
}


async function loadHistory() {
const response = await fetch("http://localhost:5000/api/history");
const history = await response.json();
const list = document.getElementById("history");
list.innerHTML = "";
history.forEach(item => {
const li = document.createElement("li");
li.innerText = `${item.prompt} → ${item.result}`;
list.appendChild(li);
});
}


window.onload = loadHistory;