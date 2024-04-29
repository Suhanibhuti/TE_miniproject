// const form = document.querySelector("form"),
//     nextBtn = form.querySelector(".nextBtn"),
//     backBtn = form.querySelector(".backBtn"),
//     allInput = form.querySelectorAll(".first input");


// nextBtn.addEventListener("click", ()=> {
// allInput.forEach(input => {
//     if(input.value != ""){
//         form.classList.add('secActive');
//     }else{
//         form.classList.remove('secActive');
//     }
// })
// })

// backBtn.addEventListener("click", () => form.classList.remove('secActive'));





// base script

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



$(document).ready(function () {
  $('[data-toggle="tooltip"]').tooltip();
});

function addRow() {
  var table = document.getElementById("myTable").getElementsByTagName('tbody')[0];
  var newRow = table.insertRow(table.rows.length);
  var cell1 = newRow.insertCell(0);
  var cell2 = newRow.insertCell(1);
  var cell3 = newRow.insertCell(2);

  cell1.innerHTML = "<input type='number' value=''>";
  cell2.innerHTML = "<input type='text' value=''>";
  cell3.innerHTML = "<input type='text' value=''>";


  deleteCell.innerHTML = "<button class='delete-btn' onclick='deleteRow(this)'>Delete</button>";
}

function saveTableData() {
  var table = document.getElementById("myTable");
  var data = [];
  for (var i = 1; i < table.rows.length; i++) {
    var rowData = [];
    for (var j = 0; j < table.rows[i].cells.length - 1; j++) {
      rowData.push(table.rows[i].cells[j].innerHTML);
    }
    data.push(rowData);
  }
  // Here you can perform actions like saving the data to a database or displaying it to the user
  console.log(data);
  alert("Data saved!");
}
function searchTable() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("searchInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

