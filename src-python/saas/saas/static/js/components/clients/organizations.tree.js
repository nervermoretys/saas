'use strict';

class OrganizationTree extends HTMLElement {
    
    constructor() {
        const self = super();

        const style = document.createElement("link");
        style.setAttribute('rel', 'stylesheet');
        style.setAttribute('href', '/static/css/clients/organization.tree.css');

        const container = document.createElement('div');
        container.classList.add('component-wrapper');

        this.init(self, container);

        const shadow = this.attachShadow({ mode: 'open' });
        shadow.appendChild(style);
        shadow.appendChild(container);

        this.setOrganizations = this.setOrganizations.bind(this);
    }

    init(component, container) {
        const ths = [];
        ths.push(`<th class="col-name">Name</th>`);
        ths.push(`<th class="col-description">Description</th>`);
        const thall = ths.join('');

        const div = document.createElement('div');
        div.classList.add('wrapper-tree');
        div.innerHTML = `
            <table class="tbl-organizations" role="treegrid" aria-label="Organizational Chart">
                <caption>Organizational Chart</caption>
                <colgroup>
                    <col id="col1">
                </colgroup>
                <thead>
                    <tr>
                        ${thall}
                    </tr>
                </thead>
                <tbody>
                </tbody>
                <tfoot>
                </tfoot>
            </table>
        `

        container.appendChild(div);
    }

    setOrganizations(organizations = []) {
        const self = this;
        const shadow = this.shadowRoot;
        const tbody = shadow.querySelector('table.tbl-organizations tbody');
        while(tbody.firstChild) {
            tbody.removeChild(tbody.lastChild);
        }
        organizations.forEach(o => {
            const tds = [];
            tds.push(`<td class="col-name"><span>${o.name}</span></td>`);
            tds.push(`<td class="col-description"><span>${o.description}</span></td>`);
            const tdall = tds.join('');

            const tr = document.createElement('tr');
            tr.classList.add('row-org');
            tr.innerHTML = `
                ${tdall}
            `;

            tbody.appendChild(tr);
        });
    }
}
customElements.define('organization-tree', OrganizationTree);
export { OrganizationTree };