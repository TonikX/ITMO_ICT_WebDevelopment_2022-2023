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

const getToken = () => {
    return JSON.parse(localStorage.getItem("token"));
};

export const fetchFromBackendApi = async (pathSegments = [], dropToken = false) => {
    const path = pathSegments.join("/");
    const token = dropToken ? null : getToken();

    const res = await fetch(`${window.location.origin}/${path}`, {
        method: "GET",
        mode: "cors",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",

            // For djago session auth
            "X-CSRFToken": getCookie("csrftoken"),
            // For djago token auth
            ...(token && { Authorization: `Token ${token}` }),
        },
    });
    if (!res.ok) throw new Error(res.statusText);
    return { json: await res.json(), ok: res.ok };
};

export const pushToBackendApi = async (
    pathSegments = [],
    method = "POST",
    body = {},
    dropToken = false
) => {
    let path = pathSegments.join("/");
    if (method === "POST") path += "/";
    const token = dropToken ? null : getToken();

    const res = await fetch(`${window.location.origin}/${path}`, {
        method,
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",

            // For djago session auth
            "X-CSRFToken": getCookie("csrftoken"),
            // For djago token auth
            ...(token && { Authorization: `Token ${token}` }),
        },
        credentials: "same-origin",
        body: JSON.stringify(body),
    });

    console.log("backend push response", res);

    // Handle empty responses
    if (res.status === 204) return { json: {}, ok: res.ok };
    return { json: await res.json(), ok: res.ok };
};

// Auth API
export const fetchLogin = async () => await fetchFromBackendApi(["auth", "users", "me"]);
export const postLogin = async ({ username, password }) =>
    await pushToBackendApi(["auth", "token", "login"], "POST", { username, password }, true);
export const postLogout = async () => await pushToBackendApi(["auth", "token", "logout"], "POST");

// Models API
export const fetchUsers = async () => {
    console.log("getToken", getToken());
    return await fetchFromBackendApi(["api", "users"]);
};
export const fetchUserDetails = async ({ userId }) =>
    await fetchFromBackendApi(["api", "user", userId]);

export const postUsers = async ({ body }) => await pushToBackendApi(["api", "users"], "POST", body);
export const patchUserDetails = async ({ userId, body }) =>
    await pushToBackendApi(["api", "user", userId], "PATCH", body);
export const deleteUserDetails = async ({ userId }) =>
    await pushToBackendApi(["api", "user", userId], "DELETE");

export const fetchLibraries = async () => await fetchFromBackendApi(["api", "libraries"]);
export const fetchLibraryDetails = async ({ libraryId }) =>
    await fetchFromBackendApi(["api", "library", libraryId]);

export const postLibraries = async ({ body }) =>
    await pushToBackendApi(["api", "libraries"], "POST", body);
export const patchLibraryDetails = async ({ libraryId, body }) =>
    await pushToBackendApi(["api", "library", libraryId], "PATCH", body);
export const deleteLibraryDetails = async ({ libraryId }) =>
    await pushToBackendApi(["api", "library", libraryId], "DELETE");

export const fetchReadingRooms = async () => await fetchFromBackendApi(["api", "reading-rooms"]);
export const fetchReadingRoomDetails = async ({ readingRoomId }) =>
    await fetchFromBackendApi(["api", "reading-room", readingRoomId]);

export const postReadingRooms = async ({ body }) =>
    await pushToBackendApi(["api", "reading-rooms"], "POST", body);
export const patchReadingRoomDetails = async ({ readingRoomId, body }) =>
    await pushToBackendApi(["api", "reading-room", readingRoomId], "PATCH", body);
export const deleteReadingRoomDetails = async ({ readingRoomId }) =>
    await pushToBackendApi(["api", "reading-room", readingRoomId], "DELETE");

export const fetchBooks = async () => await fetchFromBackendApi(["api", "books"]);
export const fetchBookDetails = async ({ bookId }) =>
    await fetchFromBackendApi(["api", "book", bookId]);

export const postBooks = async ({ body }) => await pushToBackendApi(["api", "books"], "POST", body);
export const patchBookDetails = async ({ bookId, body }) =>
    await pushToBackendApi(["api", "book", bookId], "PATCH", body);
