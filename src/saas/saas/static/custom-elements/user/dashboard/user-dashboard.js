'use strict';
class UserDashboard extends HTMLElement {

    constructor() {
        const self = super();

        const style = document.createElement("link");
        style.setAttribute('rel', 'stylesheet');
        style.setAttribute('href', '/static/custom-elements/user/dashboard/user-dashboard.css');

        const default_style = document.createElement("link");
        default_style.setAttribute('rel', 'stylesheet');
        default_style.setAttribute('href', '/static/css/default.css');

        const div = document.createElement('div');
        div.classList.add('component-wrapper');

        this._init(div);

        const shadow = this.attachShadow({ mode: 'open' });
        shadow.appendChild(style);
        shadow.appendChild(default_style);
        shadow.appendChild(div);

        this._attachEventHandlers = this._attachEventHandlers.bind(this);
        this.refresh = this.refresh.bind(this);
    }

    _init(container) {
        const div = document.createElement('div');
        div.innerHTML = `
            <div class="toolbar" role="toolbar">
                <button type="button" id="btn-refresh" class="btn btn-refresh" title="Refresh">
                    <span class="material-icons">refresh</span>
                </button>
            </div><!-- .toolbar -->
            <div class="messages-wrapper">
                <h6>Messages</h6>
                <p>reminders and system messages should go here</p>
                <user-messages></user-messages>
            </div><!-- .messages-wrapper -->
        `;

        container.appendChild(div);
    }

    _attachEventHandlers() {
        const self = this;
        const shadow = this.shadowRoot;

        shadow.getElementById('btn-refresh').addEventListener('click', function() {
            self.refresh();
        });
    }

    refresh() {
        const self = this;
        const shadow = this.shadowRoot;

        const btnrefresh = shadow.getElementById('btn-refresh');
        btnrefresh.disabled = True;
        // do stuff
        btnrefresh.disabled = False;
    }
}
customElements.define('user-dashboard', UserDashboard);