// static/js/session_keepalive.js

let activityTimeout;

function resetActivityTimeout() {
    clearTimeout(activityTimeout);
    activityTimeout = setTimeout(logout, 15 * 60 * 1000);  // 30 minutes
}

function logout() {
    window.location.href = '/login/';
}

document.onload = resetActivityTimeout;
document.onmousemove = resetActivityTimeout;
document.onkeypress = resetActivityTimeout;
