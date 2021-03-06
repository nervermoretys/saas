'use strict';
import { notify, showInTab } from '/static/js/ui/ui.js';
import { Vendors } from '/static/js/modules/purchasing/vendors.js';
class VendorExplorer extends HTMLElement {

    constructor() {
        const self = super();
        const style = document.createElement("link");
        style.setAttribute('rel', 'stylesheet');
        style.setAttribute('href', '/static/custom-elements/purchasing/vendor-explorer/vendor-explorer.css');

        const common = document.createElement("link");
        style.setAttribute('rel', 'stylesheet');
        style.setAttribute('href', '/static/css/default.css');

        const google_web_fonts = document.createElement("link");
        google_web_fonts.setAttribute('rel', 'stylesheet');
        google_web_fonts.setAttribute('href', 'https://fonts.googleapis.com/icon?family=Material+Icons');

        const div = document.createElement('div');
        div.classList.add('component-wrapper');

        this._init(div);

        const shadow = this.attachShadow({ mode: 'open' });
        shadow.appendChild(style);
        shadow.appendChild(common);
        shadow.appendChild(google_web_fonts);
        shadow.appendChild(div);

        this._attachEventHandlers = this._attachEventHandlers.bind(this);
        this.setVendors = this.setVendors.bind(this);

        this._attachEventHandlers();
    }

    _init(container) {
        const div = document.createElement('div');
        div.classList.add('wrapper');
        div.innerHTML = `
            <div class="toolbar" role="toolbar">
                <button type="button" id="btn-new" class="btn btn-new" title="New">
                    <span class="material-icons">business</span>
                </button>
            </div><!-- .toolbar -->
            <div class="form-wrapper">
                <form id="form-filter">
                    <label for="filter">Vendor</label>
                    <input type="search" id="filter" name="filter" class="form-input-filter" title="Search" placeholder="Search Vendors" />
                    <button type="button" id="btn-filter" class="btn btn-filter" title="Search">
                        <span class="material-icons">search</span>
                    </button>
                </form>
            </div><!-- .form-wrapper -->
            <div class="table-wrapper">
                <table id="tbl-vendors">
                    <caption>Vendors</caption>
                    <colgroup>
                    </colgroup>
                    <thead>
                        <tr>
                            <th scope="col"></th>
                            <th scope="col">Name</th>
                        </tr>
                    </thead>
                    <tfoot>
                    </tfoot>
                    <tbody>
                    </tbody>
                </table>
            </div><!-- .table-wrapper -->
        `;

        container.appendChild(div);
    }

    _attachEventHandlers() {
        const self = this;
        const shadow = this.shadowRoot;

        const client_id = this.getAttribute('client-id');

        const beginsearch = function(filter) {
            Vendors.filter(client_id, filter).then((r) => {
                if (r.status == 'success') {
                    self.setVendors(r.json.vendors, filter);
                } else {
                    notify(r.status, r.message);
                }
            });
        };

        const filter = shadow.getElementById('filter');
        filter.addEventListener('keyup', function(e) {
            if (e.keyCode == 13) {
                e.preventDefault();
                beginsearch(filter.value);
            }
        });

        const btnfilter = shadow.getElementById('btn-filter');
        btnfilter.addEventListener('click', function(e) {
            beginsearch(filter.value);
        });

        const btnnew = shadow.getElementById('btn-new');
        btnnew.addEventListener('click', function(e) {
            showInTab('vendor-editor', 'New Vendor', `<vendor-editor client-id="${client_id}"></vendor-editor>`);
        });
    }

    setVendors(vendors = [], filter = '') {
        const self = this;
        const shadow = this.shadowRoot;

        const client_id = this.getAttribute('client-id');

        const tbody = shadow.querySelector('table#tbl-vendors tbody');
        while(tbody.firstChild) {
            tbody.removeChild(tbody.lastChild);
        }

        vendors.forEach((v) => {
            const vendor_name = v.name.replace(filter, `<strong>${filter}</strong>`);
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td><a class="link-edit" title="Edit Vendor" href="#" data-id="${v.id}"><span class="material-icons">edit</span></a></td>
                <td>${vendor_name}</td>
            `;

            tbody.appendChild(tr);

            // event handlers
            const edit = tr.querySelector('.link-edit');
            edit.addEventListener('click', function(e) {
                e.preventDefault();

                const vendor_id = edit.dataset.id;
                showInTab('vendor-editor', 'Edit Vendor', `<vendor-editor client-id="${client_id}" vendor-id="${vendor_id}"></vendor-editor>`)
            });
        });
    }
}
customElements.define('vendor-explorer', VendorExplorer);