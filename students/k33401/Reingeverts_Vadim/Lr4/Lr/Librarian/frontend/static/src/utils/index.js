/* Return an ISO 8601 string without timezone
 ** @param {Date} d - date to create string for
 ** @returns {string} string formatted as ISO 8601 without timezone
 */
export function toISOStringLocal(d = new Date()) {
    function z(n) {
        return (n < 10 ? "0" : "") + n;
    }
    return (
        d.getFullYear() +
        "-" +
        z(d.getMonth() + 1) +
        "-" +
        z(d.getDate()) +
        "T" +
        z(d.getHours()) +
        ":" +
        z(d.getMinutes()) +
        ":" +
        z(d.getSeconds())
    );
}
