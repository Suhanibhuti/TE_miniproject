

const navBar = document.querySelector("nav"),
  menuBtns = document.querySelectorAll(".menu-icon"),
  overlay = document.querySelector(".overlay");
menuBtns.forEach((menuBtn) => {
  menuBtn.addEventListener("click", () => {
    navBar.classList.toggle("open");
  });
});
overlay.addEventListener("click", () => {
  navBar.classList.remove("open");
});



// $(document).ready(function () {
//   $('[data-toggle="tooltip"]').tooltip();
// });

// const navBar = document.querySelector("nav"),
//        menuBtns = document.querySelectorAll(".menu-icon"),
//        overlay = document.querySelector(".overlay");
//      menuBtns.forEach((menuBtn) => {
//        menuBtn.addEventListener("click", () => {
//          navBar.classList.toggle("open");
//        });
//      });
//      overlay.addEventListener("click", () => {
//        navBar.classList.remove("open");
//      });


     
// $(document).ready(function(){
// $('[data-toggle="tooltip"]').tooltip();
// });

// function addRow() {
//   var table = document.getElementById("myTable").getElementsByTagName('tbody')[0];
//   var newRow = table.insertRow(table.rows.length);
//   var cell1 = newRow.insertCell(0);
//   var cell2 = newRow.insertCell(1);
//   var cell3 = newRow.insertCell(2);

//   cell1.innerHTML = "<input type='number' value=''>";
//   cell2.innerHTML = "<input type='text' value=''>";
//   cell3.innerHTML = "<input type='text' value=''>";

  
//   deleteCell.innerHTML = "<button class='delete-btn' onclick='deleteRow(this)'>Delete</button>";
// }



   
  

// function fetchData() {
//   var xhr = new XMLHttpRequest();
//   xhr.onreadystatechange = function() {
//       if (this.readyState == 4 && this.status == 200) {
//           var data = JSON.parse(this.responseText);
//           var tableBody = document.getElementById("tableBody");
//           tableBody.innerHTML = ""; // Clear existing data
//           data.forEach(function(student, index) {
//               var newRow = tableBody.insertRow();
//               newRow.insertCell(0).textContent = index + 1;
//               newRow.insertCell(1).textContent = student.rollNumber;
//               newRow.insertCell(2).textContent = student.name;
//           });
//       }
//   };
//   xhr.open("GET", "/get_data/", true);
//   xhr.send();
// }

// Call fetchData function when the page loads
// window.onload = fetchData;


var students = [

];

// function populateTable() {
// var tableBody = document.getElementById("tableBody");
// tableBody.innerHTML = "";
// students.forEach(function(student, index) {
//     var newRow = tableBody.insertRow();
//     newRow.insertCell(0).textContent = index+1;
//     newRow.insertCell(1).textContent = student.rollNumber;
//     newRow.insertCell(2).textContent = student.name;
// });
// }

// window.onload = populateTable;

function addRow() {
  var rollNumber = prompt("Enter Roll Number:");
  if (rollNumber) {
      var existingRollNumbers = students.map(student => student.RN);
      if (existingRollNumbers.includes(rollNumber)) {
          alert("Roll Number already exists!");
          return;
      }

      // Fetch details from the pd table based on the roll number
      var xhr = new XMLHttpRequest();
      xhr.onreadystatechange = function() {
          if (this.readyState == 4) {
              if (this.status == 200) {
                  var studentDetails = JSON.parse(this.responseText);
                  if (studentDetails.rollNumber) {
                      var tableBody = document.getElementById("tableBody");
                      var newRow = tableBody.insertRow();
                      newRow.insertCell(0).textContent = students.length + 1;
                      newRow.insertCell(1).textContent = studentDetails.rollNumber;
                      newRow.insertCell(2).textContent = studentDetails.name;
                      students.push({ rollNumber: studentDetails.rollNumber });

                      // Set rollNumber and name in hidden input fields
                      document.getElementById("hiddenRollNumber").value = studentDetails.rollNumber;
                      document.getElementById("hiddenName").value = studentDetails.name;

                      // Call saveTableData() to save the data
                      saveTableData();
                  } else {
                      alert("Student details not found for the provided roll number.");
                  }
              } else {
                  alert("Error fetching student details. Status code: " + this.status);
              }
          }
      };
      xhr.open("GET", "/get_data/?rollNumber=" + rollNumber, true);
      xhr.send();
  } else {
      alert("Roll Number is required.");
  }
}



