export const fetchFromBackendAPI = async (...pathSegments) => {
    const path = pathSegments.join("/");
    const res = await fetch(`http://127.0.0.1:${backendPort}/api/${path}`, {
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
    });
    return res.json();
};

// Models API
export const fetchUsers = async () => await fetchFromBackendAPI("users");
export const fetchUserDetails = async (userId) => await fetchFromBackendAPI("user", userId);

export const fetchLibraries = async () => await fetchFromBackendAPI("libraries");
export const fetchLibraryDetails = async (libraryId) =>
    await fetchFromBackendAPI("user", libraryId);

export const fetchReadingRooms = async () => await fetchFromBackendAPI("reading-rooms");
export const fetchReadingRoomDetails = async (readingRoomId) =>
    await fetchFromBackendAPI("reading-room", readingRoomId);

export const fetchBooks = async () => await fetchFromBackendAPI("books");
export const fetchBookDetails = async (bookId) => await fetchFromBackendAPI("book", bookId);

export const fetchReadingRoomBooks = async () => await fetchFromBackendAPI("reading-room-books");
export const fetchReadingRoomBookDetails = async (id) =>
    await fetchFromBackendAPI("reading-room-book", id);

export const fetchReadingRoomBookUsers = async () =>
    await fetchFromBackendAPI("reading-room-book-users");
export const fetchReadingRoomBookUserDetails = async (id) =>
    await fetchFromBackendAPI("reading-room-book-users", id);

// Custom API
export const fetchUserBooks = async (userId) => await fetchFromBackendAPI("user-books", userId);

export const fetchUsersBooksOverdue = async () => await fetchFromBackendAPI("users-books-overdue");

export const fetchUsersBooksRare = async () => await fetchFromBackendAPI("users-books-rare");

export const fetchUsersYoung = async () => await fetchFromBackendAPI("users-young");

export const fetchUsersGroupedByDegree = async () => await fetchFromBackendAPI("users-degree");

// Report API
export const fetchLibraryMonthlyReport = async (libraryId) =>
    await fetchFromBackendAPI("library-monthly-report", libraryId);
export const fetchLibraryMonthlyReportDate = async (libraryId, year, month) =>
    await fetchFromBackendAPI("library-monthly-report", libraryId, year, month);

const backendApi = {
    fetchUsers,
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
