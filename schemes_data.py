SCHEMES_DATA = [
    {
        "id": "pm_kisan",
        "name": "PM-Kisan Samman Nidhi",
        "category": "Agriculture",
        "description": "Financial benefit of Rs. 6000/- per year in three equal installments to all land-holding farmer families.",
        "priority": 5,
        "criteria": {
            "occupation": ["Farmer"],
            "income_limit": None,
            "land_holding": True
        },
        "documents": ["Aadhaar Card", "Land Records", "Bank Account Details"],
        "how_to_apply": "Apply through the official PM-Kisan portal or visit your nearest Common Service Centre (CSC)."
    },
    {
        "id": "mgnrega",
        "name": "MGNREGA",
        "category": "Employment",
        "description": "Guarantees at least 100 days of wage employment in a financial year to every rural household whose adult members volunteer to do unskilled manual work.",
        "priority": 4,
        "criteria": {
            "location": "Rural",
            "occupation": ["Unskilled Laborer", "Laborer", "Any"]
        },
        "documents": ["Job Card", "Aadhaar Card", "Bank Passbook"],
        "how_to_apply": "Submit a written application to the local Gram Panchayat for a Job Card."
    },
    {
        "id": "pmay_g",
        "name": "PM-Awas Yojana (Gramin)",
        "category": "Housing",
        "description": "Provides financial assistance to rural BPL households for construction of houses.",
        "priority": 5,
        "criteria": {
            "location": "Rural",
            "income_limit": 120000,
            "caste": ["SC", "ST", "BPL"]
        },
        "documents": ["Income Certificate", "Caste Certificate", "BPL Card", "Aadhaar Card"],
        "how_to_apply": "Beneficiaries are selected based on SECC 2011 data. Contact your Gram Panchayat for inclusion."
    },
    {
        "id": "ayushman_bharat",
        "name": "Ayushman Bharat (PM-JAY)",
        "category": "Health",
        "description": "National Health Insurance Scheme that provides a health cover of up to Rs. 5 lakhs per family per year for secondary and tertiary care hospitalization.",
        "priority": 5,
        "criteria": {
            "income_limit": 250000,
            "caste": ["BPL", "Any"]
        },
        "documents": ["Aadhaar Card", "Ration Card", "PM Letter"],
        "how_to_apply": "Visit any empanelled public or private hospital with your Golden Card or Aadhaar Card."
    },
    {
        "id": "sukanya_samriddhi",
        "name": "Sukanya Samriddhi Yojana",
        "category": "Financial",
        "description": "A small deposit scheme for the girl child launched as a part of the 'Beti Bachao Beti Padhao' campaign.",
        "priority": 3,
        "criteria": {
            "gender": "Female",
            "max_age": 10
        },
        "documents": ["Girl Child Birth Certificate", "Aadhaar of Parent", "Photo"],
        "how_to_apply": "Open an account at any Post Office or authorised branch of commercial banks."
    },
    {
        "id": "pm_ujjwala",
        "name": "PM-Ujjwala Yojana",
        "category": "Energy",
        "description": "Provides LPG connections to women from Below Poverty Line (BPL) households.",
        "priority": 4,
        "criteria": {
            "gender": "Female",
            "income_limit": 100000,
            "caste": ["BPL", "SC", "ST"]
        },
        "documents": ["BPL Ration Card", "Aadhaar Card", "Bank Account"],
        "how_to_apply": "Apply at the nearest LPG distributor or through the PMUY website."
    },
    {
        "id": "pm_mudra",
        "name": "PM Mudra Yojana",
        "category": "Business",
        "description": "Provides loans up to 10 lakhs to non-corporate, non-farm small/micro enterprises.",
        "priority": 4,
        "criteria": {
            "occupation": ["Small Business", "Other"],
            "income_limit": None
        },
        "documents": ["Business Plan", "Address Proof", "Photo ID", "Caste Certificate"],
        "how_to_apply": "Apply at any public/private sector bank, Regional Rural Bank, or Micro Finance Institute."
    },
    {
        "id": "atal_pension",
        "name": "Atal Pension Yojana",
        "category": "Social Security",
        "description": "A pension scheme mainly aimed at the unorganized sector, providing a guaranteed minimum pension.",
        "priority": 3,
        "criteria": {
            "min_age": 18,
            "max_age": 40
        },
        "documents": ["Bank Account", "Aadhaar Card", "Mobile Number"],
        "how_to_apply": "Apply through your bank where you hold a savings account."
    },
    {
        "id": "pm_jeevan_jyoti",
        "name": "PM Jeevan Jyoti Bima Yojana",
        "category": "Insurance",
        "description": "A one-year life insurance scheme renewable from year to year, offering coverage for death due to any reason.",
        "priority": 3,
        "criteria": {
            "min_age": 18,
            "max_age": 50
        },
        "documents": ["Bank Account", "Aadhaar Card", "Consent Form"],
        "how_to_apply": "Enroll through your bank or insurance company."
    },
    {
        "id": "nsap_oldage",
        "name": "National Old Age Pension Scheme",
        "category": "Social Security",
        "description": "Monthly pension for elderly citizens living below the poverty line.",
        "priority": 4,
        "criteria": {
            "min_age": 60,
            "caste": ["BPL"]
        },
        "documents": ["Age Proof", "BPL Card", "Bank Passbook"],
        "how_to_apply": "Apply at the Block Development Office (BDO) or Municipality Office."
    },
    {
        "id": "pm_matru_vandana",
        "name": "PM Matru Vandana Yojana",
        "category": "Health",
        "description": "Maternity benefit scheme for pregnant and lactating mothers for the first live birth.",
        "priority": 4,
        "criteria": {
            "gender": "Female",
            "min_age": 19
        },
        "documents": ["Mother-Child Protection Card", "Aadhaar Card", "Bank Account"],
        "how_to_apply": "Register at the nearest Anganwadi Centre or approved Health Facility."
    }
]