function saveTableData() {
  // event.preventDefault()
  // Get roll number and name from hidden input fields
  console.log("Hidden Roll Number:", document.getElementById('hiddenRollNumber').value);
console.log("Hidden Name:", document.getElementById('hiddenName').value);

  var rollNumber = document.getElementById('hiddenRollNumber').value;
  var name = document.getElementById('hiddenName').value;

  // Check if roll number and name are not empty
  if (!rollNumber || !name) {
      console.error("Roll number and name are required fields.");
      return;
  }

  // Create JSON object with roll number and name
  var jsonData = {
      rollNumber: rollNumber,
      name: name
  };

  // Log the data being sent
  console.log("Data being sent to server:", jsonData);

  // Get CSRF token
  var csrfToken = getCSRFToken();

  // Send a POST request to save the student data
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
      if (this.readyState === 4) {
          if (this.status === 200) {
              console.log("Student data saved successfully.");
          } else {
              console.error("Failed to save student data:", this.responseText);
          }
      }
  };
  xhr.open("POST", "/save_table_data/", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.setRequestHeader("X-CSRFToken", csrfToken); // Include CSRF token in request headers
  xhr.send(JSON.stringify(jsonData));
}


// Function to get CSRF token from cookies
function getCSRFToken() {
  var csrfToken = null;
  var cookies = document.cookie.split("; ");
  cookies.forEach(function(cookie) {
      var parts = cookie.split("=");
      if (parts[0] === "csrftoken") {
          csrfToken = decodeURIComponent(parts[1]);
      }
  });
  return csrfToken;
}


function deleteStudent(rollNumber) {
    if (confirm("Are you sure you want to delete this student?")) {
        // Get the delete URL from the data attribute
        var deleteUrl = event.target.dataset.deleteUrl;
        
        // Create a new XMLHttpRequest object
        var xhr = new XMLHttpRequest();
        
        // Set up the request
        xhr.open("POST", deleteUrl, true);
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.setRequestHeader("X-CSRFToken", getCSRFToken());
        
        // Define what happens on successful data submission
        xhr.onload = function () {
            if (xhr.status === 200) {
                // If successful, reload the page to reflect the changes
                location.reload();
            } else {
                // If not successful, show an error message
                alert('Error deleting student: ' + xhr.responseText);
            }
        };

        // Define what happens in case of an error
        xhr.onerror = function () {
            alert('Request failed');
        };

        // Encode roll number as part of the request body
        var formData = "rollNumber=" + encodeURIComponent(rollNumber);
        
        // Send the request with the encoded roll number as the data
        xhr.send(formData);
    }
}





// function searchTable() {
// // Declare variables
// var input, filter, table, tr, td, i, txtValue;
// input = document.getElementById("searchInput");
// filter = input.value.toUpperCase();
// table = document.getElementById("myTable");
// tr = table.getElementsByTagName("tr");

// // Loop through all table rows, and hide those who don't match the search query
// for (i = 0; i < tr.length; i++) {
//     td = tr[i].getElementsByTagName("td")[2]; // Assuming the name of the student is in the third column (index 2)
//     if (td) {
//         txtValue = td.textContent || td.innerText;
//         if (txtValue.toUpperCase().indexOf(filter) > -1) {
//             tr[i].style.display = "";
//         } else {
//             tr[i].style.display = "none";
//         }
//     }
// }
// }