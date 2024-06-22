// const sideMenu = document.querySelector("aside");
// const menuBtn = document.querySelector("#menu-btn");
// const closeBtn = document.querySelector("#close-btn");
const themeToggler = document.querySelector(".theme-toggler");


// menuBtn.addEventListener('click', () => {
//     sideMenu.style.display = 'block';
// })


// closeBtn.addEventListener('click', () => {
//     sideMenu.style.display = 'none';
// })


// themeToggler.addEventListener('click', () => {
//     document.body.classList.toggle('dark-theme-variables');

//     themeToggler.querySelector('span:nth-child(1)').classList.toggle('active');
//     themeToggler.querySelector('span:nth-child(2)').classList.toggle('active');
// })
// let a=document.getElementById("log");
// let d=document.getElementById("dash");
// function logout(){
//     a.textContent="You are logged out from this Dashboard.";
//     a.classList.add("log");
// }
function handleFormSubmit(event) {
  event.preventDefault();  
  window.location.href = "/DASH BOARD/index.html"; 
}
// Example JavaScript for dynamic dropdowns and form submission handling

// Function to fetch user IDs and populate dropdowns
function populateUserDropdowns() {
  // Example: Fetch user IDs from backend API
  const userIDs = ['123', '456', '789']; // Replace with actual fetched data

  const checkinDropdown = document.getElementById('checkin_userid');
  const checkoutDropdown = document.getElementById('checkout_userid');

  // Populate Check-In dropdown
  userIDs.forEach(userID => {
      const option = document.createElement('option');
      option.value = userID;
      option.textContent = userID;
      checkinDropdown.appendChild(option);
  });

  // Populate Check-Out dropdown (clone options from Check-In for simplicity)
  userIDs.forEach(userID => {
      const option = document.createElement('option');
      option.value = userID;
      option.textContent = userID;
      checkoutDropdown.appendChild(option.cloneNode(true));
  });
}

// Function to handle Check-In form submission
function handleCheckInSubmit(event) {
  event.preventDefault();
  // Example: Handle form submission, send data to backend, etc.
  const formData = new FormData(event.target);
  console.log('Check-In Form Data:', formData);
  // Example: Make AJAX request to backend
  // fetch('/api/checkin', {
  //     method: 'POST',
  //     body: formData
  // })
  // .then(response => response.json())
  // .then(data => {
  //     console.log('Check-In Response:', data);
  // })
  // .catch(error => {
  //     console.error('Error:', error);
  // });
}

// Function to handle Check-Out form submission
function handleCheckOutSubmit(event) {
  event.preventDefault();
  // Example: Handle form submission, send data to backend, etc.
  const formData = new FormData(event.target);
  console.log('Check-Out Form Data:', formData);
  // Example: Make AJAX request to backend
  // fetch('/api/checkout', {
  //     method: 'POST',
  //     body: formData
  // })
  // .then(response => response.json())
  // .then(data => {
  //     console.log('Check-Out Response:', data);
  // })
  // .catch(error => {
  //     console.error('Error:', error);
  // });
}

// Populate dropdowns on page load
document.addEventListener('DOMContentLoaded', () => {
  populateUserDropdowns();
});
//change theme
themeToggler.addEventListener('click', () => {
  document.body.classList.toggle('dark-theme-variables');

  themeToggler.querySelector('span:nth-child(1)').classList.toggle('active');
  themeToggler.querySelector('span:nth-child(2)').classList.toggle('active');
})
let a=document.getElementById("log");
let d=document.getElementById("dash");
function logout(){
  a.textContent="You are logged out from this Dashboard.";
  a.classList.add("log");
}

