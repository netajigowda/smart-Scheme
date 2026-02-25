class EligibilityEngine:
    def __init__(self, schemes):
        self.schemes = schemes

    def predict(self, user_data):
        results = []

        for scheme in self.schemes:
            eligible = True
            criteria = scheme["criteria"]

            # 1. Age Check
            if criteria.get("min_age") and user_data["age"] < criteria["min_age"]:
                eligible = False
            if criteria.get("max_age") and user_data["age"] > criteria["max_age"]:
                eligible = False
            if criteria.get("age_limit") and user_data["age"] > criteria["age_limit"]:
                eligible = False

            # 2. Gender Check
            if criteria.get("gender") and user_data["gender"].lower() != criteria["gender"].lower():
                eligible = False

            # 3. Income Check
            if criteria.get("income_limit") and user_data["income"] > criteria["income_limit"]:
                eligible = False

            # 4. Location Check
            if criteria.get("location") and user_data["location"].lower() != criteria["location"].lower():
                eligible = False

            # 5. Caste/Category Check
            if criteria.get("caste") and len(criteria["caste"]) > 0:
                user_caste = user_data["caste"].lower()
                allowed_castes = [c.lower() for c in criteria["caste"]]
                if user_caste not in allowed_castes and "any" not in allowed_castes:
                    eligible = False

            # 6. Occupation Check
            if criteria.get("occupation") and len(criteria["occupation"]) > 0:
                user_occ = user_data["occupation"].lower()
                allowed_occs = [o.lower() for o in criteria["occupation"]]
                if not any(occ == "any" or occ == user_occ for occ in allowed_occs):
                    eligible = False

            if eligible:
                # Priority Score Calculation
                priority_score = scheme["priority"] * 20
                if user_data["income"] < 50000:
                    priority_score += 20
                elif user_data["income"] < 100000:
                    priority_score += 10
                
                if user_data.get("disability") == "Yes":
                    priority_score += 15

                results.append({
                    "schemeId": scheme["id"],
                    "name": scheme["name"],
                    "category": scheme["category"],
                    "description": scheme["description"],
                    "priorityScore": min(priority_score, 100),
                    "documents": scheme["documents"],
                    "how_to_apply": scheme.get("how_to_apply", "")
                })

        # Sort by priority score descending
        return sorted(results, key=lambda x: x["priorityScore"], reverse=True)
