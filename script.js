let question = "What is 2 + 2?";
let correct = "b";

document.getElementById("question").innerText = question;

function answer(choice) {
  if (choice === correct) {
    document.getElementById("result").innerText = "✅ Correct!";
  } else {
    document.getElementById("result").innerText = "❌ Wrong!";
  }
}
