// function exportToPDF() {
//     var doc = new jsPDF();
//     doc.text("Report", 10, 10); // Add a title

//     // Convert table to canvas and add it to PDF
//     var table = document.querySelector("table");
//     var canvas = document.createElement("canvas");
//     canvas.width = table.offsetWidth;
//     canvas.height = table.offsetHeight;
//     var context = canvas.getContext("2d");
//     var rows = table.querySelectorAll("tr");
//     var imageData;
//     rows.forEach(function(row, index) {
//         var y = index * row.offsetHeight;
//         context.drawImage(row, 0, y, row.offsetWidth, row.offsetHeight);
//     });
//     imageData = canvas.toDataURL("image/jpeg", 1.0);
//     doc.addImage(imageData, "JPEG", 10, 20);

//     // Save the PDF
//     doc.save("report.pdf");
// }

// document.getElementById("fileInput").addEventListener("change", function(event) {
//     var file = event.target.files[0];
//     var reader = new FileReader();
//     reader.onload = function(event) {
//         var imageUrl = event.target.result;
//         var img = document.createElement("img");
//         img.src = imageUrl;
//         document.getElementById("preview").innerHTML = "";
//         document.getElementById("preview").appendChild(img);
//     };
//     reader.readAsDataURL(file);
// });


// function genpdf(pa){
//     var b = document.body.innerHTML;
//     var d = document.getElementById(pa).innerHTML;
//     document.body.innerHTML = d;
//     window.print();
// }


// document.addEventListener('DOMContentLoaded', function() {
//     document.getElementById('fileInput1').addEventListener('change', function(event) {
//         var file = event.target.files[0];
//         var reader = new FileReader();
//         reader.onload = function(e) {
//             document.getElementById('preview1').innerHTML = '<img src="' + e.target.result + '" alt="Image 1">';
//         };
//         reader.readAsDataURL(file);
//     });

//     document.getElementById('fileInput2').addEventListener('change', function(event) {
//         var file = event.target.files[0];
//         var reader = new FileReader();
//         reader.onload = function(e) {
//             document.getElementById('preview2').innerHTML = '<img src="' + e.target.result + '" alt="Image 2">';
//         };
//         reader.readAsDataURL(file);
//     });
// });


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
     
$(document).ready(function(){
$('[data-toggle="tooltip"]').tooltip();
});



// function exportToPDF() {
//     var doc = new jsPDF();
//     doc.text("Report", 10, 10); // Add a title

//     // Convert table to canvas and add it to PDF
//     var table = document.querySelector("table");
//     var canvas = document.createElement("canvas");
//     canvas.width = table.offsetWidth;
//     canvas.height = table.offsetHeight;
//     var context = canvas.getContext("2d");
//     var rows = table.querySelectorAll("tr");
//     var imageData;
//     rows.forEach(function(row, index) {
//         var y = index * row.offsetHeight;
//         context.drawImage(row, 0, y, row.offsetWidth, row.offsetHeight);
//     });
//     imageData = canvas.toDataURL("image/jpeg", 1.0);
//     doc.addImage(imageData, "JPEG", 10, 20);

//     // Save the PDF
//     doc.save("report.pdf");
// }
// document.getElementById("fileInput").addEventListener("change", function(event) {
//     var file = event.target.files[0];
//     var reader = new FileReader();
//     reader.onload = function(event) {
//         var imageUrl = event.target.result;
//         var img = document.createElement("img");
//         img.src = imageUrl;
//         document.getElementById("preview").innerHTML = "";
//         document.getElementById("preview").appendChild(img);
//     };
//     reader.readAsDataURL(file);
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

// function saveTableData() {
//   var table = document.getElementById("myTable");
//   var data = [];
//   for (var i = 1; i < table.rows.length; i++) {
//       var rowData = [];
//       for (var j = 0; j < table.rows[i].cells.length - 1; j++) {
//           rowData.push(table.rows[i].cells[j].innerHTML);
//       }
//       data.push(rowData);
//   }
//   // Here you can perform actions like saving the data to a database or displaying it to the user
//   console.log(data);
//   alert("Data saved!");
// }
//     function searchTable() {
//       var input, filter, table, tr, td, i, txtValue;
//       input = document.getElementById("searchInput");
//       filter = input.value.toUpperCase();
//       table = document.getElementById("myTable");
//       tr = table.getElementsByTagName("tr");
//       for (i = 0; i < tr.length; i++) {
//           td = tr[i].getElementsByTagName("td")[0];
//           if (td) {
//               txtValue = td.textContent || td.innerText;
//               if (txtValue.toUpperCase().indexOf(filter) > -1) {
//                   tr[i].style.display = "";
//               } else {
//                   tr[i].style.display = "none";
//               }
//           }
//       }
//   }


