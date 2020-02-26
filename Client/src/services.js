export async function fetchUserFromId(userId) {
  const response = await fetch("https://babayaga.free.beeceptor.com/auth", {
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


export async function logoutUser(userId) {
  const response = await fetch("https://babayaga.free.beeceptor.com/unauth", {
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
  const response = await fetch("https://babayaga.free.beeceptor.com/issue", {
    method: "POST",
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
      accept: "application/json"
    },
    body: JSON.stringify({
      userId,
      bookId,
    }),
  });

  return response.json();
}

export async function returnBook(userId, bookId) {
  const response = await fetch("https://babayaga.free.beeceptor.com/return", {
    method: "POST",
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
      accept: "application/json"
    },
    body: JSON.stringify({
      userId,
      bookId,
    }),
  });

  return response.json();
}