export const deleteBookDetails = async ({ bookId }) =>
    await pushToBackendApi(["api", "book", bookId], "DELETE");

export const fetchReadingRoomBooks = async () =>
    await fetchFromBackendApi(["api", "reading-room-books"]);
export const fetchReadingRoomBookDetails = async ({ readingRoomBookId }) =>
    await fetchFromBackendApi(["api", "reading-room-book", readingRoomBookId]);

export const postReadingRoomBooks = async ({ body }) =>
    await pushToBackendApi(["api", "reading-room-books"], "POST", body);
export const patchReadingRoomBookDetails = async ({ readingRoomBookId, body }) =>
    await pushToBackendApi(["api", "reading-room-book", readingRoomBookId], "PATCH", body);
export const deleteReadingRoomBookDetails = async ({ readingRoomBookId }) =>
    await pushToBackendApi(["api", "reading-room-book", readingRoomBookId], "DELETE");

export const fetchReadingRoomBookUsers = async () =>
    await fetchFromBackendApi(["api", "reading-room-book-users"]);
export const fetchReadingRoomBookUserDetails = async ({ readingRoomBookUserId }) =>
    await fetchFromBackendApi(["api", "reading-room-book-user", readingRoomBookUserId]);

export const postReadingRoomBookUsers = async ({ body }) =>
    await pushToBackendApi(["api", "reading-room-book-users"], "POST", body);
export const patchReadingRoomBookUserDetails = async ({ readingRoomBookUserId, body }) =>
    await pushToBackendApi(["api", "reading-room-book-user", readingRoomBookUserId], "PATCH", body);
export const deleteReadingRoomBookUserDetails = async ({ readingRoomBookUserId }) =>
    await pushToBackendApi(["api", "reading-room-book-user", readingRoomBookUserId], "DELETE");

// Custom API
export const fetchUserBooks = async ({ userId }) =>
    await fetchFromBackendApi(["api", "user-books", userId]);
export const fetchUsersBooksOverdue = async () =>
    await fetchFromBackendApi(["api", "users-books-overdue"]);
export const fetchUsersBooksRare = async () =>
    await fetchFromBackendApi(["api", "users-books-rare"]);
export const fetchUsersYoung = async () => await fetchFromBackendApi(["api", "users-young"]);
export const fetchUsersGroupedByDegree = async () =>
    await fetchFromBackendApi(["api", "users-degree"]);

// Report API
export const fetchLibraryMonthlyReport = async ({ libraryId }) =>
    await fetchFromBackendApi(["api", "library-monthly-report", libraryId]);
export const fetchLibraryMonthlyReportDate = async ({ libraryId, year, month }) =>
    await fetchFromBackendApi(["api", "library-monthly-report", libraryId, year, month]);

const backendApi = {
    fetchFromBackendApi,
    pushToBackendApi,

    fetchLogin,
    postLogin,
    postLogout,

    fetchUsers,
    fetchUserDetails,
    postUsers,
    patchUserDetails,
    deleteUserDetails,

    fetchLibraries,
    fetchLibraryDetails,
    postLibraries,
    patchLibraryDetails,
    deleteLibraryDetails,

    fetchReadingRooms,
    fetchReadingRoomDetails,
    postReadingRooms,
    patchReadingRoomDetails,
    deleteReadingRoomDetails,

    fetchBooks,
    fetchBookDetails,
    postBooks,
    patchBookDetails,
    deleteBookDetails,

    fetchReadingRoomBooks,
    fetchReadingRoomBookDetails,
    postReadingRoomBooks,
    patchReadingRoomBookDetails,
    deleteReadingRoomBookDetails,

    fetchReadingRoomBookUsers,
    fetchReadingRoomBookUserDetails,
    postReadingRoomBookUsers,
    patchReadingRoomBookUserDetails,
    deleteReadingRoomBookUserDetails,

    fetchUserBooks,
    fetchUsersBooksOverdue,
    fetchUsersBooksRare,
    fetchUsersYoung,
    fetchUsersGroupedByDegree,

    fetchLibraryMonthlyReport,
    fetchLibraryMonthlyReportDate,
};

export default backendApi;
