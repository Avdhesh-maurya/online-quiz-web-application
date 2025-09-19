/**
 * Session Timeout Handler
 * Handles client-side session timeout warnings and automatic logout
 */

class SessionTimeoutHandler {
    constructor(options = {}) {
        this.sessionTimeout = options.sessionTimeout || 1800000; // 30 minutes in milliseconds
        this.warningTime = options.warningTime || 300000; // 5 minutes warning in milliseconds
        this.checkInterval = options.checkInterval || 30000; // Check every 30 seconds

        this.warningTimer = null;
        this.logoutTimer = null;
        this.checkTimer = null;
        this.lastActivity = Date.now();

        this.init();
    }

    init() {
        this.createWarningModal();
        this.bindEvents();
        this.startTimers();
    }

    createWarningModal() {
        // Create session timeout warning modal
        const modalHTML = `
            <div class="modal fade" id="sessionTimeoutModal" tabindex="-1" aria-labelledby="sessionTimeoutModalLabel" aria-hidden="true" data-bs-backdrop="static" data-bs-keyboard="false">
                <div class="modal-dialog modal-dialog-centered">
                    <div class="modal-content">
                        <div class="modal-header bg-warning text-dark">
                            <h5 class="modal-title" id="sessionTimeoutModalLabel">
                                <i class="fas fa-exclamation-triangle"></i> Session Timeout Warning
                            </h5>
                        </div>
                        <div class="modal-body">
                            <p>Your session will expire in <span id="countdown" class="fw-bold text-danger">5:00</span> minutes due to inactivity.</p>
                            <p>Click "Stay Logged In" to continue your session or you will be automatically logged out.</p>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-primary" id="stayLoggedInBtn">
                                <i class="fas fa-user-check"></i> Stay Logged In
                            </button>
                            <button type="button" class="btn btn-secondary" id="logoutNowBtn">
                                <i class="fas fa-sign-out-alt"></i> Logout Now
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        `;

        // Append modal to body if it doesn't exist
        if (!document.getElementById('sessionTimeoutModal')) {
            document.body.insertAdjacentHTML('beforeend', modalHTML);
        }

        // Bind modal button events
        document.getElementById('stayLoggedInBtn').addEventListener('click', () => {
            this.extendSession();
        });

        document.getElementById('logoutNowBtn').addEventListener('click', () => {
            this.logout();
        });
    }

    bindEvents() {
        // Track user activity
        const events = ['mousedown', 'mousemove', 'keypress', 'scroll', 'touchstart', 'click'];

        events.forEach(event => {
            document.addEventListener(event, () => {
                this.updateActivity();
            }, true);
        });
    }

    updateActivity() {
        this.lastActivity = Date.now();
        this.hideWarning();
        this.resetTimers();
    }

    startTimers() {
        this.resetTimers();

        // Set warning timer
        this.warningTimer = setTimeout(() => {
            this.showWarning();
        }, this.sessionTimeout - this.warningTime);

        // Set logout timer
        this.logoutTimer = setTimeout(() => {
            this.logout();
        }, this.sessionTimeout);

        // Start periodic check
        this.checkTimer = setInterval(() => {
            this.checkSession();
        }, this.checkInterval);
    }

    resetTimers() {
        if (this.warningTimer) {
            clearTimeout(this.warningTimer);
        }
        if (this.logoutTimer) {
            clearTimeout(this.logoutTimer);
        }
        if (this.checkTimer) {
            clearInterval(this.checkTimer);
        }

        this.startTimers();
    }

    showWarning() {
        const modal = new bootstrap.Modal(document.getElementById('sessionTimeoutModal'));
        modal.show();

        // Start countdown
        this.startCountdown();
    }

    hideWarning() {
        const modalElement = document.getElementById('sessionTimeoutModal');
        const modal = bootstrap.Modal.getInstance(modalElement);
        if (modal) {
            modal.hide();
        }
    }

    startCountdown() {
        const countdownElement = document.getElementById('countdown');
        let timeLeft = this.warningTime / 1000; // Convert to seconds

        const countdownInterval = setInterval(() => {
            const minutes = Math.floor(timeLeft / 60);
            const seconds = timeLeft % 60;
            countdownElement.textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;

            timeLeft--;

            if (timeLeft < 0) {
                clearInterval(countdownInterval);
            }
        }, 1000);
    }

    extendSession() {
        // Make AJAX request to extend session
        fetch('/extend-session/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': this.getCSRFToken(),
                'Content-Type': 'application/json',
            },
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    this.updateActivity();
                    this.hideWarning();
                    this.showToast('Session extended successfully!', 'success');
                } else {
                    this.logout();
                }
            })
            .catch(error => {
                console.error('Error extending session:', error);
                this.logout();
            });
    }

    checkSession() {
        // Check if session is still valid
        fetch('/check-session/', {
            method: 'GET',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
            },
        })
            .then(response => {
                if (response.status === 401) {
                    return response.json().then(data => {
                        if (data.session_expired) {
                            this.logout(true);
                        }
                    });
                }
            })
            .catch(error => {
                console.error('Error checking session:', error);
            });
    }

    logout(sessionExpired = false) {
        // Clear all timers
        if (this.warningTimer) clearTimeout(this.warningTimer);
        if (this.logoutTimer) clearTimeout(this.logoutTimer);
        if (this.checkTimer) clearInterval(this.checkTimer);

        // Show logout message
        if (sessionExpired) {
            this.showToast('Your session has expired. Redirecting to login...', 'warning');
        } else {
            this.showToast('Logging out...', 'info');
        }

        // Redirect to logout URL
        setTimeout(() => {
            window.location.href = '/logout/';
        }, 2000);
    }

    getCSRFToken() {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            const [name, value] = cookie.trim().split('=');
            if (name === 'csrftoken') {
                return value;
            }
        }
        return '';
    }

    showToast(message, type = 'info') {
        // Create toast notification
        const toastHTML = `
            <div class="toast align-items-center text-white bg-${type === 'success' ? 'success' : type === 'warning' ? 'warning' : type === 'info' ? 'info' : 'danger'} border-0" role="alert" aria-live="assertive" aria-atomic="true">
                <div class="d-flex">
                    <div class="toast-body">
                        ${message}
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
            </div>
        `;

        // Create toast container if it doesn't exist
        let toastContainer = document.getElementById('toast-container');
        if (!toastContainer) {
            toastContainer = document.createElement('div');
            toastContainer.id = 'toast-container';
            toastContainer.className = 'toast-container position-fixed top-0 end-0 p-3';
            toastContainer.style.zIndex = '1055';
            document.body.appendChild(toastContainer);
        }

        // Add toast to container
        toastContainer.insertAdjacentHTML('beforeend', toastHTML);

        // Initialize and show toast
        const toastElement = toastContainer.lastElementChild;
        const toast = new bootstrap.Toast(toastElement);
        toast.show();

        // Remove toast after it's hidden
        toastElement.addEventListener('hidden.bs.toast', () => {
            toastElement.remove();
        });
    }
}

// Initialize session timeout handler when DOM is loaded
document.addEventListener('DOMContentLoaded', function () {
    // Only initialize if user is authenticated
    if (document.body.dataset.userAuthenticated === 'true') {
        // Get session timeout from Django settings (convert to milliseconds)
        const sessionTimeout = (parseInt(document.body.dataset.sessionTimeout) || 1800) * 1000;
        const warningTime = (parseInt(document.body.dataset.warningTime) || 300) * 1000;

        new SessionTimeoutHandler({
            sessionTimeout: sessionTimeout,
            warningTime: warningTime
        });
    }
});