# Complex nested dictionary for practicing dictionary methods and operations

company_data = {
    "company_info": {
        "name": "TechCorp Solutions",
        "founded": 2010,
        "headquarters": {
            "address": "123 Innovation Drive",
            "city": "San Francisco",
            "state": "CA",
            "country": "USA",
            "coordinates": {"lat": 37.7749, "lng": -122.4194},
        },
        "industry": "Software Development",
        "employees_count": 2500,
        "revenue": 850000000,  # in USD
        "public": True,
    },
    "departments": {
        "engineering": {
            "head": "Alice Johnson",
            "budget": 15000000,
            "teams": {
                "backend": {
                    "members": ["John Doe", "Sarah Wilson", "Mike Chen", "Emily Davis"],
                    "technologies": ["Python", "Java", "Go", "PostgreSQL"],
                    "projects": {
                        "api_v2": {
                            "status": "in_progress",
                            "priority": "high",
                            "deadline": "2024-12-31",
                        },
                        "microservices_migration": {
                            "status": "planning",
                            "priority": "medium",
                            "deadline": "2025-03-15",
                        },
                    },
                },
                "frontend": {
                    "members": ["Lisa Park", "David Kim", "Anna Rodriguez"],
                    "technologies": ["React", "TypeScript", "CSS", "Webpack"],
                    "projects": {
                        "ui_redesign": {
                            "status": "completed",
                            "priority": "high",
                            "deadline": "2024-08-30",
                        },
                        "mobile_app": {
                            "status": "in_progress",
                            "priority": "high",
                            "deadline": "2024-11-20",
                        },
                    },
                },
                "devops": {
                    "members": ["Robert Taylor", "Jennifer Lee"],
                    "technologies": ["Docker", "Kubernetes", "AWS", "Terraform"],
                    "projects": {
                        "ci_cd_improvement": {
                            "status": "in_progress",
                            "priority": "medium",
                            "deadline": "2024-10-15",
                        }
                    },
                },
            },
        },
        "sales": {
            "head": "Michael Brown",
            "budget": 8000000,
            "regions": {
                "north_america": {
                    "manager": "Susan White",
                    "revenue": 45000000,
                    "clients": ["Apple", "Google", "Microsoft", "Netflix"],
                    "targets": {
                        "q1": 12000000,
                        "q2": 13000000,
                        "q3": 11000000,
                        "q4": 15000000,
                    },
                },
                "europe": {
                    "manager": "Hans Mueller",
                    "revenue": 32000000,
                    "clients": ["SAP", "Spotify", "ASML", "Siemens"],
                    "targets": {
                        "q1": 8000000,
                        "q2": 9000000,
                        "q3": 7500000,
                        "q4": 10000000,
                    },
                },
                "asia_pacific": {
                    "manager": "Yuki Tanaka",
                    "revenue": 28000000,
                    "clients": ["Sony", "Samsung", "Alibaba"],
                    "targets": {
                        "q1": 7000000,
                        "q2": 7500000,
                        "q3": 6800000,
                        "q4": 8200000,
                    },
                },
            },
        },
        "hr": {
            "head": "Patricia Garcia",
            "budget": 3000000,
            "metrics": {
                "employee_satisfaction": 4.2,
                "turnover_rate": 0.08,
                "diversity": {
                    "gender": {"male": 0.62, "female": 0.36, "other": 0.02},
                    "ethnicity": {
                        "white": 0.45,
                        "asian": 0.30,
                        "hispanic": 0.15,
                        "black": 0.08,
                        "other": 0.02,
                    },
                },
            },
            "benefits": {
                "health_insurance": True,
                "dental_insurance": True,
                "vision_insurance": True,
                "retirement_401k": {"match_percentage": 0.06, "vesting_years": 4},
                "vacation_days": 25,
                "sick_days": 10,
                "remote_work": True,
                "professional_development": {
                    "budget_per_employee": 2000,
                    "conference_allowance": 5000,
                },
            },
        },
    },
    "financials": {
        "quarterly_results": {
            "2024_q1": {
                "revenue": 210000000,
                "expenses": 180000000,
                "profit": 30000000,
            },
            "2024_q2": {
                "revenue": 220000000,
                "expenses": 185000000,
                "profit": 35000000,
            },
            "2023_q4": {
                "revenue": 200000000,
                "expenses": 175000000,
                "profit": 25000000,
            },
            "2023_q3": {
                "revenue": 195000000,
                "expenses": 170000000,
                "profit": 25000000,
            },
        },
        "investments": {
            "r_and_d": {"allocated": 50000000, "spent": 35000000},
            "marketing": {"allocated": 25000000, "spent": 22000000},
            "infrastructure": {"allocated": 30000000, "spent": 28000000},
        },
        "assets": {
            "cash": 150000000,
            "real_estate": 80000000,
            "equipment": 45000000,
            "intellectual_property": 120000000,
            "investments": {
                "stocks": 25000000,
                "bonds": 15000000,
                "crypto": {"bitcoin": 2000000, "ethereum": 1500000},
            },
        },
    },
    "products": {
        "cloudware_pro": {
            "type": "SaaS",
            "price": {"monthly": 99, "annual": 990},
            "users": 15000,
            "features": [
                "Advanced Analytics",
                "API Access",
                "24/7 Support",
                "Custom Integration",
            ],
            "ratings": {
                "overall": 4.6,
                "ease_of_use": 4.4,
                "features": 4.8,
                "support": 4.7,
            },
        },
        "data_insights": {
            "type": "Analytics Platform",
            "price": {"monthly": 199, "annual": 1990},
            "users": 8500,
            "features": [
                "Real-time Dashboards",
                "ML Models",
                "Data Export",
                "Team Collaboration",
            ],
            "ratings": {
                "overall": 4.3,
                "ease_of_use": 4.1,
                "features": 4.5,
                "support": 4.2,
            },
        },
        "mobile_sdk": {
            "type": "Development Tool",
            "price": {"free": 0, "pro": 49, "enterprise": 299},
            "downloads": 125000,
            "features": [
                "Cross-platform",
                "Push Notifications",
                "Analytics",
                "Cloud Sync",
            ],
            "ratings": {
                "overall": 4.5,
                "documentation": 4.3,
                "performance": 4.7,
                "support": 4.4,
            },
        },
    },
    "metadata": {
        "last_updated": "2024-08-15",
        "data_version": "3.2.1",
        "sources": ["internal_systems", "financial_reports", "hr_database"],
        "confidentiality": "internal",
        "next_review": "2024-11-15",
    },
}

