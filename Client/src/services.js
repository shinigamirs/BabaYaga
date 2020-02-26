export async function fetchUserFromId(userId) {
  const response = await fetch("https://babayaga.corp.coriolis.in:8086/" + userId, {
    method: "GET",
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
      accept: "application/json"
    },
//    body: JSON.stringify({
//      id: userId,
//    }),
  });

  return response.json();
}


export async function logoutUser(userId) {
  const response = await fetch("https://babayaga.corp.coriolis.in:8086/unauth", {
    method: "POST",
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
      accept: "application/json"
    },
    body: JSON.stringify({
      id: userId,
    }),
  });

  return response.json();
}

export async function issueBook(userId, bookId) {
  const response = await fetch("https://babayaga.corp.coriolis.in:8086/issue", {
    method: "POST",
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
      accept: "application/json"
    },
    body: JSON.stringify({
      emp_id: userId,
      isbn: bookId,
    }),
  });

  return response.json();
}

export async function returnBook(userId, bookId) {
  const response = await fetch("https://babayaga.corp.coriolis.in:8086/return", {
    method: "POST",
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
      accept: "application/json"
    },
    body: JSON.stringify({
      emp_id: userId,
      isbn: bookId,
    }),
  });

  return response.json();
}