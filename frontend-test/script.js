const API_BASE = 'http://127.0.0.1:8000/api';

async function fetchData(endpoint, containerId, renderFn) {
    const container = document.getElementById(containerId);
    if (!container) return;

    try {
        const response = await fetch(`${API_BASE}${endpoint}`);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();
        data.forEach(item => renderFn(container, item));
    } catch (error) {
        console.error(`Error fetching from ${endpoint}:`, error);
        container.innerHTML = '<p class="error">Failed to load data. Check if the backend is running.</p>';
    }
}

function renderServiceCard(container, service) {
    const card = document.createElement('div');
    card.className = 'card';
    card.innerHTML = `
        <h3>${service.title}</h3>
        <p>${service.short_description}</p>
    `;
    container.appendChild(card);
}

function renderPortfolioCard(container, project) {
    const card = document.createElement('div');
    card.className = 'card';
    card.innerHTML = `
        <h3>${project.title}</h3>
        <span class="category">${project.category}</span>
        <p>${project.short_description}</p>
    `;
    container.appendChild(card);
}

function renderTeamCard(container, member) {
    const card = document.createElement('div');
    card.className = 'card';
    card.innerHTML = `
        <h3>${member.name}</h3>
        <p class="role">${member.role}</p>
    `;
    container.appendChild(card);
}

async function handleFormSubmit(e) {
    e.preventDefault();
    const form = e.target;
    const statusEl = document.getElementById('form-status');
    const submitBtn = form.querySelector('button[type="submit"]');

    const formData = {
        name: form.name.value,
        email: form.email.value,
        subject: form.subject.value,
        message: form.message.value,
        inquiry_type: 'contact'
    };

    try {
        submitBtn.disabled = true;
        statusEl.textContent = 'Sending...';
        statusEl.className = 'status loading';

        const response = await fetch(`${API_BASE}/inquiries/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        
        statusEl.textContent = 'Submitted!';
        statusEl.className = 'status success';
        form.reset();
    } catch (error) {
        console.error('Error submitting form:', error);
        statusEl.textContent = 'Error submitting';
        statusEl.className = 'status error';
    } finally {
        submitBtn.disabled = false;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    fetchData('/services/', 'services-list', renderServiceCard);
    fetchData('/portfolio/', 'portfolio-list', renderPortfolioCard);
    fetchData('/team/', 'team-list', renderTeamCard);

    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', handleFormSubmit);
    }
});