# """
# print("=== DICTIONARY PRACTICE EXERCISES ===\n")

# # Basic dictionary operations
# print("1. BASIC OPERATIONS:")
# print(f"Company name: {company_data['company_info']['name']}")
# print(f"Number of main sections: {len(company_data)}")
# print(f"Top-level keys: {list(company_data.keys())}")

# print("\n2. NESTED ACCESS:")
# print(f"Engineering head: {company_data['departments']['engineering']['head']}")
# print(f"HQ coordinates: {company_data['company_info']['headquarters']['coordinates']}")

# print("\n3. USING get() METHOD:")
# # Safe access with default values
# print(f"Marketing budget: {company_data.get('marketing_budget', 'Not specified')}")
# print(f"Employee count: {company_data['company_info'].get('employees_count', 'Unknown')}")

# print("\n4. DICTIONARY METHODS TO PRACTICE:")
# print("- .keys(), .values(), .items()")
# print("- .get(), .pop(), .popitem()")
# print("- .update(), .setdefault()")
# print("- .clear(), .copy()")
# print("- .fromkeys()")

# print("\n5. SAMPLE OPERATIONS YOU CAN TRY:")
# print("""
# # Get all department names
# departments = list(company_data['departments'].keys())

# # Calculate total sales targets for North America
# na_targets = company_data['departments']['sales']['regions']['north_america']['targets']
# total_na_target = sum(na_targets.values())

# # Get all backend team members
# backend_members = company_data['departments']['engineering']['teams']['backend']['members']

# # Find all products with ratings above 4.5
# high_rated_products = {name: product for name, product in company_data['products'].items()
#                       if product['ratings']['overall'] > 4.5}

# # Extract all quarterly profits
# quarters = company_data['financials']['quarterly_results']
# profits = [quarter['profit'] for quarter in quarters.values()]

# # Update employee count
# company_data['company_info']['employees_count'] = 2600

# # Add new team member
# company_data['departments']['engineering']['teams']['backend']['members'].append('New Developer')

# # Get nested value safely with multiple .get() calls
# ceo = company_data.get('leadership', {}).get('ceo', 'Not specified')
# """)
# """
## Try some challenges:

# 1. Calculate the total revenue across all sales regions
print(company_data["departments"]["sales"]["regions"])
total_revenue = 0

## Using loop
for k, v in company_data["departments"]["sales"]["regions"].items():

    total_revenue = total_revenue + v.get("revenue", 0)
print("Total Revenue Generated: ", total_revenue)

## using list comprehension
profit = sum(
    data.get("revenue", 0)
    for data in company_data["departments"]["sales"]["regions"].values()
)
print("Another Profit: ", profit)

## Get all the technologies being using in engineering team
all_tech_set = set()

for team_data in company_data["departments"]["engineering"]["teams"].values():
    all_tech_set.update(team_data["technologies"])
print(all_tech_set)

## Get average ratings for all products
print(f"=================*3")

total_rating = 0
count = 0
for data in company_data["products"].values():
    count += 1
    total_rating += data["ratings"]["overall"]
print(total_rating / count)


## Add new team members
print("=====================================================================")
new_team = {
    "members": ["Robert Taylor", "Jennifer Lee"],
    "technologies": ["Docker", "Kubernetes", "AWS", "Terraform"],
    "projects": {
        "ci_cd_improvement": {
            "status": "in_progress",
            "priority": "medium",
            "deadline": "2024-10-15",
        }
    },
}

team_dict = company_data["departments"]["engineering"]["teams"]

team_data["testing"] = new_team

print(team_dict)
