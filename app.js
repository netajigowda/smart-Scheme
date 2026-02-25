document.addEventListener('DOMContentLoaded', async () => {
    const profileForm = document.getElementById('profile-form');
    const formSection = document.getElementById('form-section');
    const resultsSection = document.getElementById('results-section');
    const schemesList = document.getElementById('schemes-list');
    const backBtn = document.getElementById('back-btn');

    // Modal elements
    const modal = document.getElementById('scheme-modal');
    const modalBody = document.getElementById('modal-body');
    const closeModal = document.querySelector('.close-modal');

    let engine = null;

    // Load schemes data from data.js
    if (typeof SCHEMES_DATA !== 'undefined') {
        engine = new EligibilityEngine(SCHEMES_DATA);
    } else {
        console.error('SCHEMES_DATA not found.');
        alert('Data initialization failed.');
    }

    // Form Submission
    profileForm.addEventListener('submit', (e) => {
        e.preventDefault();

        if (!engine) return;

        // Simple Form Validation
        const age = document.getElementById('age').value;
        const income = document.getElementById('income').value;

        if (age < 1 || age > 110) {
            alert('Please enter a valid age between 1 and 110.');
            return;
        }

        const formData = new FormData(profileForm);
        const userData = {
            age: parseInt(formData.get('age')),
            income: parseInt(formData.get('income')),
            occupation: formData.get('occupation'),
            gender: formData.get('gender'),
            caste: formData.get('caste'),
            location: formData.get('location'),
            disability: formData.get('disability')
        };

        const results = engine.predict(userData);
        renderResults(results);

        // UI Transition
        formSection.classList.add('hidden');
        resultsSection.classList.remove('hidden');

        // Smooth scroll to results
        setTimeout(() => {
            resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 100);
    });

    // Back Button
    backBtn.addEventListener('click', () => {
        resultsSection.classList.add('hidden');
        formSection.classList.remove('hidden');
    });

    // Close Modal
    closeModal.addEventListener('click', () => {
        modal.classList.add('hidden');
    });

    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.add('hidden');
        }
    });

    function renderResults(results) {
        schemesList.innerHTML = '';

        if (results.length === 0) {
            schemesList.innerHTML = `
                <div class="glass-card" style="text-align: center; padding: 4rem; grid-column: 1 / -1; background: hsla(0, 0%, 100%, 0.02);">
                    <div style="font-size: 4rem; margin-bottom: 1.5rem;">🔍</div>
                    <h3 style="font-size: 1.8rem; margin-bottom: 1rem; font-weight: 800;">No matching schemes found</h3>
                    <p style="color: var(--text-muted); font-size: 1.1rem; max-width: 400px; margin: 0 auto;">Try adjusting your profile details (e.g., lower income or different occupation) to see more options.</p>
                </div>
            `;
            return;
        }

        results.forEach((scheme, index) => {
            const card = document.createElement('div');
            card.className = 'scheme-card';

            // Staggered Entry Animation
            card.style.opacity = '0';
            card.style.transform = 'translateY(30px)';

            card.innerHTML = `
                <div class="scheme-header">
                    <span class="scheme-category">${scheme.category}</span>
                    <span class="priority-badge">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14l-5-4.87 6.91-1.01L12 2z"/></svg>
                        Fit ${scheme.priorityScore}%
                    </span>
                </div>
                <h3 class="scheme-name">${scheme.name}</h3>
                <p class="scheme-desc">${scheme.description}</p>
                <div class="documents-list">
                    ${scheme.documents.slice(0, 3).map(doc => `<span class="doc-tag">${doc}</span>`).join('')}
                    ${scheme.documents.length > 3 ? `<span class="doc-tag" style="background: var(--primary-glow); color: var(--text-main);">+${scheme.documents.length - 3} more</span>` : ''}
                </div>
            `;

            card.addEventListener('click', () => showSchemeDetails(scheme));
            schemesList.appendChild(card);

            // Trigger animation with delay
            setTimeout(() => {
                card.style.transition = 'all 0.6s cubic-bezier(0.23, 1, 0.32, 1)';
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }, index * 100);
        });
    }

    function showSchemeDetails(scheme) {
        const fullScheme = SCHEMES_DATA.find(s => s.id === scheme.schemeId);

        modalBody.innerHTML = `
            <div class="modal-header">
                <span class="scheme-category" style="background: hsla(var(--h-primary), var(--s-primary), var(--l-primary), 0.15); color: var(--primary); padding: 6px 14px; border-radius: 100px; font-weight: 800; font-size: 0.75rem; text-transform: uppercase;">${scheme.category}</span>
                <h2 style="margin-top: 1.5rem; font-size: 2.2rem; font-weight: 800; letter-spacing: -0.02em;">${scheme.name}</h2>
                <div class="priority-badge" style="width: fit-content; margin-top: 1rem; font-size: 1rem; padding: 0.6rem 1.25rem; background: hsla(150, 80%, 45%, 0.1); color: var(--accent-green); border-radius: 100px; display: flex; align-items: center; gap: 8px; font-weight: 800;">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14l-5-4.87 6.91-1.01L12 2z"/></svg>
                    Fit Score: ${scheme.priorityScore}%
                </div>
            </div>
            
            <div class="modal-section" style="margin-top: 2.5rem;">
                <h4 style="color: var(--primary); text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.85rem; margin-bottom: 1rem; font-weight: 800;">Overview</h4>
                <p style="color: var(--text-muted); line-height: 1.7; font-size: 1.1rem;">${scheme.description}</p>
            </div>
            
            <div class="modal-section">
                <h4 style="color: var(--primary); text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.85rem; margin-bottom: 1rem; font-weight: 800;">Document Checklist</h4>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
                    ${scheme.documents.map(doc => `
                        <div style="display: flex; align-items: center; gap: 12px; padding: 1rem; background: hsla(0, 0%, 100%, 0.03); border: 1px solid hsla(0, 0%, 100%, 0.05); border-radius: 16px;">
                            <div style="width: 20px; height: 20px; border-radius: 6px; background: hsla(150, 80%, 45%, 0.2); display: flex; align-items: center; justify-content: center;">
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--accent-green)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            </div>
                            <span style="font-size: 0.95rem; font-weight: 500; color: var(--text-main);">${doc}</span>
                        </div>
                    `).join('')}
                </div>
            </div>
            
            <div class="modal-section">
                <h4 style="color: var(--primary); text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.85rem; margin-bottom: 1rem; font-weight: 800;">Application Process</h4>
                <div class="how-to-apply-box" style="background: linear-gradient(135deg, hsla(var(--h-primary), var(--s-primary), var(--l-primary), 0.1) 0%, transparent 100%); border: 1px solid hsla(var(--h-primary), var(--s-primary), var(--l-primary), 0.2); padding: 2rem; border-radius: 24px;">
                    <p style="color: var(--text-main); font-weight: 500; font-size: 1.15rem; line-height: 1.6;">
                        ${fullScheme ? fullScheme.how_to_apply : 'Connect with your local government center or visit the official portal for this department to start your application.'}
                    </p>
                </div>
            </div>
        `;

        modal.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
    }

    // Modal Events
    closeModal.addEventListener('click', () => {
        modal.classList.add('hidden');
        document.body.style.overflow = '';
    });

    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.add('hidden');
            document.body.style.overflow = '';
        }
    });
});
