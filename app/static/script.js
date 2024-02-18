// Add interactivity with JavaScript

document.getElementById('loginBtn').addEventListener('click', function() {
  alert('Login clicked!');
});

document.getElementById('registerBtn').addEventListener('click', function() {
  alert('Register clicked!');
});

document.getElementById('aboutBtn').addEventListener('click', function() {
  alert('About clicked!');
});

document.getElementById('contactBtn').addEventListener('click', function() {
  alert('Contact clicked!');
});

document.getElementById('voteBtn').addEventListener('click', function() {
  alert('Vote Now clicked!');
});

// Example of changing the background color dynamically
document.body.addEventListener('mousemove', function(event) {
  const x = event.clientX / window.innerWidth;
  const y = event.clientY / window.innerHeight;

  const red = Math.round(x * 255);
  const green = Math.round(y * 255);
  const blue = Math.round((x + y) * 128);

  document.body.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`;
});
