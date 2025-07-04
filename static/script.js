const BASE_URL = "http://localhost:5000";

// Add Student
async function addStudent() {
  const name = document.getElementById("name").value;
  const mark = parseInt(document.getElementById("mark").value);
  const response = await fetch(`${BASE_URL}/addStudent`, {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ name, mark })
  });
  const data = await response.json();
  alert(data.Message);
  fetchStudents();  // Refresh list
}

// Update Student
async function updateStudent() {
  const id = parseInt(document.getElementById("update-id").value);
  const name = document.getElementById("update-name").value;
  const mark = parseInt(document.getElementById("update-mark").value);

  const response = await fetch(`${BASE_URL}/update`, {
    method: "PUT",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ id, name, mark })
  });
  const data = await response.json();
  alert(data.message);
  fetchStudents();  // Refresh list
}

// Fetch All Students
async function fetchStudents() {
  const response = await fetch(`${BASE_URL}/fetchAll`);
  const students = await response.json();

  const list = document.getElementById("student-list");
  list.innerHTML = "";  // Clear old list

  students.forEach(student => {
    const item = document.createElement("li");
    item.className = "list-group-item";
    item.textContent = `ID: ${student.id}, Name: ${student.name}, Mark: ${student.mark}`;
    list.appendChild(item);
  });
}

// Delete Student
async function deleteStudent() {
  const id = parseInt(document.getElementById("delete-id").value);
  const response = await fetch(`${BASE_URL}/delete/${id}`, {
    method: "DELETE"
  });
  const data = await response.json();
  alert(data.message);
  fetchStudents();  // Refresh list
}
