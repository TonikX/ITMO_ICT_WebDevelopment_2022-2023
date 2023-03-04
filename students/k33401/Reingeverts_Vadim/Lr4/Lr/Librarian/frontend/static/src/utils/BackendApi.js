// https://stackoverflow.com/a/43943556
const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let cookie of cookies) {
            cookie = cookie.trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

export const fetchFromBackendApi = async (pathSegments = [], token = "") => {
    const path = pathSegments.join("/");

    const res = await fetch(`${window.location.origin}/api/${path}`, {
        method: "GET",
        mode: "cors",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",

            "X-CSRFToken": getCookie("csrftoken"),
            Authorization: `Token ${token}`,
        },
    });
    if (!res.ok) throw new Error(res.statusText);

    return await res.json();
};

export const pushToBackendApi = async (
    pathSegments = [],
    method = "POST",
    token = "",
    body = {}
) => {
    let path = pathSegments.join("/");
    if (method === "POST") path += "/";

    const res = await fetch(`${window.location.origin}/api/${path}`, {
        method,
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",

            "X-CSRFToken": getCookie("csrftoken"),
            Authorization: `Token ${token}`,
        },
        credentials: "same-origin",
        body: JSON.stringify(body),
    });
    if (!res.ok) throw new Error(res.statusText);

    return await res.json();
};

// Models API
export const fetchUsers = async ({ token }) => await fetchFromBackendApi(["users"], token);
export const fetchUserDetails = async ({ userId, token }) =>
    await fetchFromBackendApi(["user", userId], token);

export const postUsers = async ({ token, body }) =>
    await pushToBackendApi(["users"], "POST", token, body);

export const patchUserDetails = async ({ userId, token, body }) =>
    await pushToBackendApi(["user", userId], "PATCH", token, body);

export const deleteUserDetails = async ({ userId, token }) =>
    await pushToBackendApi(["user", userId], "DELETE", token);

export const fetchLibraries = async ({ token }) => await fetchFromBackendApi(["libraries"], token);
export const fetchLibraryDetails = async ({ libraryId, token }) =>
    await fetchFromBackendApi(["user", libraryId], token);

export const fetchReadingRooms = async ({ token }) =>
    await fetchFromBackendApi(["reading-rooms"], token);
export const fetchReadingRoomDetails = async ({ readingRoomId, token }) =>
    await fetchFromBackendApi(["reading-room", readingRoomId], token);

export const fetchBooks = async ({ token }) => await fetchFromBackendApi(["books"], token);
export const fetchBookDetails = async ({ bookId, token }) =>
    await fetchFromBackendApi(["book", bookId], token);

export const fetchReadingRoomBooks = async ({ token }) =>
    await fetchFromBackendApi(["reading-room-books"], token);
export const fetchReadingRoomBookDetails = async ({ readingRoomBookId, token }) =>
    await fetchFromBackendApi(["reading-room-book", readingRoomBookId], token);

export const fetchReadingRoomBookUsers = async ({ token }) =>
    await fetchFromBackendApi(["reading-room-book-users"], token);
export const fetchReadingRoomBookUserDetails = async ({ readingRoomBookUserId, token }) =>
    await fetchFromBackendApi(["reading-room-book-users", readingRoomBookUserId], token);

// Custom API
export const fetchUserBooks = async ({ userId, token }) =>
    await fetchFromBackendApi(["user-books", userId], token);

export const fetchUsersBooksOverdue = async ({ token }) =>
    await fetchFromBackendApi(["users-books-overdue"], token);

export const fetchUsersBooksRare = async ({ token }) =>
    await fetchFromBackendApi(["users-books-rare"], token);

export const fetchUsersYoung = async ({ token }) =>
    await fetchFromBackendApi(["users-young"], token);

export const fetchUsersGroupedByDegree = async ({ token }) =>
    await fetchFromBackendApi(["users-degree"], token);

// Report API
export const fetchLibraryMonthlyReport = async ({ libraryId, token }) =>
    await fetchFromBackendApi(["library-monthly-report", libraryId], token);
export const fetchLibraryMonthlyReportDate = async ({ libraryId, year, month, token }) =>
    await fetchFromBackendApi(["library-monthly-report", libraryId, year, month], token);

const backendApi = {
    fetchFromBackendApi,
    fetchUsers,
    postUsers,
    patchUserDetails,
    deleteUserDetails,
    fetchUserDetails,
    fetchLibraries,
    fetchLibraryDetails,
    fetchReadingRooms,
    fetchReadingRoomDetails,
    fetchBooks,
    fetchBookDetails,
    fetchReadingRoomBooks,
    fetchReadingRoomBookDetails,
    fetchReadingRoomBookUsers,
    fetchReadingRoomBookUserDetails,
    fetchUserBooks,
    fetchUsersBooksOverdue,
    fetchUsersBooksRare,
    fetchUsersYoung,
    fetchUsersGroupedByDegree,
    fetchLibraryMonthlyReport,
    fetchLibraryMonthlyReportDate,
};

export default backendApi;
