/**
 * Smart Government Scheme Eligibility Predictor Logic
 */

class EligibilityEngine {
    constructor(schemes) {
        this.schemes = schemes;
    }

    predict(userData) {
        const results = [];

        for (const scheme of this.schemes) {
            let score = 0;
            let eligible = true;
            const criteria = scheme.criteria;

            // 1. Age Check
            if (criteria.min_age && userData.age < criteria.min_age) {
                eligible = false;
            }
            if (criteria.max_age && userData.age > criteria.max_age) {
                eligible = false;
            }
            if (criteria.age_limit && userData.age > criteria.age_limit) { // For backward compatibility
                eligible = false;
            }

            // 2. Gender Check (Case-insensitive)
            if (criteria.gender && userData.gender.toLowerCase() !== criteria.gender.toLowerCase()) {
                eligible = false;
            }

            // 3. Income Check
            if (criteria.income_limit && userData.income > criteria.income_limit) {
                eligible = false;
            }

            // 4. Location Check
            if (criteria.location && userData.location.toLowerCase() !== criteria.location.toLowerCase()) {
                eligible = false;
            }

            // 5. Caste/Category Check
            if (criteria.caste && criteria.caste.length > 0) {
                const userCaste = userData.caste.toLowerCase();
                const allowedCastes = criteria.caste.map(c => c.toLowerCase());

                if (!allowedCastes.includes(userCaste) && !allowedCastes.includes("any")) {
                    eligible = false;
                }
            }

            // 6. Occupation Check
            if (criteria.occupation && criteria.occupation.length > 0) {
                const userOcc = userData.occupation.toLowerCase();
                const matchesOccupation = criteria.occupation.some(occ =>
                    occ.toLowerCase() === "any" || occ.toLowerCase() === userOcc
                );
                if (!matchesOccupation) {
                    eligible = false;
                }
            }

            if (eligible) {
                // Priority Score Calculation (Simple version)
                // Base priority from scheme + Income factor
                let priorityScore = scheme.priority * 20; // 0-100 base

                // Increase priority for lower income
                if (userData.income < 50000) priorityScore += 20;
                else if (userData.income < 100000) priorityScore += 10;

                // Disability bonus
                if (userData.disability === "Yes") priorityScore += 15;

                results.push({
                    schemeId: scheme.id,
                    name: scheme.name,
                    category: scheme.category,
                    description: scheme.description,
                    priorityScore: Math.min(priorityScore, 100),
                    documents: scheme.documents
                });
            }
        }

        // Sort by priority score descending
        return results.sort((a, b) => b.priorityScore - a.priorityScore);
    }
}

// Export for use in main logic if needed, or keep global for simple script tag
if (typeof module !== 'undefined' && module.exports) {
    module.exports = EligibilityEngine;
} else {
    window.EligibilityEngine = EligibilityEngine;
}
